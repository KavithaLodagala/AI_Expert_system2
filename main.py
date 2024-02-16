"""
we have implemented by using option#1 that is we used algorithm for building the AI expert system


******** File Name: Project1_A05252367_main.py **********
# This file contains the declaration and initilaization of variables
# It imports Project1_A05252367_Disorder_BW (BW) and Project1_A05252367_Drug_FW (FW) which are 
backward and forward chaining alogorithms respectively.
# In this file all the variables required for BW and FW are declared
# Backward (BW) : CONCLUSION_LIST, CLAUSE_VARIABLE_LIST, DISORDER_LIST, backward_conclusion
# Forward (FW) : FORWARD_CLAUSE_VARIABLE_LIST, forward_conclusion
**************************************************************
"""

import logging
import Project1_A05252367_Disorder_BW as BW
import Project1_A05252367_Drug_FW as FW
import time
import psutil

# CONCLUSION_LIST- It is a dictionary where it stores the rule number and conclusion of each rule 
# this is used in backward chaining algorithm
CONCLUSION_LIST = {
    1 : "DISORDER",
    2 : "ANXIETY" ,
    3 : "PERSONALITY DISEASE" ,
    4 : "DISORDER" ,
    5 : "DISORDER" ,
    6 : "DEPRESSION" ,
    7 : "DISORDER" ,
    8 : "DISORDER" ,
    9 : "DISORDER" ,
    10 : "PSYCHOTIC" ,
    11 : "CHRONIC BRAIN DISEASE" ,
    12 : "DISORDER" ,
    13 : "DISORDER" ,
    14 : "SLEEP DISEASE" ,
    15 : "DISORDER" ,
    16 : "DISORDER" ,
    17 : "DISORDER" ,
    18 : "DISORDER" ,
    19 : "DISORDER" ,
    20 : "DISORDER" ,
    21 : "DISORDER" ,
    22 : "EATING DISEASE" ,
    23 : "DISORDER" ,
    24 : "DISORDER" ,
    25 : "DISORDER" ,
    26 : "DISORDER" ,
    27 : "DISORDER" 
}

#CLAUSE_VARIABLE_LIST is a dictionary with clause number as key and variables of if clause are stored in a list as value to that key(clause number)
# This is used backward chaining algorithm and 10 slots for each rule

CLAUSE_VARIABLE_LIST= {
    1 : ["SICK"],
    11 : ["SICK", "IRRITABILITY","UNFOCUSED","RESTLESNESS"],
    21 : ["ANXIETY", "MOOD SWINGS" , "SOCIAL ISOLATION"],
    31 : ["PERSONALITY DISEASE", "AGITATION", "IMPULSIVITY", "COMPULSIVE BEHAVIOUR", "HYPERVIGILENCE", "RITUALISTIC BEHAVIOUR", "REPETITIVE BEHAVIOUR"],
    41 : ["PERSONALITY DISEASE", "BOREDOM", "DISTORTED SELF IMAGE", "EMPTYNESS", "LOSS OF INTEREST"],
    51 : ["ANXIETY", "SADNESS","ANGRY"],
    61 : ["DEPRESSION", "STEALING", "STEALING PLEASURE", "GUILT"],
    71 : ["DEPRESSION", "HYPERACTIVITY"],
    81 : ["DEPRESSION", "POOR APPETITE"],
    91 : ["DEPRESSION", "HALLUCINATION", "SUICIDAL THOUGHTS"],
    101 : ["DEPRESSION", "HALLUCINATION" , "SUICIDAL THOUGHTS", "MENTAL CONFUSION", "PARANOIA", "MENTAL DISORIENTATION", "MENTAL DECLINE", "LACK OF RESTRAINT", "NERVOUSNESS"],
    111 : ["CHRONIC BRAIN DISEASE", "JUMBLED SPEECH"],
    121 : ["CHRONIC BRAIN DISEASE", "SUSPICIOUS"],
    131 : ["PSYCHOTIC", "SLEEPLESSNESS"],
    141 : ["SLEEP DISEASE", "HEADACHE"],
    151 : ["SLEEP DISEASE", "HEADACHE", "LOSS OF MUSCLE", "CATAPLEXY", "SLEEP PARALYSIS"],
    161 : ["SLEEP DISEASE", "SLOW THINKING"],
    171 : ["PSYCHOTIC", "DELUSION", "DISORGANIZED THINKING", "LACK OF MOTIVATION", "AMNESIA", "INCOHERENT SPEECH", "EXCITABILITY"],
    181 : ["PSYCHOTIC", "DELUSION", "DISORGANIZED THINKING", "LACK OF MOTIVATION", "AMNESIA", "INCOHERENT SPEECH", "IDENTITY CONFUSION", "BLACKOUT"],
    191 : ["PSYCHOTIC", "DELUSION", "DISORGANIZED THINKING", "LACK OF MOTIVATION", "AMNESIA", "HOPELESSNESS", "HOSTILITY"],
    201 : ["PSYCHOTIC", "DELUSION", "DISORGANIZED THINKING", "LACK OF MOTIVATION", "AMNESIA", "HOPELESSNESS", "GRANDIOSITY"],
    211 : ["ANXIETY", "FATIGUE", "WEIGHT FLUCTUATIONS", "LACK OF CONFIDENCE"],
    221 : ["ANXIETY", "FATIGUE", "NIGHTMARES", "TRAUMA MEMORIES"],
    231 : ["ANXIETY", "FATIGUE", "WEIGHT FLUCTUATION", "CHEST PAIN"],
    241 : ["EATING DISEASE", "BODY THINKING", "APPEARANCE CHANGE", "BINGE EATING", "VOMITING", "FASTING", "LAXATIVE USE"],
    251 : ["ANXIETY", "FATIGUE", "WEIGHT FLUCTUATION", "CHEST PAIN", "DIZZINESS", "SWEATING", "NAUSEA", "HELPLESSNESS", "FEAR OF BEING ALONE"],
    261 : ["EATING DISEASE", "BODY THINKING", "APPEARANCE CHANGE", "PICKY SKIN"]
}


# FORWARD_CLAUSE_VARIABLE_LIST  this is dictionary with clause number as key and variables of if clause are stored in a list as a value to the key(clause number)
# This is used by forwarding chaining algorithm and 3 slots for each rule
FORWARD_CLAUSE_VARIABLE_LIST = {
    1 : ["DISORDER", "THOUGHT DISORDER"],
    4 : ["DISORDER", "COMPULSIVE HOARDING"],
    7 : ["DISORDER", "URGE TO STEAL"],
    10 : ["DISORDER", "TALKATIVENESS"],
    13 : ["DISORDER", "LOSS OF INTEREST"],
    16 : ["DISORDER", "INDECISIVENESS"],
    19 : ["DISORDER", "MEMORY LOSS"],
    22 : ["DISORDER", "PERSONALITY CHANGES"],
    25 : ["DISORDER", "LACK OF CONCENTRATION"],
    28 : ["DISORDER", "CHANGE IN REM SLEEP"],
    31 : ["DISORDER", "UNEXPLAINABLE BODY ACHES"],
    34 : ["DISORDER", "FEAR"],
    37 : ["DISORDER", "DEHYDRATION"],
    40 : ["DISORDER", "SWEATING"],
    43 : ["DISORDER", "POUNDING HEART RATE"],
    46 : ["DISORDER", "GENERAL DISCONTENT"],
    49 : ["DISORDER", "DEREALIZATION"],
    52 : ["DISORDER", "NONSENSE WORD REPETITION"],
    55 : ["DISORDER", "MANIA"]
}


#DISORDER_LIST is a list that will contain all disorders that needs to be diagnosed by the Backward chaining algorithm
DISORDER_LIST = ["BIPOLAR DISORDER", "SCHIZOPHRENIA", "SCHIZOAFFECTIVE DISORDER", "MAJOR DEPRESSIVE DISORDER",
 "PANIC DISORDER WITH AGORAPHOBIA", "DISSOCIATIVE IDENTITY DISORDER", "DYSTHYMIA", "GENERALIZED ANXIETY DISORDER", 
 "DEMENTIA", "POST TRAUMATIC STRESS DISORDER", "OBSESSIVE COMPULSIVE DISORDER", "PSYCHOSIS", "BODY DISMORPHIC DISORDER", 
 "INSOMNIA", "NARCOLEPSY", "BORDERLINE PERSONALITY DISORDER", "ALZHEIMERS DISEASE", "BULIMIA NERVOSA", "KLEPTOMANIA"]

# KNOWLEDGE BASE & VARIABLE LIST are created as seperate JSON files for better readability and access

# The output of backward chaining algorithm(i.e, disorder) is stored in backward_conclusions 
# The output of forward chaining algorithm(i.e, Treatment ) is stored in forward_conclusions
backward_conclusions = None
forward_conclusions=None

# derived variable of backward and forward chaining
DERIVED_VARIABLE_LIST={}
DERIVED_FORWARD_VARIABLE_LIST ={}


"""
************************ Function Name: main() *******************************
# This function first configures the logging where we can store the logs in Project1_A05252367_ITERATION_DETAILS.log file
# Then it calls the Backward chaining algorithm's process function and process returns the output(disorder is returned after process BW algorithm)
# The output of backward chaining(BW) is sent as input to the forwarding chaining algorithm's process function.
# The process function of FW returns the output(treatment is returned after processing the FW algorithm)
# Time and space calculated and displayed.
*******************************************************************************
"""

def main():
        
    # Create and configure logger
    logging.basicConfig(filename="Project1_A05252367_ITERATION_DETAILS.log",format='%(asctime)s %(message)s',filemode='w')
    # Creating an object
    LOG = logging.getLogger()
    # Setting the threshold of logger to DEBUG
    LOG.setLevel(logging.DEBUG)
    
    LOG.info("PROGRAM START")
    LOG.info("DEFINING THE GOAL VARIABLE AS DISORDER FOR BACKWARD CHAINING")
    LOG.info("CALLING BACKWARD CHAINING PROCESS FUNCTION")


    print("\n**********Kindly input YES or NO for each question***********\n")
    goal_variable = "DISORDER"

    #recording the start time to calculate the time taken by the backward chaining
    start_time_bw = time.perf_counter()

    # calling the backward chaining algorithm and output is stored disorder
    disorder = BW.process(goal_variable)

    #ending the timer as the backward chaining algorithm execution is completed
    end_time_bw = time.perf_counter()

    LOG.info("THIS IS THE GOAL IDENTIFIED BY BACKWARD CHAINING ALGORITHM :%s "% disorder)
    LOG.info("PASSING THE DISORDER TO FORWARD CHAINING AND CALLING THE FORWARD CHAINING PROCESS FUNCTION")

    
    # calculating time for BW by subtracting end time and start time
    print(f"\nTime Elapsed for Backward chaining : {end_time_bw - start_time_bw:0.2f} Secs")
    
    #checking whether person is having any disorder or not condition will be true if he is having some disorder else no disorder
    if disorder in DISORDER_LIST:
        print("You are suffering from  : ", disorder,"\n")

        # starting another timer to calculate the time taken by the forward chaining
        start_time_fw = time.perf_counter()

        # calling the forward chaining algorithm and output is stored treatment
        treatment = FW.process(disorder)

        #ending the timer as the forward chaining algorithm execution is completed
        end_time_fw = time.perf_counter()

        print("\nTreatment for" , disorder, " is : ",treatment)
        LOG.info("THIS IS THE GOAL IDENTIFIED BY FORWARD CHAINING ALGORITHM :%s "% treatment)

        # calculating time for FW by subtracting end time and start time
        print(f"\nTime Elapsed for Forward chaining :  {end_time_fw - start_time_fw:0.2f} Secs")
    else:
        print("You are not suffering from any disorder so no treatment required")
        LOG.info("No treatment required")

    # calculating the memory consumed by using psutil library in python
    memory = psutil.Process().memory_info().rss / (1024 * 1024)
    print("Memory consumed : ", memory, "MB\n")

# This calls the main function 
if __name__ == "__main__":
    main()