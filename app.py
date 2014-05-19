import sys

from gcode import parser, analysis

def main(argv):
  ast = parser.GCodeGrammar.parse(parser.EXAMPLE)
  visitor = analysis.GCodeVisitor(ast)
  print [word.text for word in visitor.words if word.text[0] == "T"]

if __name__ == "__main__":
  main(sys.argv)
