# 📱 Contact Manager

A simple Python **Contact Manager** that allows users to add, search, update, delete, and view contacts. This project is designed to practice important Python concepts such as **lists, dictionaries, loops, conditions, functions, input, and string methods**.

---

## 📌 Project Overview

The Contact Manager stores contacts in a Python list.

Each contact contains:

* **Name**
* **Phone Number**

The program provides a menu where the user can choose different operations.

---

## ✨ Features

* ➕ Add a new contact
* 🔍 Search for a contact
* ✏️ Update a contact
* 🗑️ Delete a contact
* 📋 Show all contacts
* 🚪 Exit the program
* 🔤 Search names without worrying about uppercase/lowercase

---

## 🐍 Python Concepts Used

This project uses several basic Python concepts:

* **List** — Stores all contacts
* **Dictionary** — Stores each contact's name and phone
* **while loop** — Keeps the program running
* **for loop** — Searches through contacts
* **if / elif / else** — Handles menu choices
* **input()** — Takes information from the user
* **append()** — Adds a contact to the list
* **remove()** — Deletes a contact
* **lower()** — Makes searching case-insensitive
* **break** — Stops the loop when needed

---

## 💻 Code

```python
contacts = []

while True:
    print("\n---Contact Manager---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contact = {
            "Name": name,
            "Phone": phone,
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["Name"].lower() == name.lower():
                print("Name:", contact["Name"])
                print("Phone:", contact["Phone"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to update: ")

        for contact in contacts:
            if contact["Name"].lower() == name.lower():
                contact["Name"] = input("Enter new name: ")
                contact["Phone"] = input("Enter new phone: ")

                print("Contact updated successfully!")
                break

    elif choice == "4":
        name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["Name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                break

    elif choice == "5":
        print("\nAll Contacts:")

        for contact in contacts:
            print(contact["Name"], "_", contact["Phone"])

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
```

> **Note:** I changed `elif choice >= "5"` to `elif choice == "6"` because option **6** is the Exit option. I also removed the `else` statements inside the update/delete loops because they could incorrectly show **"Contact not found"** before the program checks all contacts.

---

## 🧪 Example

### Add Contact

```text
---Contact Manager---
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Show All Contacts
6. Exit

Enter your choice: 1
Enter name: Rehan
Enter phone: 03001234567

Contact added successfully!
```

### Show Contacts

```text
All Contacts:
Rehan _ 03001234567
Bilal _ 03111234567
```

### Search Contact

```text
Enter name to search: rehan

Name: Rehan
Phone: 03001234567
```

### Delete Contact

```text
Enter name to delete: Rehan
Contact deleted successfully!
```

---

## 🔄 How It Works

### 1. Store Contacts

```python
contacts = []
```

An empty list is created to store all contacts.

Each contact is stored as a dictionary:

```python
contact = {
    "Name": "Rehan",
    "Phone": "03001234567"
}
```

---

### 2. Add Contact

The program asks for a name and phone number and then adds the contact using:

```python
contacts.append(contact)
```

---

### 3. Search Contact

The program uses a `for` loop to check every contact.

```python
for contact in contacts:
```

The `.lower()` method allows:

```text
Rehan
rehan
REHAN
```

to be treated as the same name.

---

### 4. Update Contact

The program finds the contact and changes its name and phone number.

```python
contact["Name"] = input("Enter new name: ")
contact["Phone"] = input("Enter new phone: ")
```

---

### 5. Delete Contact

The `remove()` method removes the selected contact.

```python
contacts.remove(contact)
```

---

### 6. Show All Contacts

The program uses a `for` loop to display every contact:

```python
for contact in contacts:
    print(contact["Name"], "_", contact["Phone"])
```

---

### 7. Exit

When the user chooses option `6`, the `break` statement stops the `while` loop.

```python
elif choice == "6":
    print("Goodbye!")
    break
```

---

## 📂 Project Structure

```text
Contact-Manager/
│
├── contact_manager.py
└── README.md
```

---

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Create the Python file

Save the code as:

```text
contact_manager.py
```

### 3. Run the program

Open your terminal and type:

```bash
python contact_manager.py
```

---

## 🎯 Purpose

This project is useful for practicing:

* Lists
* Dictionaries
* Loops
* Conditions
* User input
* String methods
* Adding and removing data
* Building menu-based Python programs

---

## 🚀 Future Improvements

You can improve this project by adding:

* Save contacts to a JSON file
* Prevent duplicate contacts
* Validate phone numbers
* Search by phone number
* Sort contacts alphabetically
* Add email addresses
* Add a graphical user interface (GUI)

---

## 👨‍💻 Author

**Muhammad Rehan**

> Beginner Python Developer | Learning Programming Step by Step

---

⭐ If you like this project, consider giving it a **star** on GitHub!

