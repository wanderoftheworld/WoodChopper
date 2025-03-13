# To solve a boggle board, run:
# `python3 solve.py`
import copy
from pprint import pprint

class Trie(object):
  def __init__(self):
    self.child = {}
  def insert(self, word):
      current = self.child
      for l in word:
         if l not in current:
            current[l] = {}
         current = current[l]
      current['#']=1
  def search(self, word):
      current = self.child
      for l in word:
         if l not in current:
            return False
         current = current[l]
      return '#' in current
  def startsWith(self, prefix):
      current = self.child
      for l in prefix:
         if l not in current:
            return False
         current = current[l]
      return True

# 'board' contains letters; 'grid' marks traversal
def move_right(board, grid, row, column):
  if column < 3 and grid[row][column+1] is None:
    return board[row][column+1]
  return None

def move_left(board, grid, row, column):
  if column > 0 and grid[row][column-1] is None:
    return board[row][column-1]
  return None

def move_up(board, grid, row, column):
  if row > 0 and grid[row-1][column] is None:
    return board[row-1][column]
  return None

def move_down(board, grid, row, column):
  if row < 3 and grid[row+1][column] is None:
    return board[row+1][column]
  return None

def move_upleft(board, grid, row, column):
  if (row > 0 and column > 0) and grid[row-1][column-1] is None:
    return board[row-1][column-1]
  return None

def move_upright(board, grid, row, column):
  if (row > 0 and column < 3) and grid[row-1][column+1] is None:
    return board[row-1][column+1]
  return None

def move_downleft(board, grid, row, column):
  if (row < 3 and column > 0) and grid[row+1][column-1] is None:
    return board[row+1][column-1]
  return None

def move_downright(board, grid, row, column):
  if (row < 3 and column < 3) and grid[row+1][column+1] is None:
    return board[row+1][column+1]
  return None

words = set()
dictionary = Trie()

# Walk the board starting from (row, column)
def walk_from(board, row, column):
  grid = [[None for x in range(4)] for y in range(4)]
  grid[row][column] = 'Y'
  c = board[row][column]
  if c == 'q':
    c = 'qu'
  walk_partial(board, grid, c, row, column)

# The board has already been partially walked
def walk_partial(board, grid, prefix, row, column):
  c = move_right(board, grid, row, column)
  if c == 'q':
    c = 'qu'
  if c:
    g1 = copy.deepcopy(grid)
    g1[row][column+1] = 'Y'
    # check if a new word is formed
    word = prefix + c
    if dictionary.search(word):
      words.add(word)
    if dictionary.startsWith(word):
      walk_partial(board, g1, word, row, column+1)

  c = move_left(board, grid, row, column)
  if c == 'q':
    c = 'qu'
  if c:
    g2 = copy.deepcopy(grid)
    g2[row][column-1] = 'Y'
    # check if a new word is formed
    word = prefix + c
    if dictionary.search(word):
      words.add(word)
    if dictionary.startsWith(word):
      walk_partial(board, g2, word, row, column-1)

  c = move_up(board, grid, row, column)
  if c == 'q':
    c = 'qu'
  if c:
    g3 = copy.deepcopy(grid)
    g3[row-1][column] = 'Y'
    # check if a new word is formed
    word = prefix + c
    if dictionary.search(word):
      words.add(word)
    if dictionary.startsWith(word):
      walk_partial(board, g3, word, row-1, column)

  c = move_down(board, grid, row, column)
  if c == 'q':
    c = 'qu'
  if c:
    g4 = copy.deepcopy(grid)
    g4[row+1][column] = 'Y'
    # check if a new word is formed
    word = prefix + c
    if dictionary.search(word):
      words.add(word)
    if dictionary.startsWith(word):
      walk_partial(board, g4, word, row+1, column)

  c = move_upleft(board, grid, row, column)
  if c:
    g5 = copy.deepcopy(grid)
    g5[row-1][column-1] = 'Y'
    word = prefix + c
    if dictionary.search(word):
      words.add(word)
    if dictionary.startsWith(word):
      walk_partial(board, g5, word, row-1, column-1)

  c = move_upright(board, grid, row, column)
  if c:
    g6 = copy.deepcopy(grid)
    g6[row-1][column+1] = 'Y'
    word = prefix + c
    if dictionary.search(word):
      words.add(word)
    if dictionary.startsWith(word):
      walk_partial(board, g6, word, row-1, column+1)

  c = move_downleft(board, grid, row, column)
  if c:
    g7 = copy.deepcopy(grid)
    g7[row+1][column-1] = 'Y'
    word = prefix + c
    if dictionary.search(word):
      words.add(word)
    if dictionary.startsWith(word):
      walk_partial(board, g7, word, row+1, column-1)

  c = move_downright(board, grid, row, column)
  if c:
    g8 = copy.deepcopy(grid)
    g8[row+1][column+1] = 'Y'
    word = prefix + c
    if dictionary.search(word):
      words.add(word)
    if dictionary.startsWith(word):
      walk_partial(board, g8, word, row+1, column+1)

def solve(board):
  for x in range(4):
    for y in range(4):
      walk_from(board, x, y)
  print('Total words: ', len(words))
  sorted_by_points = dict()
  for word in words:
    points = score(word)
    if points in sorted_by_points:
      sorted_by_points[points].append(word)
    else:
      sorted_by_points[points] = [word]

  pprint(sorted_by_points)

with open('nwl2020.txt') as f:
  lines = f.readlines()
  for line in lines:
    word = line.strip()
    dictionary.insert(word)

letter_points = {'b':4, 'c':4, 'd':2, 'f':4, 'g':3, 'h':2, 'j':10, 'k':4, 'l':2, 'm':2, 'n':2, 'p':4, 'q':10, 'u':2, 'v':4, 'w':4, 'x':8, 'y':3, 'z':10}
wordln_points = {5:3, 6:6, 7:10, 8:15, 9:20}

board = 'venseatilmreaiss'
# DL: 2, TL: 3, DW: 4, TW: 9
tiles = '1111111111111111'

def to_array(s):
  if len(board) != 16:
    return None
  l = list(s)
  return [l[:4], l[4:8], l[8:12], l[12:]]

def score(word):
  sum = 0
  has_seen_q = False
  for l in word:
    if has_seen_q and l == 'u':
      has_seen_q = False
      continue
    if l in letter_points:
      sum += letter_points[l]
    else:
      sum += 1 
    # Has to handle 'Qu'
    if l == 'q':
      has_seen_q = True
  wordln = len(word)
  if wordln > 4:
    if wordln in wordln_points:
      sum += wordln_points[wordln]
    else:
      print("LONG WORD - add 20 points", word)
      sum += 20
  return sum

solve(to_array(board))
