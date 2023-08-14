# -*- coding: utf-8 -*-

from Int2_2_Read_transition import Read_transition_table,print_table
from Int2_2_Question_2 import is_deterministic,is_complete,is_standard
from Int2_2_Determinize import determinize
from Int2_2_Complementary import Complementary_fun
from Int2_2_standardize import standardize
from Int2_2_Completion import complete





#initialize Global variables
alphabet, state_transition_matrix, states_list,initial_state_list,final_state_list= [],[],[],[],[]




def menu_input():
   
    Quit=False
    while not Quit:
        print("\n")
        print("Option 0: Print transition table")
        print("Option 1: Check if deterministic")
        print("Option 2: Check if deterministic and complete")
        print("Option 3: Check if Standardized")
        print("Option 4: Standardize the FA")
        print("Option 5: Determinize and complete the FA")
        print("Option 6: Get the complementary of the FA")
        print("Option 7: Quit ")
        print()
        print()
      
        
       
        given_input = input("\n Please enter a number between 0 et 7 to choose the options available\n")
        if 0 <= int(given_input) < 8:
            
    
            switch_result=Switch_Function(int(given_input))
            if switch_result == -2:
                #(Quit option chosed)
                Quit= True
                return True
            elif switch_result== -1:
                print("You haven't entered the right number")
            
               
    
    
    
    
def Switch_Function(given_input):
    
    global alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list
    if given_input == 0:
        #print table
        print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
       
        
    elif given_input == 1:
        #Option 1: Check if deterministic 
        #print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
        if is_deterministic(initial_state_list,state_transition_matrix):
            print("\nThe FA provided is deterministic\n")
        else:
            print("\nThe FA provided is NOT deterministic\n")
            
                
    elif given_input == 2:
        #Option 2: Check if deterministic and complete
        #print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
        if is_deterministic(initial_state_list,state_transition_matrix):
            #state_transition_matrix, states_list = complete(state_transition_matrix, states_list)
            if is_complete(state_transition_matrix, alphabet):
                print("\nThe FA provided is already Deterministic AND Complete.\n")
            else:
                print("\nThe FA provided is already Deterministic, however it is NOT Complete.\n")          
        else:
            print("\n The FA is Not Deterministic therefore cannot be 'Deterministic AND Complete' FA \n")         
    elif given_input == 3:
        #Check if Standardized"
        #print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
        if is_standard(initial_state_list, state_transition_matrix):
            print("\nThe FA provided is Standardized.\n")
        else:
            print("\nThe FA provided is NOT Standardized.\n")         
    elif given_input == 4:
        #Standardize the FA"        
        if is_standard(initial_state_list, state_transition_matrix):
            print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
            print("\nThe FA provided is ALREADY Standardized so no need to standardize it again.\n")
        else:
            st_state_transition_matrix, st_states_list,st_initial_state_list,st_final_state_list = standardize(state_transition_matrix, states_list, initial_state_list, final_state_list)
            print("\n \n After standardization............\n")
            print_table(alphabet, st_state_transition_matrix, st_states_list,st_initial_state_list,st_final_state_list)
            
    elif given_input == 5:
         #Determinize and complete the FA
         if is_deterministic(initial_state_list,state_transition_matrix):
             if is_complete(state_transition_matrix, alphabet):
                 # It is already determinized and complete no need to do anything
                 print("\nIt is already determinized and complete no need to do anything\n")
                 #print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
                 
             else:  
                 #Just complete it since it is already determinized
                 print("\nIt is already determinized but not complete so here is the completed table\n")
                 state_transition_matrix, states_list=complete(state_transition_matrix, states_list)
                 print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
         else:
             print("\n Here is the determinized and the Complete version\n")
             #It is not already deterministic so we should determinize it
             alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list = determinize(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
             #check if already complete: if not 
             if not is_complete(state_transition_matrix, alphabet):
                 state_transition_matrix, states_list=complete(state_transition_matrix, states_list)
             print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
    elif given_input == 6:
        final_state_list = Complementary_fun(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
        print_table(alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list)
    
    
    
    elif given_input == 7:
        print("\n*********** Goodbye! ***********\n")       

    else:
        #incorrect no given
        return -1
    if given_input == 7:
        #user wants to quit
        return -2
    else:
        #user typed the correct option
        return 0


def main():
    
    global alphabet, state_transition_matrix, states_list, initial_state_list, final_state_list
    Quit = False
    while not Quit:    
        #Ask user to choose which file to work with (1-44)
        
        given_input = input("\n Please enter the automation file number to work with (between 1 et 44) \n If you want to quit enter -1\n")
        if int(given_input)==-1:
            print("\n*********** Goodbye! ***********\n")
            break;
                  
        if not given_input.isdigit():
            print("You entered a non numeric value!!!!! \n Please a number between 1-44")
            continue
        if 0 < int(given_input) < 45 :
            alphabet, state_transition_matrix, states_list,initial_state_list,final_state_list = Read_transition_table('Int2_2_automata_files/Int2-2-'+ given_input+'.txt')
            if 30<int(given_input)<36:
                print("\n The chosen file is an asynchronous automata.\nPlease choose another number(1-30)or(36-44) to further proceed")
                continue;      
        else:
            print("Please make sure you have entered a number from 1 to 44")
            
        if menu_input():
            print("Are you sure you want to quit? \n  User clicked Yes")
            given_input=input("Are you sure you want to quit? if so click Yes \nElse, if you want to go back to menu1 click No \n")
            if given_input=="Yes" or given_input=="yes":
                Quit=True                     
        
        print("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n" )
        

    
main()