import pandas as pd
import os

FILE_PATH = "clients.xlsx"

def load_data():
    if os.path.exists(FILE_PATH):
        return pd.read_excel(FILE_PATH)
    else:
        return pd.DataFrame(columns=["Name", "Email", "Phone", "Status"])

def save_data(df):
    df.to_excel(FILE_PATH, index=False)
    print("Client list saved.")

def add_client():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    status = input("Status (e.g., Prospect, Client, Follow-up): ")
    return {"Name": name, "Email": email, "Phone": phone, "Status": status}

def list_clients(df):
    if df.empty:
        print("No clients found.")
    else:
        print("\nClient List:")
        print(df.sort_values(by="Name"))

def main():
    df = load_data()
    while True:
        print("\nMini CRM - Options:")
        print("1. Add client")
        print("2. List clients")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            client = add_client()
            df = pd.concat([df, pd.DataFrame([client])], ignore_index=True)
            save_data(df)
        elif choice == "2":
            list_clients(df)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
