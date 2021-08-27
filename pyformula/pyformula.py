from sympy.solvers import solveset


class Formula:
    """
    Class definition Formula: 
    
    Save expression and create callable functions for each symbol
    
    ToDo:
      - Comments 
      - Function return sympy sets => Check better way so values can be used further
      - Check compatibility with numpy arrays
      - Error Handling, e.g. values for wrong arguments, or not enough supplied
    """
    def __init__(self, expr):
        """
        Initialize object
        
        :param expr:
        """
        self.expr = expr
        for sym in expr.free_symbols:
            self.__dict__[sym.name] = lambda **kwargs: solveset(expr.subs(kwargs))

    def __repr__(self):
        return str(self.expr)

    def __str__(self):
        return str(self.expr)
