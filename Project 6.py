from time import sleep
from os import system

name_list = []
contact_list = []

while(True):
    print("""1. Add a New Contact
2. View a Contact
3. Display all Contacts
0. Exit\n""")

    choice = int(input("Enter Your Choice: "))
    sleep(0.25)
    system('cls')
    if(choice == 1):
        name = str(input("Enter The Name: "))
        contact = int(input("Enter Contact Number: "))
        name_list.append(name)
        contact_list.append(contact)

        system('cls')
    elif(choice == 2):
        print("""1. Search by Name
0. Search by Contact\n""")
        usr_choice = int(input("Enter Your Choice: "))
        sleep(0.25)
        system('cls')
        if(usr_choice == 1):
            name = str(input("Enter the Name of Contact You want to Search: "))
            if(name in  name_list):
                index = name_list.index(name)
                system('cls')
                print(f"---     {name_list[index]}  :  {contact_list[index]}    ---")
                sleep(1)
                _ = input("press Enter to countine")
                system('cls')
            else:
                system('cls')
                print("     --------------     Sorry, Name Not Found     ---------------")
                sleep(0.25)
                _ = input("press Enter to countine")
                system('cls')
        elif(usr_choice == 0):
            contact = int(input("      Enter the Name of Contact You want to Search      "))
            if(contact in  contact_list):
                index = contact_list.index(contact)
                system('cls')
                print(f"---     {name_list[index]}  :  {contact_list[index]}    ---")
                sleep(1)
                _ = input("press Enter to countine")
                system('cls')
            else:
                system('cls')
                print("--------------     Sorry, Contact Not Found     ---------------")
                sleep(1)
                _ = input("press Enter to countine")
                system('cls')
        else:
            system('cls')
            print("---------------     INVALID  CHOICE     ---------------")
            sleep(0.25)
            _ = input("press Enter to countine")
            system('cls')
    elif(choice == 3):
        print("---------------     Contacts     ----------------")
        for index in range(0, len(name_list)):
            print(f"---     {name_list[index]}  :  {contact_list[index]}    ---")
            sleep(0.25)
            _ = input("press Enter to countine")
    elif(choice == 0):
        print("---------------     Thanks For Using Our Software!!!     ---------------")
        break
    else:
        system('cls')
        print("---------------     INVALID  CHOICE     ---------------")
        sleep(0.25)
        system('cls')
        print("---------------     RESTARTING.........     ---------------")
        sleep(1)
        system('cls')
