import pyttsx3
import os

while True:
 print("Chat with me with your requirements:", end ='')
 

 p =input().casefold()
  
 

 if(("run" in p) or ("open" in p) or ("execute" in p)) and ("chrome" in p) and ("not" not in p):
    os.system("chrome")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")

     
 elif(("run" in p)or("execute" in p) or ("open" in p)) and (("notepad" in p)or("editor" in p)) and ("do not" not in p):
    os.system("notepad")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("player" in p) and ("media" in p) and ("do not" not in p):
    os.system("wmplayer")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("word document" in p) or ("ms-word" in p) or ("document" in p)) and ("do not" not in p):
    os.system("Word 2013")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("recorder" in p) or ("screen recorder" in p) or ("video maker" in p)) and ("do not" not in p):
    os.system("FRecorder")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("team viewer" in p) or ("remote desktop" in p) or ("remote connection" in p)) and ("do not" not in p):
    os.system("TeamViewer")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("internet explorer" in p) or ("microsoft explorer" in p) or ("browser" in p)) and ("do not" not in p):
    os.system("iexplore")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("java idle" in p) or ("netbeans" in p) or ("java file" in p)) and ("do not" not in p):
    os.system("netbeans")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("photo viewer" in p) or ("irfan view" in p) or ("view software" in p)) and ("do not" not in p):
    os.system("i_view64")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("python idle" in p) or ("python file" in p) or ("python script" in p)) and ("do not" not in p):
    os.system("python")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("image processing file" in p) or ("my file" in p) or ("python file" in p)) and ("do not" not in p):
    os.system("ASSIGN_1")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("winrar" in p) or ("extract file" in p)) and ("do not" not in p):
    os.system("WinRAR")
    print("")
    print("----------------------SUCESSFULLY LAUNCHED YOUR PROGRAM--------------------")
    print("")
 
 
 
    
 elif("exit" in p) or ("quit" in p):
    print("----------------THANKS FOR INTERACTING WITH US!!------------------")
    break    
 else:
    if ("do not" in p):
     print("")
     print("------------COMMAND ACCEPTED ,WILL NOT OPEN THIS PROGRAM FOR YOU!!-------------")
     print("")
    else:
     print("")
     print("---------SORRY!! TRY AGAIN---------------")
     print("")
    
