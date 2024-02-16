Project Title: INTELLIGENT EXPERT SYSTEM FOR DIAGNOSING MENTAL ILLNESSES AND TREATMENT

Project is implemented in Python language

Required software: Visual studio IDE, python interpreter

Instructions for downloading the visual studio
download the software from the link: https://visualstudio.microsoft.com/vs/features/python/

Installation of visual studio:
1. Make sure your computer is ready for Visual Studio
2. Download Visual Studio
3. Install the Visual Studio installer
4. After the new workloads and components are installed, choose Launch. Then choose install
5. For Python, select the Python development workload and select Install
6. select the installation location
7. Start programming


****Execution steps*****

1. The Project execution starts from the main program. Open the  main.py and click Run.
2. Now the execution will start and all the variables required are declared in the main file. The Main function imports 
  Disorder_BW.py(Backward chaining algorithm) and   Drug_FW.py (Forward chaining algorithm) files.
3. Knowledge base, variable list, intermediate node and derived variable lists are stored in separate Json files for both backward and forward chaining algorithm.
3. Once declaration is done and backward chaining algorithm is called which is in separate file  Disorder_BW.py and then we need to enter either  "yes" or "no" based on questions asked.
4. Once the user has responded to the questions, then backward chaining algorithm detects the disorder based on the symptoms given.
5. The obtained disorder will be passed as an input to the forward chaining which will determine the treatment after asking considering the user response.
6. Now the time taken by both algorithms is calculated and memory consumed is also determined.
7. All the outputs are displayed on 


