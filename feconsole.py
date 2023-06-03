print("Welcome to the Fun Elektroniks Input Console developed by the FUNEWARE team.")
print("__Ver. 1.6__")
fepp = ["B.O.B. - model_name: bb1001", "Micro B.O.B - model_name: mbb299"]
ferp = ["FUN-PAD - model_name: funp2x2", "Beeping Cane - model_name: beec930"]
fep = ["Ander", "Alejandro", "Iker", "Alan", "Toño", "Luis", "Sebastian"]
feb = ["Dante - Lying to the team / Property damage"]
fepro = ["Custom Invention Design Making Service"]
fecsp = ["PCBs for starters"]
loop1 = 1 
while loop1 == 1:
     idlist = ["111-111-111", "122-001-003", "111-001-002", "122-002-004", "133-001-005", "144-001-006", "144-002-007"]
     idp = input("Please enter your ID Number. ")
     if idp in idlist:
         print("Access Granted.")
         access = 1
         break
     else:
         print("Access Denied. (Try Again.)")
         continue
while access == 1:
    print("What do you want to do? - To stop running the program enter an invalid input.")
    print("A- View all public FE projects")
    print("B- [CLASSIFIED] View all private FE projects")
    print("C- Get a list of the current members.")
    print("D- [SEMI-CLASSIFIED] Get a list of the current banned users.")
    print("E- Get a list of all available products and services.")
    print("F- [CLASSIFIED] Get a list of WIP products and services.")
    print("_________EXTRA INFO_________")
    print("NON-CLASSIFIED INFO: Information that is not classified and can be showed to the public.")
    print("SEMI-CLASSIFIED INFO: Information that only certain people have access to.")
    print("CLASSIFIED INFO: Information that only members of FE should have access to.")
    opt = input("Choose an option. ")
    if opt == "A":
        print("Public FE projects array:", fepp)
        print("------------------------Continue browsing!------------------------")
    elif opt == "B":
        print("[CLASSIFIED INFO] Private FE projects array:", ferp)
        print("------------------------Continue browsing!------------------------")
    elif opt == "C":
        print("Members of FE array:", fep)
        print("------------------------Continue browsing!------------------------")
    elif opt == "D":
        print("[SEMI-CLASSIFIED INFO] Banned users of FE array:", feb)
        print("------------------------Continue browsing!------------------------")
    elif opt == "E":
        print("FE Available products and services:", fepro)
        print("------------------------Continue browsing!------------------------")
    elif opt == "F":
        print("[CLASSIFIED INFO] WIP FE Products:", fecsp)
        print("------------------------Continue browsing!------------------------")
    else:
        opt2 = input("Wanna stop the program? Y | N ")
        if opt2 == "Y":
            print("Closing program...")
            for i in range(1, 11):
                print("Closing in..", i)
            print("Goodbye!")
            break
        else:
             print("------------------------Try Again------------------------")
             continue