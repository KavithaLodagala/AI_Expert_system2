"""
we have implemented by using option#1 that is we used algorithm for building the AI expert system

************** File name:Project1_A05252367_Disorder_BW.py *****************

# This file is implementation Backward chaining algorithm. 
# This is called once Project1_A05252367_main.py execution starts.
# it import Project1_A05252367_main.py to use all the variables declared 
# knowledge base and variable list json files stored dictionary
# The execution starts from process function where "DISORDER" is passed from main

*****************************************************************************
"""


import Project1_A05252367_main as M
import json
import logging

# Creating an object
LOG = logging.getLogger()
LOG.setLevel(logging.DEBUG)


#READING AND LOADING ALL THE NECESSARY JSON FILES NEEDED FOR PROCESSING
json_file1 = open('Project1_A05252367_BW_KNOWLEDGE_BASE.json', "r")
kb_rules = json.load(json_file1)
json_file2 = open('Project1_A05252367_BW_VARIABLE_LIST.json', "r")
variable_list = json.load(json_file2)  
json_file3 = open('Project1_A05252367_BW_INTERMEDIATE_NODE.json', "r")
intermediate_node = json.load(json_file3)  
json_file1.close() 
json_file2.close()
json_file3.close()

# This variable stores all the rules which are executed by validate function
visited_rules=[]


"""
*****************************************************************************
# search_con(): This function searches goal_variable in CONCLUSION_LIST. 
# If the matching goal is found then it checks corresponding rule 
# whether it is already visited or not by using visited_rules. 
# If not visited then it return rule_number 
# else checks for another matching goal and process repeats again
# goal_variable: It is the string(goal) where it needs to be searched in CONCLUSION_LIST
# Rule number is returned to process function
*****************************************************************************
"""    

def search_con(goal_variable):
    LOG.info("INSIDE SEARCH_CON FUCNTION WITH GOAL VARIABLE :%s" % goal_variable)
    # assigning some invalid rule number if no rule is found this will be returned
    rule_num=-1
    
    # In CONCLUSION_LIST every value is checked for matching goal
    for ri,con in M.CONCLUSION_LIST.items():

        # checking goal variable with conclusions in conclusion_list and the corresponding rule should not be visited
        if(con==goal_variable and ri not in visited_rules):
            
            #store the rule and breaks from loop 
            rule_num=ri
            break

    LOG.info("THIS IS THE RULE TO BE PASSED TO NEXT FUNCTION:%s" % rule_num)

    return rule_num
        
"""
*****************************************************************************
# rule_to_clause(): This function converts rule number to clause number 
# Formula used is 10 * ( rule number -1)+1. Rules number are in the form of 1,2,3,..
# rule number: This is an integer which is calculated by search_con function and
# sent as input to rule_to_clause() function
# Clause number is calculated by using the formula and it is returned to process function
*****************************************************************************
"""    
def rule_to_clause(rule_number:int):
    
    #formula for calculating clause number
    clause_number=10*(rule_number-1)+1

    LOG.info("THIS IS THE CALCULATED CLAUSE NUMBER :%s "% clause_number)
    
    return clause_number
       
"""
*****************************************************************************
# update_VL: This function asks the user several questions
# It asks questions to get the values for the variables present in CLAUSE_VARIABLE_LIST for that clause number.
# The users input is stored in VARIABLE_LIST. But if the variable already instantiated then it just skips to ask 
# that question. If the variable occured is not present in VARIABLE_LIST then it calls process function as that
# variable is a intermediate node or if the intermediate node is already processed then we just skip.
# Every time we get answer from user then it is stored in DERIVED_VARIABLE_LIST
# clause number that is calculated by rule_to_clause function is passed as input to this function update_VL
*****************************************************************************
"""   

def update_VL(clause_number:int):
    LOG.info("INSIDE UPDATE VL FUNCTION AT WITH CLAUSE NUMBER :%s "% clause_number)

    #stores clause variable list corresponding to given clause number
    temp_clause_list=M.CLAUSE_VARIABLE_LIST[clause_number] 
    
    # If there is intermediate node in CLAUSE_VARIABLE_LIST for the given clause_number and it is not processed
    # then it just call process function which recursive call and execution continues once the intermediate node is processed
    for clause_var in temp_clause_list:
        
        #If variable is intermediate then condition will be true
        if(clause_var in intermediate_node.keys() ):
        
            #checking intermediate node value if this is empty then if condition will be true
            if(intermediate_node[clause_var]['SystemOutput']==""):

                #calls process function with intermediate node as input
                process(clause_var) 

    # checks every variable in CLAUSE_VARIABLE_LIST for the give clause_number and takes input from user
    for i in range(len(temp_clause_list)):  

            # If there is intermediate node  which is processed and generated value is "no" then condition
            # becomes false and exists the funtion as there is no need ask further question to the user
            if(temp_clause_list[i] in intermediate_node.keys() and intermediate_node[temp_clause_list[i]]['SystemOutput']=="no"):
                return "done"      

            # If the variable is present in variable_list then condition will be true
            if temp_clause_list[i] in variable_list:

                # if the variable is not instantiated then condition will be true
                if(variable_list[temp_clause_list[i]]['Userinput']==""):

                    # loop continues until every variable is instantiated for that clause number in clause_variable_list
                    while(1):

                        # Asking the user questions regarding the  symptoms which will be "yes" or "no"
                        inputvariable = input(variable_list[temp_clause_list[i]]["Question"]+""+temp_clause_list[i]+"? ")
                        
                        # checking if the user input is "yes" or "no" if he enters other than these.
                        # Same question will be asked again 
                        if inputvariable.lower() in  ["yes","no"]:
                            
                            # user response is valid and is stored in variable_list
                            variable_list[temp_clause_list[i]]['Userinput'] = inputvariable.lower()
                            break
                        
                    # stores user response in this variable
                    M.DERIVED_VARIABLE_LIST[temp_clause_list[i]] = variable_list[temp_clause_list[i]]['Userinput']   
                    
    LOG.info("UPDATING THE DERIVED VARIABLE LIST AS :%s "% M.DERIVED_VARIABLE_LIST)
    return "done"

"""
*****************************************************************************
# validate_ri(): This function checks the ri rule in kb_rules with the user input present in VARIABLE_LIST.
# Once it satisfies the kb rules then it will return corresponding conclusion else it will return None.
# It also adds every rule that is validated into visited_rules listwhich will later used in search_con to
# track rules which are executed
# FUNCTION INPUTS:
# ri : Rule number that we need to validate
# conclusion : it is just None value 
# FUNCTION RETURN:
# It will return conclusion variable. If the rule is satisfied it will return conclusion in kb_rules
# else returns None
*****************************************************************************
"""

def validate_ri(ri:int,conclusion:str):

    LOG.info("INSIDE UPDATE VALIDATE_RULE FUCNTION WITH RULE NUMNER :%s "% ri)

    #converting to string as rule numbers are stored as string in kb_rule
    rule_num = str(ri)

    # A local variable which is created to store the variables used in the rule ri
    symptoms_list=list(kb_rules[rule_num]['SYMPTOMS'].keys())

    LOG.info("PRINTING THE SYMPTOM PRESENT IN KNOWLEGE BASE :%s "% symptoms_list)
    
    # A flag to track whether the rule is satisfied or not
    # flag=1 rule not satisfied and flag=0 rule satisfied
    flag=0

    #append that rule into visited
    visited_rules.append(ri)

    # checks each variable in kb rule(ri) with userInput if there is any mismatch loop breaks and returns None
    # else assigns conclusion variable with conclusion in kb_rule(ri) and then return conclusion
    for symptom in symptoms_list:

        # check whether the user input in variable_list is matching with kb_rules or not
        # check if the intermediate node is satisfied or not
        if((symptom  in variable_list and kb_rules[rule_num]['SYMPTOMS'][symptom] == variable_list[symptom]['Userinput'])
          or (symptom in intermediate_node and kb_rules[rule_num]['SYMPTOMS'][symptom] == intermediate_node[symptom]['SystemOutput'])):
            continue
        else:
            #Rule is not satisfied and assigns flag to 1 and breaks from the loop
            flag=1
            break

    # flag =0 means the rule(ri) is satisfied and returns the conclusion
    if(flag == 0):
        conclusion=kb_rules[rule_num]['CONCLUSION']
        LOG.info("RULE IS SATISFIED AND THE CONCLUSION RETUREND IS :%s"% conclusion)

         # if the conclusion is intermediate variable then assign yes and add same in the derived_variable_list
        if(conclusion in intermediate_node.keys()):
            intermediate_node[conclusion]["SystemOutput"]="yes"
            M.DERIVED_VARIABLE_LIST[conclusion]=intermediate_node[conclusion]["SystemOutput"]
        return conclusion

    else:
        #rule is not satisfied if the conclusion is intermediate node then assign no and add same in the derived_variable_list
        if(kb_rules[rule_num]['CONCLUSION'] in intermediate_node.keys()):
            intermediate_node[kb_rules[rule_num]['CONCLUSION']]["SystemOutput"]="no"
            M.DERIVED_VARIABLE_LIST[kb_rules[rule_num]['CONCLUSION']]=intermediate_node[kb_rules[rule_num]['CONCLUSION']]["SystemOutput"]
    
        LOG.info("RULE IS NOT SATISFIED AND THE CONCLUSION RETUREND IS :%s"%None)
        return None
    
"""
*****************************************************************************
# process(): This function just process the goal by calling search_con,rule_to_clause, update_VL and validate_ri.
# The execution continues until goal is reached or if the user is not suffering then loop breaks.
# goal: Initially goal will be "DISORDER" and the process starts from this.
# returns conclusion that is some disorder which is in DISORDER_LIST or it can be none or no disorder 
# if the user is not sick

*****************************************************************************
"""
def process(goal):

    LOG.info("INSIDE THE PROCESS FUNCTION WITH GLOBAL VARIABLE :%s" % goal)
    
    #if the goal is intermediate node and is not processed then condition will be true
    # or if the goal is not occured and it is "no disorder" then condition will be true
    while((goal in intermediate_node.keys() and intermediate_node[goal]["SystemOutput"]=="") or 
     (goal not in intermediate_node.keys() and  M.backward_conclusions not in M.DISORDER_LIST and M.backward_conclusions != "NO DISORDER")):
        
        LOG.info("visited rules: %s" %visited_rules)
        # calling search_con function to find the rule number to the goal variable
        rule_num = search_con(goal)

        # The rules is passed as input to rule_to_clause and clause number is returned
        clause_num = rule_to_clause(rule_num)

        # calling update_vl function to ask the userinput for that rule
        d = update_VL(clause_num) 

        # once input taken from user validation of that rule  is done by calling validate_ri with rule ri and conclusion None as input
        M.backward_conclusions = validate_ri(rule_num,M.backward_conclusions)
        # if the ANXIETY is not satisfied then loop breaks
        # this is because ANXIETY is the mandatory symptom for all disorders if the user is not
        # feeling ANXIETY he is not having any disorder
        if intermediate_node["ANXIETY"]["SystemOutput"] == "no":
            break

        # flag1 to check if all the intermediate nodes are processed and still the conclusion is not occured
        # then flag1 will be 0 else if any intermediate node is not processed then flag will be 1 and for loop breaks 
        flag1=0
        for key in intermediate_node.keys():
            if intermediate_node[key]["SystemOutput"]=="" or intermediate_node[key]["SystemOutput"]=="yes" :
                flag1=1  
                break

        # while loop breaks as user is not suffering from any disorder
        if flag1==0:
            break
  
    #LOG.info("YOUR VALUE IS :%s" % M.backward_conclusions)
    
    # loading the conclusion value into DERIVED_VARIABLE_LIST
    M.DERIVED_VARIABLE_LIST["DISORDER"] = M.backward_conclusions

    # loading the DERIVED_VARIABLE_LIST into json file
    json_file = open('Project1_A05252367_BW_DERIVED_VARIABLE_LIST.json', "w")
    json.dump(M.DERIVED_VARIABLE_LIST, json_file, indent=6)
    json_file.close()

    #returning conclusion of backward_chaining that is goal value
    return M.backward_conclusions




