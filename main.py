contacts = []

while True:
    print("\n---Contact Manager---")
    print("1.  Add Contact")
    print("2.  Search Contact")
    print("3.  Update Contact")
    print("4.  Delete Contact")
    print("5.  Show All Contacts")
    print("6.  Exit")
    
    choice = input("Enter your choice:")
    
    if choice == "1":
        name = input("Enter name:")
        phone = input("Enter phone:")
        contact = {
            "Name":name,
            "Phone":phone,
        }
        contacts.append(contact)
        print("Contact added Successfully!")
    elif choice == "2":
        name = input("Enter name to search: ")
        found = False
        for contact in contacts:
         if  contact["Name"].lower() == name.lower():
             print("Name:",
contact["Name"])
             print("Phone:",
contact["Phone"])
             found = True
        if not found:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter name to update:")
        
        for contact in contacts:
         if contact["Name"].lower() == name.lower():
             contact["Name"] = input("Enter new name:")
             contact["Phone"] = input("Enter new phone:")
             print("Contact updated succesfully!")
             break 
         else:
             print("Contact not found.")
    elif choice == "4":
        name = input("Enter name to delete:")
        for contact in contacts:
         if contact["Name"].lower() == name.lower():
             contacts.remove(contact)
             print("contact deleted successfully!")
             break
         else:
             print("Contact not found.")
    elif choice == "5":
        print("\nAll Contacts:")
        for contact in contacts:
            print(contact["Name"],"_",contact["Phone"])
    elif choice >="5":
        print("Good bye!")
        break
    else:
        print("Invalid choice ")
         


    
    
    

       