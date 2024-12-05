class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.transactions = {}
        self.next_account_id = 1
    
    def create_account(self, timestamp):
        account_id = self.next_account_id
        self.accounts[account_id] = 0
        self.transactions[account_id] = 0
        self.next_account_id += 1
        return f"[{timestamp}] Account {account_id} created"
    
    def deposit(self, timestamp, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id] += amount
            self.transactions[account_id] += amount
            return f"[{timestamp}] Deposited {amount} to account {account_id}"
        return f"[{timestamp}] Account {account_id} does not exist"
    
    def withdraw(self, timestamp, account_id, amount):
        if account_id in self.accounts:
            if self.accounts[account_id] >= amount:
                self.accounts[account_id] -= amount
                self.transactions[account_id] += amount
                return f"[{timestamp}] Withdrew {amount} from account {account_id}"
            return f"[{timestamp}] Insufficient funds in account {account_id}"
        return f"[{timestamp}] Account {account_id} does not exist"
    
    def rank_accounts(self, timestamp):
        ranked_accounts = sorted(self.transactions.items(), key=lambda x: x[1], reverse=True)
        ranking_str = ", ".join([f"Account {acc_id} ({value})" for acc_id, value in ranked_accounts])
        return f"[{timestamp}] Ranked accounts: {ranking_str}"

    def process_queries(self, queries):
        results = []
        for query in queries:
            timestamp = query[0]
            operation = query[1]
            if operation == "create_account":
                result = self.create_account(timestamp)
            elif operation == "deposit":
                account_id, amount = query[2], query[3]
                result = self.deposit(timestamp, account_id, amount)
            elif operation == "withdraw":
                account_id, amount = query[2], query[3]
                result = self.withdraw(timestamp, account_id, amount)
            elif operation == "rank_accounts":
                result = self.rank_accounts(timestamp)
            results.append(result)
        return results

queries = [
    (1, "create_account"),
    (2, "create_account"),
    (3, "deposit", 1, 100),
    (4, "withdraw", 1, 50),
    (5, "withdraw", 2, 30),
    (6, "withdraw", 1, 60),
    (7, "deposit", 2, 200),
    (8, "rank_accounts")
]

bank_system = BankSystem()
results = bank_system.process_queries(queries)
print(results)
