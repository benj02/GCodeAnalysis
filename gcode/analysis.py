import parsimonious as p

class GCodeVisitor(p.nodes.NodeVisitor):
  def __init__(self, ast):
    self.words = []
    self.visit(ast)
  def visit_word(self, node, vc):
    self.words.append(node)
  def generic_visit(self, node, vc):
    pass
