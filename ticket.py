class Ticket:
    def __init__(self, discount, ticket_type, validity, price):
        self.discount = discount
        self.type = ticket_type
        self.validity = validity
        self.price = price

    def __repr__(self):
        return f"Ticket(discount='{self.discount}', type='{self.ticket_type}', validity='{self.validity}', price='{self.price})"
    def __str__(self):
        return f"{self.discount} {self.ticket_type} {self.validity} ${self.price: .2f}"