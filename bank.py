%%writefile bank.py
import json
import os
from datetime import datetime

class Account:
    def __init__(self, acc_id, name, balance=0.0):
        self.id = acc_id
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
        self.balance += amount
        record = f"{datetime.now()} | Deposited ₹{amount:.2f} | New Balance: ₹{self.balance:.2f}"
        self.transactions.append(record)
        print("✅ Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("❌ Insufficient balance.")
            return
        self.balance -= amount
        record = f"{datetime.now()} | Withdrew ₹{amount:.2f} | New Balance: ₹{self.balance:.2f}"
        self.transactions.append(record)
        print("✅ Withdrawal successful.")

    def get_balance(self):
        print(f"💰 Current Balance: ₹{self.balance:.2f}")

    def get_history(self):
        if not self.transactions:
            print("📄 No transactions yet.")
        else:
            print("\n🧾 Transaction History:")
            for t in self.transactions:
                print("  -", t)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }

    @staticmethod
    def from_dict(data):
        acc = Account(data["id"], data["name"], data["balance"])
        acc.transactions = data.get("transactions", [])
        return acc


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        name = input("Enter account holder name: ")
        acc_id = len(self.accounts) + 1
        account = Account(acc_id, name)
        self.accounts.append(account)
        print(f"✅ Account created successfully! Account ID: {acc_id}")

    def find_account_by_id(self, acc_id):
        for acc in self.accounts:
            if acc.id == acc_id:
                return acc
        print("❌ Account not found.")
        return None

    def deposit_to_account(self):
        acc_id = int(input("Enter account ID: "))
        acc = self.find_account_by_id(acc_id)
        if acc:
            amount = float(input("Enter deposit amount: "))
            acc.deposit(amount)

    def withdraw_from_account(self):
        acc_id = int(input("Enter account ID: "))
        acc = self.find_account_by_id(acc_id)
        if acc:
            amount = float(input("Enter withdrawal amount: "))
            acc.withdraw(amount)

    def show_account_details(self):
        acc_id = int(input("Enter account ID: "))
        acc = self.find_account_by_id(acc_id)
        if acc:
            print(f"\n👤 Account ID: {acc.id}")
            print(f"Name: {acc.name}")
            acc.get_balance()
            acc.get_history()

    def save_to_file(self, filename="bank.json"):
        data = [acc.to_dict() for acc in self.accounts]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("💾 Data saved successfully to bank.json")

    def load_from_file(self, filename="bank.json"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                self.accounts = [Account.from_dict(d) for d in data]
            print("📂 Data loaded successfully.")
        else:
            print("⚠️ No existing data file found.")
