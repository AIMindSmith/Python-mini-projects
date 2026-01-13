from abc import ABC, abstractmethod
from typing import Dict, Any

"""Product Pricing Engine using SOLID principles."""



class Product:
    """Represents a product with pricing information."""

    def __init__(self, name: str, base_price: float, discount: float = 0.0, tax: float = 0.0):
        """Initialize product with validation."""
        self._validate(base_price, discount, tax)
        self.name = name
        self.base_price = base_price
        self.discount = discount
        self.tax = tax

    @staticmethod
    def _validate(base_price: float, discount: float, tax: float) -> None:
        """Validate pricing parameters."""
        if base_price < 0:
            raise ValueError("Base price cannot be negative")
        if not (0 <= discount <= 100):
            raise ValueError("Discount must be between 0 and 100")
        if not (0 <= tax <= 100):
            raise ValueError("Tax must be between 0 and 100")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        """Create product from dictionary."""
        return cls(
            name=data["name"],
            base_price=data["base_price"],
            discount=data.get("discount", 0.0),
            tax=data.get("tax", 0.0)
        )

    @classmethod
    def from_string(cls, text: str) -> "Product":
        """Create product from comma-separated string."""
        name, base_price, discount, tax = text.split(",")
        return cls(
            name=name.strip(),
            base_price=float(base_price),
            discount=float(discount),
            tax=float(tax)
        )


class PriceCalculator(ABC):
    """Abstract base for price calculation strategies."""

    @abstractmethod
    def calculate(self, product: Product) -> float:
        """Calculate price based on strategy."""
        pass


class StandardPriceCalculator(PriceCalculator):
    """Calculates final price with discount and tax."""

    def calculate(self, product: Product) -> float:
        """Apply discount then tax."""
        price = product.base_price
        price -= price * (product.discount / 100)
        price += price * (product.tax / 100)
        return round(price, 2)


class PricingEngine:
    """Manages pricing calculations (Dependency Injection)."""

    def __init__(self, calculator: PriceCalculator):
        self.calculator = calculator

    def final_price(self, product: Product) -> float:
        """Get final price using injected calculator."""
        return self.calculator.calculate(product)


# Example usage
calculator = StandardPriceCalculator()
engine = PricingEngine(calculator)

p1 = Product("Laptop", 50000, discount=10, tax=18)
print(f"Laptop final price: {engine.final_price(p1)}")

p2 = Product.from_dict({"name": "Phone", "base_price": 20000, "discount": 5, "tax": 18})
print(f"Phone final price: {engine.final_price(p2)}")

p3 = Product.from_string("Headphones,3000,20,18")
print(f"Headphones final price: {engine.final_price(p3)}")
