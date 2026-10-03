import json
import time


class Ticket:
    """Reprezentuje pojedynczy bilet."""

    def __init__(self, discount, ticket_type, validity, price):
        self.discount = discount
        self.ticket_type = ticket_type
        self.validity = validity
        self.price = price

    def __str__(self):
        return (
            f"Bilet {self.discount} "
            f"{self.ticket_type} "
            f"{self.validity} "
            f"- {self.price:.2f} zł"
        )


class Cart:
    """Reprezentuje koszyk z biletami."""

    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def clear(self):
        self.tickets.clear()

    def is_empty(self):
        return len(self.tickets) == 0

    def get_total(self):
        return sum(ticket.price for ticket in self.tickets)

    def show(self):
        if self.is_empty():
            print("W koszyku nie ma jeszcze żadnych biletów.")
            return

        print()
        print("Zawartość koszyka:")
        print()
        print("Lp. | Cena      | Bilet")

        for index, ticket in enumerate(self.tickets, start=1):
            print(
                f"{index:3} | "
                f"{ticket.price:7.2f} zł | "
                f"{ticket}"
            )

        print()
        print(f"Wartość biletów w koszyku: {self.get_total():.2f} zł")


class TicketMachine:
    """Główna klasa automatu biletowego."""

    PROMPT = "Twój wybór: "
    ERROR_MSG = "Niepoprawny wybór, spróbuj ponownie."

    def __init__(self, prices):
        self.prices = prices
        self.cart = Cart()
        self.running = True

    def run(self):
        """Uruchamia automat."""
        print("================================")
        print("       AUTOMAT BILETOWY")
        print("================================")

        while self.running:
            self.display_menu()

    def display_menu(self):
        """Wyświetla główne menu."""
        print()
        print("Wybierz jedną z opcji:")
        print("1 - dodaj bilet")
        print("2 - pokaż koszyk")
        print("3 - zapłać")
        print("4 - zakończ program")

        choice = input(self.PROMPT).strip()

        if not choice:
            print(self.ERROR_MSG)
            return

        match choice[0]:
            case "1":
                self.add_ticket()
            case "2":
                self.cart.show()
            case "3":
                self.register_payment()
            case "4":
                self.end_machine()
            case _:
                print(self.ERROR_MSG)

    def add_ticket(self):
        """Tworzy i dodaje bilet do koszyka."""
        discount = self.choose_discount()

        if discount is None:
            return

        ticket_type = self.choose_ticket_type()

        if ticket_type is None:
            return

        validity = self.choose_validity(ticket_type)

        if validity is None:
            return

        try:
            price = self.prices[discount][ticket_type][validity]
        except KeyError:
            print("Nie znaleziono ceny biletu w prices.json.")
            return

        ticket = Ticket(
            discount,
            ticket_type,
            validity,
            price
        )

        self.cart.add_ticket(ticket)

        print()
        print(
            f"Dodano do koszyka: {ticket}"
        )

    def choose_discount(self):
        """Wybiera rodzaj biletu: normalny lub ulgowy."""
        while True:
            print()
            print("Wybierz rodzaj biletu:")
            print("n - normalny")
            print("u - ulgowy")
            print("p - powrót")
            print("k - koniec")

            choice = input(self.PROMPT).strip().lower()

            if not choice:
                print(self.ERROR_MSG)
                continue

            match choice[0]:
                case "n":
                    return "normalny"

                case "u":
                    return "ulgowy"

                case "p":
                    return None

                case "k":
                    self.end_machine()
                    return None

                case _:
                    print(self.ERROR_MSG)

    def choose_ticket_type(self):
        """Wybiera typ biletu."""
        while True:
            print()
            print("Wybierz typ biletu:")
            print("o - okresowy")
            print("c - czasowy")
            print("j - jednorazowy")
            print("p - powrót")
            print("k - koniec")

            choice = input(self.PROMPT).strip().lower()

            if not choice:
                print(self.ERROR_MSG)
                continue

            match choice[0]:
                case "o":
                    return "okresowy"

                case "c":
                    return "czasowy"

                case "j":
                    return "jednorazowy"

                case "p":
                    return None

                case "k":
                    self.end_machine()
                    return None

                case _:
                    print(self.ERROR_MSG)

    def choose_validity(self, ticket_type):
        """Wybiera okres lub obszar ważności biletu."""

        if ticket_type == "okresowy":
            options = {
                "1": "półroczny",
                "2": "miesięczny",
                "3": "tygodniowy",
                "4": "jednodniowy"
            }

            message = (
                "Wybierz okres ważności biletu:\n"
                "1 - półroczny\n"
                "2 - miesięczny\n"
                "3 - tygodniowy\n"
                "4 - jednodniowy\n"
                "p - powrót\n"
                "k - koniec"
            )

        elif ticket_type == "czasowy":
            options = {
                "1": "60 - minutowy",
                "2": "30 - minutowy",
                "3": "10 - minutowy"
            }

            message = (
                "Wybierz okres ważności biletu:\n"
                "1 - 60 minut\n"
                "2 - 30 minut\n"
                "3 - 10 minut\n"
                "p - powrót\n"
                "k - koniec"
            )

        else:
            options = {
                "1": "miejski",
                "2": "aglomeracyjny"
            }

            message = (
                "Wybierz obszar ważności biletu:\n"
                "1 - miejski\n"
                "2 - aglomeracyjny\n"
                "p - powrót\n"
                "k - koniec"
            )

        while True:
            print()
            print(message)

            choice = input(self.PROMPT).strip().lower()

            if not choice:
                print(self.ERROR_MSG)
                continue

            if choice[0] in options:
                return options[choice[0]]

            if choice[0] == "p":
                return None

            if choice[0] == "k":
                self.end_machine()
                return None

            print(self.ERROR_MSG)

    def register_payment(self):
        """Obsługuje wybór metody płatności."""
        if self.cart.is_empty():
            print("W koszyku nie ma jeszcze żadnych biletów.")
            return

        while True:
            print()
            print(f"Do zapłaty: {self.cart.get_total():.2f} zł")
            print()
            print("Wybierz metodę płatności:")
            print("c - karta")
            print("g - gotówka")
            print("b - BLIK")
            print("p - powrót")
            print("k - koniec")

            choice = input(self.PROMPT).strip().lower()

            if not choice:
                print(self.ERROR_MSG)
                continue

            match choice[0]:
                case "c":
                    if self.pay_by_card():
                        self.finish_payment()
                        return

                case "g":
                    if self.pay_by_cash():
                        self.finish_payment()
                        return

                case "b":
                    if self.pay_by_blik():
                        self.finish_payment()
                        return

                case "p":
                    return

                case "k":
                    self.end_machine()
                    return

                case _:
                    print(self.ERROR_MSG)

    def pay_by_card(self):
        """Obsługuje płatność kartą."""
        print()
        input("Proszę zbliżyć kartę i nacisnąć ENTER...")

        print("Płatność kartą zakończona pomyślnie.")
        return True

    def pay_by_cash(self):
        """Obsługuje płatność gotówką."""
        to_pay = self.cart.get_total()
        paid = 0.0

        print()
        print(f"Do zapłaty: {to_pay:.2f} zł")

        while paid < to_pay:
            print(f"Pozostało: {to_pay - paid:.2f} zł")

            try:
                money = float(
                    input("Wrzuć pieniądze: ").replace(",", ".")
                )

                if money <= 0:
                    print("Kwota musi być większa od 0.")
                    continue

                paid += money

            except ValueError:
                print("Niepoprawna kwota, spróbuj ponownie.")

        if paid > to_pay:
            print(f"Reszta: {paid - to_pay:.2f} zł")

        print("Płatność gotówką zakończona pomyślnie.")
        return True

    def pay_by_blik(self):
        """Obsługuje płatność BLIK."""
        while True:
            blik = input("Podaj 6-cyfrowy kod BLIK: ").strip()

            if len(blik) == 6 and blik.isdigit():
                print("Płatność BLIK zakończona pomyślnie.")
                return True

            print(
                "Niepoprawny kod BLIK, spróbuj ponownie."
            )

    def finish_payment(self):
        """Kończy płatność i drukuje bilety."""
        print()
        print("Drukowanie biletów...")

        time.sleep(len(self.cart.tickets))

        print("Bilety zostały wydrukowane.")
        print(
            "Dziękujemy za skorzystanie "
            "z automatu biletowego!"
        )

        self.cart.clear()

    def end_machine(self):
        """Kończy działanie automatu."""
        while True:
            choice = input(
                "Czy na pewno chcesz porzucić koszyk?\n"
                "t - tak\n"
                "n - nie\n"
                f"{self.PROMPT}"
            ).strip().lower()

            if not choice:
                print(self.ERROR_MSG)
                continue

            if choice[0] == "t":
                print(
                    "Dziękujemy za skorzystanie "
                    "z automatu."
                )
                self.running = False
                return

            if choice[0] == "n":
                return

            print(self.ERROR_MSG)


def load_prices():
    """Wczytuje ceny z pliku prices.json."""
    try:
        with open(
            "prices.json",
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except FileNotFoundError:
        print(
            "Błąd: nie znaleziono pliku prices.json."
        )
        return None

    except json.JSONDecodeError:
        print(
            "Błąd: plik prices.json ma niepoprawny format."
        )
        return None


def main():
    prices = load_prices()

    if prices is None:
        return

    machine = TicketMachine(prices)
    machine.run()


if __name__ == "__main__":
    main()
