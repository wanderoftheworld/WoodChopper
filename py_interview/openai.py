from typing import Tuple, Union
from typing_extensions import get_args


"""
We are implementing a data structure to power a simple spreadsheet. Our spreadsheet allows a user to enter values into arbitrary cells. The values can be either a) an integer or b) a sum of two cells (e.g. B3 + C1).

Your data structure should support set_cell(loc, value) and get_cell_value(loc) methods, where get_cell_value() should always return the final integer value for the cell. Note that a user can change the value in a cell by calling set_cell() on a cell with a previous value.
"""


class Spreadsheet(object):
    def __init__(self):
        self.sheet = {}
        # key: cell name, value: (current_val, formula)
    
    def set_cell(self, loc, value):
        # if value is int, set it - and go over all cells
        # that refers to me (possibly non recursive??)
        # if value is tuple, get the value, then go over all cells...
        if isinstance(value, int):
            newval = (value, None)
        else:
            x, y = value
            newval = (self.get_cell_value(x) + self.get_cell_value(y), value)
        self.sheet[loc] = newval
        # build adjacency map in order to dfs(start == loc)
        # map: key being cell name, value being the sister cells
        adj = {}
        for cell in self.sheet:
            simval, formula = self.sheet[cell]
            if not formula:
                continue
            # add 2 adj cell depend on both
            x, y = formula
            if cell not in adj:
                adj[cell] = [x, y]
            else:
                adj[cell].append(x)
                adj[cell].append(y)

        # Now dfs to discover the cells that need two
        # updated
        path = []
        def dfs(adj, start):
            if cell not in adj:
                # woohoo - no one depends on me
                return
            path.extend(adj[cell])
            for element in adj[cell]:
                dfs(adj, element)

        # update cells in the order discovered
        for cell in path:
            simval, formula = self.sheet[cell]
            x, y = formula
            simval = self.get_cell_value(x) + self.get_cell_value(y)
            self.sheet[cell][0] = simval

    def set_cell_o1(
        self,
        loc: str,
        value: Union[int, Tuple[str, str]],
    ):
        # validate 'value'
        if not isinstance(value, int):
            a, b = value
            if a not in self.sheet or b not in self.sheet:
                raise AssertionError("must only reference existing cells")
        self.sheet[loc] = value


    def get_cell_value(self, cell):
        return self.sheet[cell][0]

    def get_cell_value_on(self, loc: str):
        if loc not in self.sheet:
            raise AssertionError("Bad key")
        val = self.sheet[loc]
        if isinstance(val, int):
            return val
        # try to locate the other 2 cells: ensure to do it
        # recursively
        ca, cb = val
        sum = 0
        if not isinstance(self.sheet[ca], int):
            #print('A cell', ca)
            sum += self.get_cell_value(ca)
        else:
            sum += self.sheet[ca]
        if not isinstance(self.sheet[cb], int):
            #print('B cell', cb)
            sum += self.get_cell_value(cb)
        else:
            sum += self.sheet[cb]
        return sum

      
def check_exception_raised(fnc, args, exception_type=AssertionError):
    try:
        fnc(*args)
        raise RuntimeError()
    except exception_type:
        pass
      

def test_spreadsheet(s_class):
    s = s_class()

    # ints
    s.set_cell("A", 3)
    s.set_cell("B", 5)
    s.set_cell("C", 1)
    assert s.get_cell_value("B") == 5
    check_exception_raised(s.get_cell_value, ["D"])

    # formulas
    s.set_cell("D", ("B", "C"))
    assert s.get_cell_value("D") == 6
    s.set_cell("E", ("B", "D"))
    assert s.get_cell_value("E") == 11
    s.set_cell("F", ("E", "D"))
    assert s.get_cell_value("F") == 17
    check_exception_raised(s.set_cell, ["G", ("B", "H")])

    # edits
    s.set_cell("C", ("B", "A"))
    assert s.get_cell_value("C") == 8
    assert s.get_cell_value("D") == 13
    assert s.get_cell_value("E") == 18
    assert s.get_cell_value("F") == 31
    s.set_cell("A", 1)
    assert s.get_cell_value("F") == 27
    assert s.get_cell_value("C") == 6
    s.set_cell("D", ("A", "C"))
    assert s.get_cell_value("D") == 7
    assert s.get_cell_value("F") == 19
    print("Passed tests!")

    
test_spreadsheet(Spreadsheet)
