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

words = set()
dictionary = Trie()

def solve(board, trie, path):
  for c in board:
    if c not in trie:
      continue
    #print('path, Trie:', path, trie[c])
    if '#' in trie[c] and board[0] in (path+c):
      word_maybe = path + c
      if word_maybe not in words:
        words.add(word_maybe)
        print(word_maybe)
    solve(board, trie[c], path + c)

with open('nwl2020.txt') as f:
  lines = f.readlines()
  for line in lines:
    word = line.strip()
    if len(word) >= 4:
      dictionary.insert(word)


# NYT spelling bee: letters can be reused; first letter MUST appear
board = 'vitacel'
solve(board, dictionary.child, '')
