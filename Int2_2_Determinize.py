import copy


def determinize(alphabet, transition_table, states_list, initial_state_list, final_states_list):
    """
    A FA is considered to be déterministic if there is only only unique initial state and 
    no more than one transitions for the same alphabet on the same state

    Parameters:
        transition_table: FA transition 2D table(list of lists) 
        initial_state_list: list of initial states 
        final_state_list: list of final states
        states_list: list of FA states  
        alphabet: list of alphabet of the FA
        
    Returns:
        determinized version of the automats 
        alphabet, transition_table_noset, new_state_list, new_initial_list , new_final_list
    """
    
    
    
    #initialize and populate the new transition table 
    #size is len(states_list)*2) because the number of states might have greater no of states while determinizing
    #so we took the *2 to be safe
    new_transition_table = [[-1 for i in range(len(alphabet))] for j in range(len(states_list)*2)]
    initial_state_list= [ "".join(ini_state.strip()) for ini_state in initial_state_list]
    new_state_list= [set(initial_state_list)]    
    new_initial_list= new_state_list.copy()
    
    i=0
    while i< len(new_state_list):
        for j in range(len(transition_table[0])):             
            if not isinstance(new_state_list[i], set):
                new_state_list[i]={new_state_list[i]}
            new_transition_table=inner_det_fun(new_state_list,new_transition_table,transition_table,i,j)
            if not new_transition_table[i][j] in new_state_list and new_transition_table[i][j]!=-1 :
                new_state_list.append(new_transition_table[i][j])
        i+=1
    
    new_final_list=[]
    final_state_index=[]
    index=0
    for dt_states in new_state_list:
        for char in dt_states:
            if char in final_states_list:
                final_state_index.append(index)
                break  # once a final state is found,
                       #break out of the inner loop and move on to the next element
        index+=1
    
    new_initial_list = ["".join(sorted(list(new_initial_list[0])))]  
    new_state_list = ["".join([str(x) if not isinstance(x, str) else x for x in state]) for state in new_state_list]

    #new_state_list = ["".join(list(state)) for state in new_state_list] 
    new_state_list[0]=new_initial_list[0]
    
    for index in final_state_index:
        new_final_list.append(new_state_list[index])
    
                     
    #remove the used empty states greater than 
    new_transition_table = new_transition_table[:len(new_state_list)] 
    transition_table_noset = []
    # if a cell is found join it to string as it is already determinized and no sets needed        
    for row in new_transition_table:
        joined_row = []
        for cell in row:
            if isinstance(cell, set):
                #joined_cell = ''.join(cell)
                if isinstance(cell, str):
                    joined_cell = cell
                else:
                    joined_cell = ''.join([str(x) for x in cell])
                joined_row.append(joined_cell)
            else:
                joined_row.append(cell)                
        transition_table_noset.append(joined_row) 
    
    return alphabet, transition_table_noset, new_state_list, new_initial_list , new_final_list      
             
            
            
         
def inner_det_fun(new_state_list,new_transition_table,transition_table,i,j):
    for state in new_state_list[i].copy():
        state= int(str(state).strip())
        
        if new_transition_table[i][j] != -1 and transition_table[state][j] != -1:
            if isinstance(new_transition_table[i][j], set):  
                if isinstance(transition_table[state][j], set):
                    new_transition_table[i][j].update(transition_table[state][j])
                else:
                    new_transition_table[i][j].add(transition_table[state][j])
            else:
                if isinstance(transition_table[state][j], set):
                    new_transition_table[i][j]={new_transition_table[i][j]}
                    new_transition_table[i][j].update(transition_table[state][j])
                else:
                    new_transition_table[i][j] = {new_transition_table[i][j], transition_table[state][j]}                    
        else:
            if transition_table[state][j] != -1:
                if not isinstance(transition_table[state][j], set):
                    #print(transition_table[state][j])
                    new_transition_table[i][j]= set([transition_table[state][j]])
                else:
                    new_transition_table[i][j]= set(transition_table[state][j])
                    

    return new_transition_table        
    









































