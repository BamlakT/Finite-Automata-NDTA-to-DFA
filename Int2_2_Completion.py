# -*- coding: utf-8 -*-

import copy

#state_transition_matrix, 
def complete(state_transition_matrix, states_list):
    """ Complete a Finite Automata

    Parameters:
        state_transition_matrix: FA transition 2D table(list of lists) 
        states_list: states_list: list of FA states
        
    Returns:
        lists: Complete version of the FA
    """
    
    temp=[]
    junk_state_added = False
    new_state_transition =  copy.deepcopy(state_transition_matrix)
    #for each cell that is -1(empty) add a P state to it 
    for row in range(len(new_state_transition)):
        for col in range(len(new_state_transition[0])):
            if new_state_transition[row][col] == -1:
                if not junk_state_added:
                    states_list.append('P')
                    for i in range(len(new_state_transition[0])):
                        temp.append('P')
                    new_state_transition.append(temp)
                    junk_state_added = True
                new_state_transition[row][col]='P'            
    return new_state_transition, states_list