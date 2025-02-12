import db

while True:
    print("\n--- Welcome to the Banking Application ---")
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        while True:
            print("\n--- Banker Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Update Customers")
            print("4. View Customers")
            print("5. Delete Customer")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                username = input("Enter banker username: ")
                password = input("Enter banker password: ")

                conn = db.create_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO bankers (username, password) VALUES (%s, %s)", (username, password))
                conn.commit()
                cursor.close()
                conn.close()
                print("Banker registered successfully........")

            elif choice == '2':
                username = input("Enter banker username: ")
                password = input("Enter banker password: ")

                conn = db.create_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM bankers WHERE username=%s AND password=%s", (username, password))
                result = cursor.fetchone()
                cursor.close()
                conn.close()

                if result:
                    print("Login successful....")
                    while True:
                        print("\n--- Banker Menu ---")
                        print("1. Register")
                        print("2. Login")
                        print("3. Update Customers")
                        print("4. View Customers")
                        print("5. Delete Customer")
                        print("6. Exit")
                        choice = input("Choose an option: ")

                        if choice == '3':
                            conn = db.create_connection()
                            cursor = conn.cursor()
                            cursor.execute("SELECT * FROM customers")
                            customers = cursor.fetchall()
                            for customer in customers:
                                print(customer)

                            customer_id = int(input("Enter the customer ID to update: "))
                            new_balance = float(input("Enter new balance: "))
                            cursor.execute("UPDATE customers SET balance=%s WHERE id=%s", (new_balance, customer_id))
                            conn.commit()
                            cursor.close()
                            conn.close()
                            print("Customer updated successfully.")

                        elif choice == '4':
                            conn = db.create_connection()
                            cursor = conn.cursor()
                            cursor.execute("SELECT * FROM customers")
                            customers = cursor.fetchall()
                            for customer in customers:
                                print(customer)
                            cursor.close()
                            conn.close()

                        elif choice == '5':
                            customer_id = int(input("Enter the customer ID to delete: "))
                            conn = db.create_connection()
                            cursor = conn.cursor()
                            cursor.execute("DELETE FROM customers WHERE id=%s", (customer_id,))
                            conn.commit()
                            cursor.close()
                            conn.close()
                            print("Customer deleted successfully.")

                        elif choice == '6':
                            break
                        else:
                            print("Invalid choice! Please try again.....")

                else:
                    print("Invalid username or password.Please Enter Valid Password...")

            elif choice == '3':
                conn = db.create_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customers")
                customers = cursor.fetchall()
                for customer in customers:
                    print(customer)

                customer_id = int(input("Enter the customer ID to update: "))
                new_balance = float(input("Enter new balance: "))
                cursor.execute("UPDATE customers SET balance=%s WHERE id=%s", (new_balance, customer_id))
                conn.commit()
                cursor.close()
                conn.close()
                print("Customer updated successfully.")

            elif choice == '4':
                conn = db.create_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customers")
                customers = cursor.fetchall()
                for customer in customers:
                    print(customer)
                cursor.close()
                conn.close()

            elif choice == '5':
                customer_id = int(input("Enter the customer ID to delete: "))
                conn = db.create_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM customers WHERE id=%s", (customer_id,))
                conn.commit()
                cursor.close()
                conn.close()
                print("Customer deleted successfully.")

            elif choice == '6':
                break
            else:
                print("Invalid choice! Please try again.....")

    elif choice == '2':
        while True:
            print("\n--- Customer Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Withdraw Amount")
            print("4. Deposit Amount")
            print("5. View Balance")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                username = input("Enter customer username: ")
                password = input("Enter customer password: ")

                conn = db.create_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO customers (username, password) VALUES (%s, %s)", (username, password))
                conn.commit()
                cursor.close()
                conn.close()
                print("Customer registered successfully.")

            elif choice == '2':
                username = input("Enter customer username: ")
                password = input("Enter customer password: ")

                conn = db.create_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customers WHERE username=%s AND password=%s", (username, password))
                result = cursor.fetchone()
                cursor.close()
                conn.close()

                if result:
                    print("Login successful.")
                    while True:
                        print("\n--- Customer Menu ---")
                        print("1. Register")
                        print("2. Login")
                        print("3. Withdraw Amount")
                        print("4. Deposit Amount")
                        print("5. View Balance")
                        print("6. Exit")
                        choice = input("Choose an option: ")

                        if choice == '3':
                            username = input("Enter your username: ")
                            amount = float(input("Enter amount to withdraw: "))
                            
                            conn = db.create_connection()
                            cursor = conn.cursor()
                            cursor.execute("UPDATE customers SET balance = balance - %s WHERE username = %s AND balance >= %s", (amount, username, amount))
                            if cursor.rowcount > 0:
                                conn.commit()
                                print("Withdrawal successful.")
                            else:
                                print("Insufficient funds or user not found.")
                            cursor.close()
                            conn.close()

                        elif choice == '4':
                            username = input("Enter your username: ")
                            amount = float(input("Enter amount to deposit: "))
                            
                            conn = db.create_connection()
                            cursor = conn.cursor()
                            cursor.execute("UPDATE customers SET balance = balance + %s WHERE username = %s", (amount, username))
                            conn.commit()
                            cursor.close()
                            conn.close()
                            print("Deposit successful.")

                        elif choice == '5':
                            username = input("Enter your username: ")
                            
                            conn = db.create_connection()
                            cursor = conn.cursor()
                            cursor.execute("SELECT balance FROM customers WHERE username = %s", (username,))
                            result = cursor.fetchone()
                            cursor.close()
                            conn.close()

                            if result:
                                print(f"Your balance is: {result[0]}")
                            else:
                                print("User not found.")

                        elif choice == '6':
                            break
                        else:
                            print("Invalid choice! Please try again.")

                else:
                    print("Invalid username or password.")

            elif choice == '6':
                break
            else:
                print("Invalid choice! Please try again.")

    elif choice == '3':
        break
    else:
        print("Invalid choice! Please try again.")
