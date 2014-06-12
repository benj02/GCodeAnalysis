import sys, re

from gcode import parser, analysis

numerics = ["0","1","2","3","4","5","6","7","8","9"]

def main(argv): # Only grabs T<number> but very simple
  text = re.sub(r"[\s]", "", parser.EXAMPLE) # We stip all whitespace because in GCode whitespace is irrelevant
  print text
  toolnums = []
  for x in range(len(text)):
    if text[x] in ["T"]:
      print text[x]
      toolnum = ""
      for y in text[x+1:]:
        if y in numerics:
          toolnum += y
        else:
          break
      toolnums.append(toolnum)
  print toolnums

def parseAST():
  filteredCode = re.sub(r"\s", "", parser.EXAMPLE) # We stip all whitespace because in GCode whitespace is irrelevant
  ast = parser.GCodeGrammar.parse(parser.EXAMPLE)
  visitor = analysis.GCodeVisitor(ast)
  print [word.text for word in visitor.words if word.text[0] == "T"]

if __name__ == "__main__":
  main(sys.argv)
