# -*- coding: utf-8 -*-


import copy

def standardize(state_transition_matrix, states_list, initial_state_list, final_state_list):
    """
    A finite automata is considered to be stanadardized if there is only one unique initial state and
    No transistions should go towards the initial state

    Parameters:
        state_transition_matrix: FA transition 2D table(list of lists) 
        initial_state_list: list of initial states 
        final_state_list: list of final states
        states_list: list of FA states  

    Returns:
        lists after standardization
        new_state_transition, new_states_list, new_initial_state_list, new_final_state_list
    """
    
    #used deep copy so that we avoid reference by pointer error
    new_state_transition =  copy.deepcopy(state_transition_matrix)
    new_states_list = copy.deepcopy(states_list)
    new_initial_state_list = copy.deepcopy(initial_state_list)
    new_final_state_list=copy.deepcopy(final_state_list)
    
    
    #initialize and populate the i_list with {-1}
    i_list=[]  
    for j in range(0,len(state_transition_matrix[int(0)])):
        i_list.append(set([-1])) 
    #boolean if the initial state used to recognize an empty word    
    initial_recognizes_empty = False
    for state in initial_state_list:
        #used the strip function incase if state includes a whitespace
        if str(state).strip() in final_state_list:
            initial_recognizes_empty = True    
        for i in range(0, len(state_transition_matrix[0])):
            if -1 in i_list[i] and state_transition_matrix[int(state)][i] !=-1:
                i_list[i].remove(-1)
            if state_transition_matrix[int(state)][i]==-1:
                continue;    
            #check if the state is a set using isinstance set    
            if isinstance(state_transition_matrix[int(state)][i], set):                
                for state_incell in state_transition_matrix[int(state)][i]:
                    #check if it is not already is the list 
                    if not state_incell in i_list[i]:
                        i_list[i].add(state_incell)                        
            else:
                    i_list[i].add(state_transition_matrix[int(state)][i]) 
             
    #append the new state list to the new transition table           
    new_state_transition.append(i_list)
    #finlly we add the i state to make it simpler we added len(new_state_transition)-1 so that it is a number
    new_initial_state_list = [str(len(new_state_transition)-1)]
    new_states_list.append(str(len(new_state_transition)-1))
    #check if the previous automata used to recognize an empty word 
    #if so the standardized automata should also recognize an empty word
    if initial_recognizes_empty:
        new_final_state_list.append(str(len(new_state_transition)-1))    
    return new_state_transition, new_states_list, new_initial_state_list, new_final_state_list


