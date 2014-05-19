import re
import parsimonious as p

EXAMPLE = """
G99 M42 (feed per rev, high gear if there is a gearbox on the machine)
T101 (tool #1, tool offset #1)
G50 S1500 (spindle speed limiting, this is very important for your safety!)
G96 S180 M3 (constant surface speed, 180m/min, or 180ft/min if you run your machine in imperial units, Spindle start CW)
G0 X105. Z0 M8 (rapid movement to position tool for facing, coolant on)
G1 X-1.6 F0.2 (facing the workpiece, X-1.6 instead of X0 to remove small nub which would be otherwise left on the center, F0.2 is feed 0.2mm/rev, or in/rev)
G0 X102. Z2. (rapid movement to position tool for roughing operation)
G71 U2. R0.2 (roughing cycle, U2 is radial depth of cut, R0.2 retraction amount)
G71 P1 Q2 U1. W0.1 F0.35 (roughing cycle, P1 and Q2 are start and end of desired shape, meaning it begins from N1 and ends to N2. U1. is amount of material left for G70 finishing cycle, this is a diametrical dimension. W0.1 is same for Z-axis. )
N1 G0 X19. (Start of the desired shape)
G1 G42 Z0.5 F0.18 (Cutter compensation on, approaching the face of workpiece)
X20. Z0
G3 X50. Z-15. R15. (Cutting an arc, these coordinates are the endpoint for arc. R15. means radius of the arc.)
G1 Z-25.
X99.
N2 G40 X102. (End of the desired shape)
G70 P1 Q2 (Finishing cycle, P1 and Q2 mean the same as in roughing cycle)
G0 X200. Z200. M9 (Rapiding the tool away from workpiece, coolant off)
M30
"""
NUM_EXAMPLE = "-100."

GCodeGrammar = p.Grammar(r"""
  program = demarcated_program / m30_terminated_program
  demarcated_program = ~"[^\%]"? "%" line* "%" anything?
  m30_terminated_program = line* ("M30" / "m30") anything?
  blank = (ws / break)+
  break = ("\n" / "\r\n")
  ws = ("\t" / " " / comment)
  comment = "(" ~"[^\)]*" ")"
  anything = ~".*"s

  line = (ws* word* ws*)* "\n"
  word = !"M30" ~"[a-zA-Z]" decimal # M30 is not considered a word, but a terminating metastring

  decimal = plusminus? ((number "." number) / ("." number) / (number ".") / number)
  integer = plusminus? number
  plusminus = "+" / "-"
  number = ~"[0-9]+"
""")
