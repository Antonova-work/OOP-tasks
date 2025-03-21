#3

'''
Создайте класс "Банк" с атрибутами название и список счетов. 
Каждый счет представлен классом
"Счет" с атрибутами номер и баланс. Напишите методы для добавления с
чета в банк, удаления счета из
банка и вычисления общего баланса всех счетов в банке. 
Используйте магический метод `__len__` для
определения количества счетов в банке.
'''

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Счет №{self.account_number}: Баланс = {self.balance}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Счет №{account.account_number} добавлен в банк '{self.name}'.")

    def remove_account(self, account):
        if account in self.accounts:
            self.accounts.remove(account)
            print(f"Счет №{account.account_number} удален из банка '{self.name}'.")
        else:
            print(f"Счета №{account.account_number} нет в банке '{self.name}'.")

    def calculate_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.balance
        return total_balance

    def __len__(self):
        return len(self.accounts)

    def display_accounts(self):
      if not self.accounts:
        print(f"В банке '{self.name}' нет счетов.")
      else:
        print(f"Счета в банке '{self.name}':")
        for account in self.accounts:
          print(f"- {account}")

account1 = Account("12345", 1000)
account2 = Account("67890", 500)
account3 = Account("11223", 2000)

bank = Bank("ФПИ-Банк")

bank.add_account(account1)
bank.add_account(account2)
bank.add_account(account3)

bank.display_accounts()

print(f"Количество счетов в банке: {len(bank)}")
print(f"Общий баланс всех счетов: {bank.calculate_total_balance()}")

bank.remove_account(account2)
bank.display_accounts()

print(f"Количество счетов в банке: {len(bank)}")
print(f"Общий баланс всех счетов: {bank.calculate_total_balance()}")

account4 = Account("55555", 100)
bank.remove_account(account4)