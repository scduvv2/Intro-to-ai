# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:47:21 2021

@author: cflynch
"""

import sys
import csv

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
    
    def __init__(self, Content, Justification):
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
    
def create_knowledge(DataRows):
    print('printing data rows: ',DataRows)    
    knowledge =[]
    rules=[] 
    facts=[]
    i=0
    for data in DataRows:
     
        # this is a rule. let us create a rule
        stringLets = data.split(' ')
        if stringLets[0] == 'Tell:' and '>' in data:
            # this is a tell rule create a tell rule
            for i in range(len(stringLets)):
                if '>' == stringLets[i]:
                    lhs = stringLets[i-1].split('+')                    
                    rhs = stringLets[i+1]                    
                    break
            rule = Rule(lhs,rhs,stringLets[0])
            rules.append(rule)
            if lhs in knowledge:
                executeRulesAndUpdateKnowledgeForRule(knowledge,rules,rule)
        elif stringLets[0] == 'Tell:' and '>' not in data:
            # this is a fact and create a fact
            lhs = stringLets[1]
            justification = stringLets[0]
            fact = Fact(lhs,justification)
            facts.append(fact)

            if lhs not in knowledge:
                knowledge.append(lhs)
                print('due to the fact ',fact.Justification,'-',fact.Content,':',knowledge)
            executeRulesAndUpdateKnowledgeForTell(knowledge,rules,fact)
        elif stringLets[0] == 'Retract:' and '>' not in data:
            # this is a fact and create a fact
            lhs = stringLets[1]
            justification = stringLets[0]
            fact = Fact(lhs,justification)    
            facts.append(fact)
            knowledge.remove(lhs)
            print('due to the fact ',fact.Justification,'-',fact.Content,':',knowledge)
            executeRulesAndUpdateKnowledgeForRetract(knowledge,rules,fact)


def executeRulesAndUpdateKnowledgeForTell(knowldge,rules,fact):

    for rule in rules:
        if is_LHS_in_Knowledge(rule.LHS,knowldge) and rule.RHS not in knowldge:
            knowldge.append(rule.RHS)
    print('due to the fact ',fact.Justification,'-',fact.Content,':',knowldge)
    pass

def is_LHS_in_Knowledge(s,l):
    len_s = len(s) #so we don't recompute length of s on every iteration
    return any(s == l[i:len_s+i] for i in range(len(l) - len_s+1))

def executeRulesAndUpdateKnowledgeForRule(knowldge,rules,rule):
        if is_LHS_in_Knowledge(rule.LHS,knowldge):
            knowldge.append(rule.RHS)

        for rule_in_list in rules:
            if is_LHS_in_Knowledge(rule_in_list.LHS,knowldge) and rule.RHS not in knowldge:
                 knowldge.append(rule.RHS)
        print('due to the rule ',rule.Justification,'-',rule.LHS,':',knowldge)


def executeRulesAndUpdateKnowledgeForRetract(knowldge,rules,fact):

    for rule in rules:
        if fact.Content in rule.LHS:
            knowldge.remove(rule.RHS)
    print('due to the fact ',fact.Justification,'-',fact.Content,':',knowldge)
    pass

def main():
    fileName = sys.argv[1]
    DataRows =[]
    
    
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
      
        for row in reader:
            DataRows.append(row[0])
    create_knowledge(DataRows)   
main()    