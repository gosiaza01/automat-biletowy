from ticket import Ticket 

class Cart:
    def __init__(self):
        self.items = []

    def add_ticket(self, ticket: Ticket):
        self.items.append(ticket)
        print(f"Dodano do koszyka bilet {ticket}")

    def remove_ticket(self, index):
        if 0 <= index < len(self.items:)
            def self.items[index]

    def display_cart_value(self):
        return f"Wartość biletów w koszyku: {self.get_cart_value():5.2f} zł."
    
    def get_cart_value(self): 
        return sum(ticket.price for ticket in self.items)
    
    def display_cart(self):
        if not self.items:
            print("W koszyku nie ma jeszcze żadnych biletów.")
        else: 
            print("Zawartość koszyka")
            print()
            print("Lp.  I  Cena  I Bilet")
            for index, ticket in enumerate(self.items): 
                print(f"{index+1:3} I {ticket.price:7.2f} zł I Bilet {ticket.discount} {ticket.type} {ticket.validity}")
            print()
            print(self.display_cart_value())
            
    def clear_cart(self):
        self.items.clear()

