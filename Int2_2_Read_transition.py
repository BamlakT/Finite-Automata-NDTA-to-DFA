

def Read_transition_table(file_path):
    # Read the file
    with open(file_path, 'r') as f:
        file_contents = f.read()
        
    
    # Split the file into lines
    lines = file_contents.split('\n')


    # Extract the alphabet
    alphabet_line = lines[0].split('= ')
    alphabet = alphabet_line[1].split(',')

    # Extract the states
    states_line = lines[1].split('= ')
    states = states_line[1].split(',')

    # Extract the initial state
    initial_line = lines[2].split('= ')
    initial_state = initial_line[1].split(',')

    # Extract the final states
    final_line = lines[3].split('= ')
    final_states = final_line[1].split(',')

    # Initialize the transition table
    table = [[-1 for i in range(len(alphabet))] for j in range(len(states))]


    # Fill in the transition table
    for line in lines[4:]:       
       from_state, symbol, to_state = line.split(',')
       if from_state.isalpha() :
           from_state = states.index(from_state)
       symbol_index = alphabet.index(symbol)
       if table[int(from_state)][symbol_index]!=-1: 
           if isinstance(table[int(from_state)][symbol_index], set):
               table[int(from_state)][symbol_index].add(int(to_state))
           else:
               table[int(from_state)][symbol_index]={table[int(from_state)][symbol_index],to_state}
       else:
           table[int(from_state)][symbol_index] = to_state 
           
    print_table(alphabet, table, states,initial_state,final_states)
    return alphabet, table, states,initial_state,final_states    
        
        

def print_table(alphabet, table, states,initial_state,final_states):
    # Find the maximum length of any element in the table
    max_1=1
    for row in table:
        for elem in row:
            if isinstance(elem, set):
                max_1=max(max_1, len(elem)+(len(elem)//2))
            else:
                max_1=max(max_1, len(str(elem)))
    max_2=0
    for elem in states:
        max_2=max(max_2, len(str(elem)))
    max_len = max(max_1,max_2)
    
    
    
    print("--- Display of the Transition Table of the FA  ---\n")
    cell=" "
    print(" "+cell.ljust(max_len+5), end=" ")
    for symbol in alphabet:
        print(str(symbol).ljust(max_len), end="  ")
    print()
    border="--------"
    
    print(border.ljust(max_len-2) + (border.ljust(max_len))*len(alphabet))
    for i, state in enumerate(states):
        state=state.strip()    
        if (state in initial_state):
            if (state in final_states):
                print("↔ "+str(state).ljust(max_len+5), end="")
            else:
                print("→ "+str(state).ljust(max_len+5), end="")            
        elif state in final_states:
            print("← "+str(state).ljust(max_len+5), end="")  
        else:
            print("  "+str(state).ljust(max_len+5), end="")
        for j in range(len(alphabet)):
            if table[i][j] == -1:
                print(str("-").ljust(max_len), end='  ')         
            elif isinstance(table[i][j], set):
                if -1 in table[i][j]:
                    print(str("-").ljust(max_len), end='  ')
                else:
                    elem=','.join(str(x) for x in table[i][j])
                    print(str(elem).ljust(max_len), end='  ')   
            else:
                print(str(table[i][j]).ljust(max_len), end='  ')
        print()
    
        
    




