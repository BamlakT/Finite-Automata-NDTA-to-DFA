from Int2_2_Question_2 import is_deterministic,is_complete



def Complementary_fun(alphabet, state_transition_matrix, states_list, initial_state_list, final_states_list):
    """
    Get the complementary of this automata

    Parameters:
        state_transition_matrix: FA transition 2D table(list of lists) 
        initial_state_list: list of initial states 
        final_state_list: list of final states
        states_list: list of FA states  
        alphabet: list of alphabet of the FA
     

    Returns:
        new_final_list: a list of new final states of complementary if possible
    """
    
    
    new_final_list=[]
    if is_deterministic(initial_state_list , state_transition_matrix):
        if is_complete(state_transition_matrix, alphabet):
            for state in states_list:
                if state not in final_states_list:
                    new_final_list.append(state)
            return new_final_list        
        else:
            print("\n \n \n In order to get the complementary of this automata, It should be Deterministic and Complete")
            print("However, this is not a Complete Automata. Please click option 5 first!")
            return final_states_list
            
    else:
        print("\n \n \n In order to get the complementary of this automata, It should be Deterministic and Complete")
        print("However, this is not a Deterministic Automata. Please click option 5 first!")
        return final_states_list
