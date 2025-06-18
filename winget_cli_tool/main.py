from winget_manager import *

def menu():
    print("\n==== Winget CLI Tool ====")
    print("1. List Upgradable Packages")
    print("2. Upgrade All Packages")
    print("3. Install Application")
    print("4. Uninstall Application")
    print("5. Manage Sources")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        list_upgradable_packages()
    elif choice == '2':
        upgrade_all_packages()
    elif choice == '3':
        pkg = input("Enter the package name to install: ")
        install_package(pkg)
    elif choice == '4':
        pkg = input("Enter the package name to uninstall: ")
        uninstall_package(pkg)
    elif choice == '5':
        manage_sources()
    elif choice == '6':
        print("Exiting Winget CLI Tool. Goodbye!")
        exit()
    else:
        print("Invalid choice! Please try again.")

def manage_sources():
    print("\n--- Source Management ---")
    print("1. List Sources")
    print("2. Add Source")
    print("3. Remove Source")
    print("4. Back to Main Menu")
    sub_choice = input("Select an option: ")

    if sub_choice == '1':
        list_sources()
    elif sub_choice == '2':
        name = input("Enter source name: ")
        url = input("Enter source URL: ")
        add_source(name, url)
    elif sub_choice == '3':
        name = input("Enter source name to remove: ")
        remove_source(name)
    elif sub_choice == '4':
        return
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    while True:
        menu()
