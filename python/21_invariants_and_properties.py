# Technique: Encapsulation with Invariants + @property
# Use When:
# - Objects protect their own correctness (invariants)
# - Callers use a simple API; representation can change safely
# - Properties expose computed values without leaking internal state

from dataclasses import dataclass


@dataclass
class BankAccount:
    _balance_cents: int

    def __post_init__(self) -> None:
        if self._balance_cents < 0:
            raise ValueError("balance must be >= 0")

    @property
    def balance(self) -> float:
        return self._balance_cents / 100

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be > 0")
        self._balance_cents += int(round(amount * 100))

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdrawal must be > 0")
        cents = int(round(amount * 100))
        if cents > self._balance_cents:
            raise ValueError("insufficient funds")
        self._balance_cents -= cents


if __name__ == "__main__":
    acct = BankAccount(0)
    acct.deposit(10.25)
    acct.withdraw(3.00)
    print("balance:", acct.balance)
