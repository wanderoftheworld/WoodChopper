# Simple credit card processing. Run it like this:
# $ python3 app.py <input file>
# ----- OR ----
# $ cat <input file> | python3 app.py
#
# As the problem description says 'Keep It Simple', I chose not to
# use class to encapsulate command handling logic.
#
import sys

# Just a simple data class
class Account:
  def __init__(self, cc: str, limit: int, balance: int=0):
    self.cc = cc
    self.limit = limit
    self.balance = balance

def process_add(tokens, ledger):
  # Tom <cc> <amount>
  assert len(tokens) == 3
  if tokens[0] in ledger:
    raise ValueError('Account already exists for %s', tokens[0])
  cc = tokens[1]
  if not checkLuhn(cc):
    cc = -1
  ledger[tokens[0]] = Account(cc, int(tokens[2][1:]))

def process_charge(tokens, ledger):
  # Tom $500
  assert tokens[0] in ledger
  account = ledger[tokens[0]]
  if account.cc != -1:
    delta = int(tokens[1][1:])
    if account.limit >= account.balance + delta:
      account.balance += delta

def process_credit(tokens, ledger):
  # Lisa $100
  assert tokens[0] in ledger
  account = ledger[tokens[0]]
  if account.cc != -1:
    delta = int(tokens[1][1:])
    account.balance -= delta

def summarize(ledger):
  # Python dictionary is sorted by the order the item was added.
  for k in sorted(ledger):
    account = ledger[k]
    if account.cc == -1:
      print(k, ': error')
    else:
      print(k, ': $'+str(account.balance))

# Luhn algorithm - from geeksforgeeks.org/luhn-algorithm/
# Verbatim copy : DO NOT REFORMAT
# Returns true if given card number is valid
def checkLuhn(cardNo):

    nDigits = len(cardNo)
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False


def main(argv):
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')
  if argv:
    file = open(argv[0])
  else:
    file = sys.stdin

  ledger = {}
  for line in file:
    tokens = line.split()
    if tokens[0] == 'Add':
        process_add(tokens[1:], ledger)
    elif tokens[0] == 'Credit':
        process_credit(tokens[1:], ledger)
    elif tokens[0] == 'Charge':
        process_charge(tokens[1:], ledger)
    else:
        raise ValueError('Unrecognizable command %s', tokens[0])

  summarize(ledger)


if __name__ == "__main__":
  main(sys.argv[1:])
