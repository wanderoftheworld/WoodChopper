# `python3 solve.py`
from anytree import Node, RenderTree

root = Node('food')
cuisine_mexico = Node('Mexico', parent = root)
cuisine_french = Node('French', parent = root)
tacos = Node('Tacos', parent = cuisine_mexico)
bacon = Node('Bacon', parent = cuisine_french)
souffle = Node('Souffle', parent = cuisine_french)

print(RenderTree(root))
