

from typing import Dict


class Deposit:
    def __init__(self, amount: float, years: int, annual_rate: float = 0.10):
        self.amount = amount
        self.years = years
        self.annual_rate = annual_rate
        self.monthly_rate = annual_rate / 12
        self.active = True

    def calculate_final_amount(self) -> float:
        n_months = self.years * 12
        balance = self.amount
        for _ in range(n_months):
            balance += balance * self.monthly_rate
        return round(balance, 2)


class Bank:
    def __init__(self):
        self.clients: Dict[str, str] = {}
        self.deposits: Dict[str, Deposit] = {}

    def register_client(self, client_id: str, name: str):
        if client_id in self.clients:
            raise ValueError(f"Client {client_id} already registered")
        self.clients[client_id] = name

    def open_deposit_account(self, client_id: str, start_balance: float, years: int):
        if client_id not in self.clients:
            raise ValueError(f"Client {client_id} not registered")
        self.deposits[client_id] = Deposit(start_balance, years)

    def calc_interest_rate(self, client_id: str) -> float:
        if client_id not in self.deposits:
            raise ValueError(f"No deposit found for client {client_id}")
        return self.deposits[client_id].calculate_final_amount()

    def close_deposit(self, client_id: str):
        if client_id not in self.deposits:
            raise ValueError(f"No deposit found for client {client_id}")
        self.deposits[client_id].active = False
        del self.deposits[client_id]


if __name__ == "__main__":
    main_client_id = "0000001"
    bank = Bank()
    bank.register_client(client_id=main_client_id, name="Siarhei")
    bank.open_deposit_account(client_id=main_client_id, start_balance=1000, years=1)
    final_amount = bank.calc_interest_rate(client_id=main_client_id)
    print(final_amount)
    assert final_amount == 1104.71, "Interest calculation error"
    bank.close_deposit(client_id=main_client_id)
