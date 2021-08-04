#!/usr/bin/env python
# MapColor.py
# Skeleton Code.


# Imports
# ====================================
import networkx
import re
import copy
import sys


# Data Structures for the Graph.
# =================================

class Variable(object):
    """
    The Variables will be used to store 
    the individual variables for our 
    constraint poblem.  Each one will be
    defined from the file and will store 
    the total domain and the current 
    domain.
    """


    def __init__(self, Name, Values):
        """
        Set the initial value for the variables.
        """

        # Set the name.
        self.Name = Name
        
        # The full domain for the values.
        self.FullDomain = set(Values)
        
        # The current working domain for
        # the variable.
        self.CurrDomain = set(Values)


    def assignValue(self, Val):
        """
        Assign a specific value to the variable by
        cutting the domain down to a single value.
        """
        self.CurrDomain = set([Val])
        

    def dropValue(self, Val):
        """
        Drop the specified value from 
        the Current Domain.
        """
        self.CurrDomain.remove(Val)


    def restoreValue(self, Val):
        """
        Add in the value back into the 
        current domain.  Raise an error
        if it is not in the primary.
        """
        self.CurrDomain.add(Val)


    def resetCurrDomain(self):
        """
        Restore the oroginal domain.
        """
        self.CurrDomain = copy.copy(self.FullDomain)


    
                

class ConstraintGraph(object):
    """
    The constraint graph class will store the
    individual variables and not equal constraints.  
    """


    def __init__(self, Variables, Constraints):
        """
        Define the basic contents.
        """

        # Set storage for the variables and arcs.
        self.Variables   = {}
        #self.Constraints = set()

        # The relationship can be used as a graph.
        self.Graph = networkx.Graph()

        # Iterate over the variables and 
        # add them in by name as a dict.
        for Var in Variables:
            
            Name = Var.Name
            
            self.Variables[Name] = Var
            self.Graph.add_node(Name, var=Var)

        # Now add the constraint pairs as
        # tuples and in the graph so that
        # we can find them later.
        for (VarA, VarB) in Constraints:

            self.Graph.add_edge(VarA, VarB)
            


    def isComplete(self):
        """
        Return True if this is complete, that is 
        each variable has only one value remaining
        in its current domain.
        """
        for Var in self.Variables:

            if (len(self.CurrDomain) != 1):
                return(False)
            
        return(True)
        


    def backtrackSearch(self):
        """
        Do the backtracking search algorithm.
        """
        pass


    def ac3(self):
        """
        Do AC3.
        """
        pass


    




# Read in the constraint code.
# =================================
VAR_START = re.compile("^VARS")
VAR_END   = re.compile("^ENDVARS")
VAR_ROW   = re.compile("^(?P<Name>[A-Z]+) : (?P<Vals>[A-Za-z0-9 ]+)")

    
def readConstraintGraph(InFile):
    """
    Read in the constraint graph.  This 
    relies on the regular expressions
    to match each row.  
    """
    with open(InFile, "r") as Input:

        Variables   = readVars(Input)
        #Constraints = readConstraints(Input)

    # Now add in the construction.
    pass


def readVars(InputStream):
    """
    Read in the first var line then read until we 
    reach the endvars.  Then return the variables.
    """

    # Allocate storage for the vars.
    Variables = []
    
    # Read in and print the first line.
    First = InputStream.readline()[:-1]
    print("Reading: |{}|".format(First))

    if (VAR_START.match(First) == None):
        raise RuntimeError("Line Mismatch")

    # Read in each of the variable lines.
    NextLine = InputStream.readline()[:-1]
    while(VAR_END.match(NextLine) == None):

        # At this point we have a variable row so
        # Generate a match.
        print("Reading: |{}|".format(First))
        Match = VAR_ROW.match(NextLine)
        print("Groups found: {}".format(Match.groups()))

        # At this point the variable values should be split
        # via string.split and then a new variable instance
        # should be made.  That is left to students.

        # And read the next line.
        NextLine = InputStream.readline()[:-1]
        
        
    print("End vars read.")
    return(Variables)
        
def readConstraints(Input):
    print('you need to write this')

search = sys.argv[1]
infile = sys.argv[2]
readConstraintGraph(infile)