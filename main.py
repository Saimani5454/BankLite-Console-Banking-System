#main.py
from bank import Bank

def main():
    bank = Bank()
    bank.load_from_file()

    while True:
        print("\n===== 🏦 BankLite Console Menu =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance & History")
        print("5. Save Data")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit_to_account()
        elif choice == "3":
            bank.withdraw_from_account()
        elif choice == "4":
            bank.show_account_details()
        elif choice == "5":
            bank.save_to_file()
        elif choice == "6":
            bank.save_to_file()
            print("👋 Exiting BankLite. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
