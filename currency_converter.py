
from typing import Dict, Tuple


class CurrencyConverter:
    def __init__(self):
        self.rates_to_byn: Dict[str, float] = {
            "USD": 3.269,
            "EUR": 7.04,
            "BYN": 1.0,
        }

    def exchange_currency(
        self,
        from_currency: str,
        amount: float,
        to_currency: str = "BYN"
    ) -> Tuple[float, str]:
        if from_currency not in self.rates_to_byn:
            raise ValueError(f"Unsupported currency: {from_currency}")

        if to_currency not in self.rates_to_byn:
            raise ValueError(f"Unsupported currency: {to_currency}")

        amount_in_byn = amount * self.rates_to_byn[from_currency]

        if to_currency == "BYN":
            return round(amount_in_byn, 2), "BYN"

        converted_amount = amount_in_byn / self.rates_to_byn[to_currency]

        return round(converted_amount, 2), to_currency


class Person:
    def __init__(self, currency: str, amount: float):
        self.currency = currency
        self.amount = amount


if __name__ == "__main__":
    converter = CurrencyConverter()

    vasya = Person('USD', 10)
    petya = Person('EUR', 5)

    assert converter.exchange_currency(vasya.currency, vasya.amount) == (32.69, "BYN")
    assert converter.exchange_currency(petya.currency, petya.amount) == (35.20, "BYN")

    assert converter.exchange_currency(vasya.currency, vasya.amount, 'EUR') == (9.29, "EUR")
    assert converter.exchange_currency(petya.currency, petya.amount, 'USD') == (10.76, "USD")

    print("All tests passed!")
