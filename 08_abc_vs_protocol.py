"""
Technique: ABC vs Protocol (Nominal vs Structural Interfaces)

Why this is professional:
- You choose interface style based on control and flexibility needs.
- ABC enforces explicit inheritance (nominal typing).
- Protocol enables duck-typed compatibility with static checks (structural typing).

Pattern:
1) Use ABC when you own implementations and want explicit contracts.
2) Use Protocol when you want loose coupling across independent implementations.
3) Keep method signatures small and behavior-focused.
"""

from abc import ABC, abstractmethod
from typing import Protocol


# ---------- ABC example (explicit inheritance required) ----------
class PaymentGatewayABC(ABC):
    @abstractmethod
    def charge(self, amount: float) -> str:
        pass


class StripeGateway(PaymentGatewayABC):
    def charge(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("amount must be > 0")
        return f"stripe_charge_id_{int(amount * 100)}"


def checkout_with_abc(gateway: PaymentGatewayABC, amount: float) -> str:
    return gateway.charge(amount)


# ---------- Protocol example (inheritance optional) ----------
class PaymentGatewayProtocol(Protocol):
    def charge(self, amount: float) -> str:
        ...


class MockGateway:
    # No inheritance from Protocol; still compatible by signature.
    def charge(self, amount: float) -> str:
        if amount <= 0:
            raise ValueError("amount must be > 0")
        return f"mock_charge_id_{int(amount * 100)}"


def checkout_with_protocol(gateway: PaymentGatewayProtocol, amount: float) -> str:
    return gateway.charge(amount)


if __name__ == "__main__":
    stripe = StripeGateway()
    print("ABC checkout:", checkout_with_abc(stripe, 19.99))

    mock = MockGateway()
    print("Protocol checkout:", checkout_with_protocol(mock, 19.99))
