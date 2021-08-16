# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:47:21 2021

@author: cflynch
"""



class Knowledge(object):
    """
    The Knowledge class represents a basic component that we know and supports
    the Fact and Rule classes.
    """

    def __init__(self, Justification):
        """
        

        Parameters
        ----------
        Justification : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.Justification = Justification
        
        
    def add_justification(self, Justification):
        pass
    
    
    def drop_justification(self, Justification):
        pass
    
    
    

class Fact(Knowledge):
    """
    This class represents a fact that we have in memory.
    
    It stores the contents of the fact and the source of it.
    """
    
    def __init__(self, Content Justification):
        """
        Initialize the fact in memory with at least one 
        justification which will be held on for use.

        Parameters
        ----------
        Content : String form of content.

        Justification : List or item.

        Returns
        -------
        None.

        """
        super().__init__(Justification)
        self.Content = Content
        
        
class Rule(Knowledge):
    """
    The Rule class provides for items that have consequences.

    of the form LHS > RHS.
    """

    def __init__(self, LHS, RHS, Justification):
        """
        Initialize a new rule with the LHS and RHS items.

        Parameters
        ----------
        LHS : List of items that must be true for this to hold.
            DESCRIPTION.
                
        RHS : The consequence of this being true.
            DESCRIPTION.
        Justification : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        super().__init__(Justification)        
        self.LHS = LHS
        self.RHS = RHS
        
        
    def known(self, KB):
        pass
    
    
    
    
    # Load a file.
    # Iterate over the file;
    #   For an add