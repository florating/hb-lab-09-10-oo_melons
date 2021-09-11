"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    
    tax = 0
    order_type = ''
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if 'christmas' in self.species.lower():
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if 'international' in self.order_type.lower() and self.qty < 10:
            total += 3
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0
    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)

    def mark_inspection(self, passed):
        """Takes a Boolean input (passed) and updates whether or not the melon has passed inspection."""
        self.passed_inspection = passed
        
