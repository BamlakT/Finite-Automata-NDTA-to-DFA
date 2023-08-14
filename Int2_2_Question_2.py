# -*- coding: utf-8 -*-


def is_deterministic(initial_state_list , state_transition_matrix):
    """
    A FA is considered to be déterministic if there is only only unique initial state and 
    no more than one transitions for the same alphabet on the same state

    Parameters:
        state_transition_matrix: FA transition 2D table(list of lists) 
        initial_state_list: list of initial states 
        
        
    Returns:
        boolean: if deterministic True else False
    """
    
    # if more than one initial state
    if len(initial_state_list) != 1:
        print("\n it is not deterministic FA since there is more than one initial states\n")
        return False
    #for every cell in matrix
    for row in state_transition_matrix:
        for column in row:
            #if cell contains a set more than one state return False
            if isinstance(column, set):
                if len(column)>1:
                    print("\nIt is NOT deterministic since there is more than one transitions for the same alphabet on the same state\n")
                    return False
    return True


def is_complete(state_transition_matrix, alphabet):
    """ Complete a Finite Automata

    Parameters:
        state_transition_matrix: FA transition 2D table(list of lists) 
        alphabet: list of alphabets of FA states
        
    Returns:
        Boolean: True if FA is complete else False
    """
    #if no alphabet 
    if alphabet ==['']:
        return True 
    #for every cell in the transition matrix..       
    for row in state_transition_matrix:
        for column in row:        
            #if -1(no transition) found
            if column == -1:
                print("\n it is not a complete autimata since there is empty in transition table\n")
                return False
    return True

def is_standard(initial_state_list, state_transition_matrix):
    """
    A finite automata is considered to be standardized if there is only one unique initial state and
    No transistions should go towards the initial state

    Parameters:
        state_transition_matrix: FA transition 2D table(list of lists) 
        initial_state_list: list of initial states   

    Returns:
        Boolean: True if FA is standard else False
    """
    # if there is only one initial state
    if len(initial_state_list) != 1:
        print("\n it is not standard since there is more than one initial states\n")
        return False
    initial_state = initial_state_list[0]   
    for row in state_transition_matrix:
        for column in row: 
            #we check if it is a set 
            #               if it is a set and if the initial state is in col then not standard
            #               or if col=initial state -> not standard else true 
            
            if (isinstance(column, set) and (int(initial_state) in column or initial_state in column )) or (column == int(initial_state) or column == initial_state):
                print("\nIt is NOT standard since there is a transistion that goes towards the initial state\n")
                return False        
    return True