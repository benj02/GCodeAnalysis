import sys

from gcode import parser

def main(argv):
  words = parser.parseString(parser.EXAMPLE)
  tools = parser.getTools(words)
  print words
  print tools

if __name__ == "__main__":
  main(sys.argv)
