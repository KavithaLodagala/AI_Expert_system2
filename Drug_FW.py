"""
we have implemented by using option#1 that is we used algorithm for building the AI expert system

************** File name:Project1_A05252367_Drug_FW.py *****************

# This file is implementation forward chaining algorithm. 
# This is called once Project1_A05252367_main.py  execution starts and Project1_A05252367_Disorder_BW.py is completed.
# it import Project1_A05252367_main.py to use all the variables declared 
# knowledge base and variable list json files stored as dictionary
# The execution starts from process function where diagnosed disorder which is 
# returned by process function in backward chaining algorithm is passed as input forward chaining process function from main 

"""

import Project1_A05252367_main  as M
import json
import logging

# Creating an object
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)

# goal variable is stored 
global_disorder_value : None

# conclusions and its value is stored
global_conclusion_variable_queue=[]

#ALL THE JSON FILES ARE LOADED HERE
json_file1 = open('Project1_A05252367_FW_KNOWLEDGE_BASE.json', "r")
forward_kb_rules = json.load(json_file1)
json_file1.close()
json_file2 = open('Project1_A05252367_FW_VARIABLE_LIST.json', "r")
forward_variable_list = json.load(json_file2)
json_file2.close()

# This variable stores all the clause numbers which are executed by validate function
visited_clause =[]

"""
*****************************************************************************
# search_con(): This function searches goal_variable in FORWARD_CLAUSE_VARIABLE_LIST. 
# If the matching goal is found then it checks corresponding clause_number 
# whether it is already visited or not by using visited_clause. 
# If not visited then it return clause_number 
# else checks for another matching goal and process repeats again
# goal_variable: It is the string(goal) where it needs to be searched in FORWARD_CLAUSE_VARIABLE_LIST.
# clause number is returned to process function
*****************************************************************************
"""    
def search_cvl(goal_variable): #get's the goal variable from the main function

        LOG.info("INSIDE SEARCH_CVL FUCNTION WITH GOAL VARIABLE :%s" % goal_variable)
        # assigning some invalid rule number if no rule is found this will be returned
        clause_num=-1

        # In FORWARD_CLAUSE_VARIABLE_LIST every value is checked for matching goal
        for key, value in M.FORWARD_CLAUSE_VARIABLE_LIST.items():

            # checking goal variable with variable in FORWARD_CLAUSE_VARIABLE_LIST and the corresponding clause_num should not be visited
            if goal_variable in value and key not in visited_clause:
                #store the clause number and breaks from loop 
                clause_num=key
                break     


        LOG.info("visited clause: %s" %visited_clause)
        LOG.info("THIS IS THE CLAUSE NUMBER TO BE PASSED TO NEXT FUNCTION:%s" % clause_num)   

        #returns clause number
        return clause_num

       
"""
*****************************************************************************
# update_VL: This function asks the user several questions
# It asks questions to get the values for the variables present in CLAUSE_VARIABLE_LIST for that clause number.
# The users input is stored in VARIABLE_LIST. But if the variable already instantiated then it just skips to ask that question. 
# It also adds every clause number that is visited into visited_rules list which will later used in search_con to
# track clause_numbers which are already executed.
# Every time we get answer from user then it is stored in DERIVED_VARIABLE_LIST
# clause_number : It is output returned by search_con function and it is passed as input to the update_VL 
*****************************************************************************
"""   

def update_VL(clause_number:int):
    LOG.info("INSIDE THE UPDATE_VL FUNCTION WITH CLAUSE NUMBER :%s " % clause_number)

    #stores clause variable list corresponding to given clause number
    fw_temp_clause_list=M.FORWARD_CLAUSE_VARIABLE_LIST[clause_number] 
    
    #append that clause numer into visited_clause list
    visited_clause.append(clause_number)

    #checking if the variable is instantiated in the variable list or not. If not, it will ask the user to provide the values of variables and instantiate them.  
    for i in range(len(fw_temp_clause_list)): 
        if fw_temp_clause_list[i] in forward_variable_list and forward_variable_list[fw_temp_clause_list[i]]["Userinput"]=="":
            while(1):
                # Asking the user questions regarding the  symptoms which will be "yes" or "no"
                inputvariable = input(forward_variable_list[fw_temp_clause_list[i]]['Question'] +" "+fw_temp_clause_list[i]+"? ")

                # checking if the user input is "yes" or "no" if he enters other than these.
                # Same question will be asked again 
                if inputvariable.lower() in  ["yes","no"]:
                    forward_variable_list[fw_temp_clause_list[i]]["Userinput"]  = inputvariable.lower()
                    break

            #forward_variable_list[fw_temp_clause_list[i]]["Userinput"] = input(forward_variable_list[fw_temp_clause_list[i]]['Question'] +" "+fw_temp_clause_list[i]+"? ")
            M.DERIVED_FORWARD_VARIABLE_LIST[fw_temp_clause_list[i]] = forward_variable_list[fw_temp_clause_list[i]]["Userinput"]
    LOG.info("UPDATING THE FORWARD DERIVED VARIABLE LIST AS :%s "% M.DERIVED_FORWARD_VARIABLE_LIST)
    
    
 
"""
*****************************************************************************
# rule_to_clause(): This function converts clause number to rule number 
# If rule numbers are in the pattern 1,2,3,4... then Rule number = {(Quotient (clause number/3))} +1)
# clause number: This is an integer which is calculated by search_con function and
# sent as input to clause_to_rule() function
# rule number is calculated by using the formula and it is returned to process function
*****************************************************************************
"""    
def clause_to_rule(clause_number:int):
    LOG.info("INSIDE THE CLAUSE_TO_RULE FUNCTION WITH CLAUSE NUMBER :%s " % clause_number)

    #formula for calculating rule number
    rule_number = int(clause_number//3)+1

    LOG.info("THIS IS THE CALCULATED RULE NUMBER :%s "% rule_number)
    
    # rule number is returned
    return rule_number

"""
*****************************************************************************
# validate_ri(): This function checks the ri rule in kb_rules with the user input present in VARIABLE_LIST.
# Once it satisfies the kb rules then it will return corresponding conclusion else it will return None.
# FUNCTION INPUTS:
# ri : Rule number that we need to validate
# conclusion : it is just None value 
# FUNCTION RETURN:
# It will return conclusion variable. If the rule is satisfied it will return conclusion in kb_rules
# else returns None
*****************************************************************************
"""

def validate_ri(ri:int):

    LOG.info("INSIDE UPDATE VALIDATE_RULE FUCNTION WITH RULE NUMNER :%s "% ri)
    rule_num = str(ri)

    # A local variable which is created to store the variables used in the rule
    symptoms_list=list(forward_kb_rules[rule_num]['SYMPTOMS'].keys())

    LOG.info("PRINTING THE SYMPTOM PRESENT IN FORWARD KNOWLEGE BASE :%s "% symptoms_list)

    # A flag to track whether the rule is satisfied or not
    flag=0

    # checks each variable in kb rule(ri) with userInput if there is any mismatch loop breaks and returns None
    # else assigns conclusion with conclusion in kb_rule(ri) and then return conclusion
    for symptom in symptoms_list:
        
        if((symptom  in forward_variable_list and forward_kb_rules[rule_num]['SYMPTOMS'][symptom] == forward_variable_list[symptom]['Userinput'])):
            continue
        else:

            #Rule is not satisfied
            flag=1
            break

    # flag =0 means the rule(ri) is satisfied and returns the conclusion
    if(flag == 0):
        
        LOG.info("RULE IS SATISFIED AND THE TREATMENT RETUREND IS :%s"% forward_kb_rules[rule_num]['TREATMENT'])
        
        # rule is satisfied and appends the conclusion into global_conclusion_variable
        global_conclusion_variable_queue.append(forward_kb_rules[rule_num]['TREATMENT'])
        return forward_kb_rules[rule_num]['TREATMENT']
    else:
        LOG.info("RULE IS NOT SATISFIED AND THE TREATMENT RETUREND IS :%s"%None)
    return None


 
"""
*****************************************************************************
# process(): This function just process the goal by calling search_con, update_VL, clause_to_rule and validate_ri.
# The execution continues until goal is reached or if the user is not suffering then loop breaks.
# "DISORDER" in Forward_variable_list is initialized with backward chaining algorithm output
# goal: Initially goal will be "DISORDER" and the process starts from this.
# returns conclusion that is some treatment to the disorder the user is suffering from.
*****************************************************************************
"""
def process(variable:str):
    LOG.info("INSIDE THE FORWARD PROCESS FUNCTION WITH GLOBAL VARIABLE :%s" % variable)

    # loop continues until conclusion is determined
    while(M.forward_conclusions==None):
        # assigning the backward chaining output to the variable_list
        forward_variable_list["DISORDER"]["Userinput"]=variable
        global_disorder_value = "DISORDER"

        # calling search_con function to find the clause number to the goal variable
        clause_num = search_cvl(global_disorder_value)

        # calling update_vl function to ask the userinput for that clause number
        update_VL(clause_num)

        # The clause is passed as input to clause_to_rule and rule number is returned
        rule_num=clause_to_rule(clause_num)

        # once input taken from user validation of that rule  is done by calling validate_ri with rule ri and conclusion None as input
        M.forward_conclusions = validate_ri(rule_num)
        

    # loading the conclusion value into DERIVED_VARIABLE_LIST
    M.DERIVED_FORWARD_VARIABLE_LIST["TREATMENT"] = M.forward_conclusions

    # loading the DERIVED_VARIABLE_LIST into json file
    json_file = open('Project1_A05252367_FW_DERIVED_VARIABLE_LIST.json', "w") 
    json.dump(M.DERIVED_FORWARD_VARIABLE_LIST, json_file, indent=6)
    json_file.close()
    
    #returning conclusion of backward_chaining that is goal value
    return M.forward_conclusions