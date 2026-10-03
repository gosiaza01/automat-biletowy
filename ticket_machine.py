# 1.	Uruchom program.
# 2.	Wczytaj dane z pliku prices.json.
import json
import time

# Stałe
PROMPT = "Twój wybór: "
ERROR_MSG = "Niepoprawny wybór, spróbuj ponownie."


def display_menu(cart, prices):
    """Wyświetla główne menu."""
    while True:
        print()
        print("Wybierz jedną z opcji:")
        print("1 - dodaj bilet")
        print("2 - pokaż koszyk")
        print("3 - zapłać")
        print("4 - zakończ program")

        choice = input(PROMPT).strip()

        if not choice:
            print(ERROR_MSG)
            continue

        match choice[0]:
            case "1":
                add_ticket(cart, prices)
            case "2":
                display_cart(cart)
            case "3":
                register_payment(cart, prices)
            case "4":
                end_machine(cart, prices)
            case _:
                print(ERROR_MSG)


def display_cart(cart):
    """Wyświetla zawartość koszyka."""
    print()

    if not cart:
        print("W koszyku nie ma jeszcze żadnych biletów.")
        return

    print("Zawartość koszyka:")
    print()
    print("Lp. | Cena      | Bilet")

    for index, ticket in enumerate(cart, start=1):
        print(
            f"{index:3} | "
            f"{ticket['price']:7.2f} zł | "
            f"Bilet {ticket['discount']} "
            f"{ticket['type']} "
            f"{ticket['validity']}"
        )

    print()
    print(get_cart_value(cart))


def get_cart_value(cart):
    """Zwraca wartość wszystkich biletów w koszyku."""
    total = sum(ticket["price"] for ticket in cart)
    return f"Wartość biletów w koszyku: {total:.2f} zł."


def register_payment(cart, prices):
    """Obsługuje wybór metody płatności."""
    if not cart:
        print("W koszyku nie ma jeszcze żadnych biletów.")
        return

    while True:
        print()
        print(get_cart_value(cart))
        print()
        print("Wybierz metodę płatności:")
        print("c - karta")
        print("g - gotówka")
        print("b - BLIK")
        print("p - powrót")
        print("k - koniec")

        choice = input(PROMPT).strip().lower()

        if not choice:
            print(ERROR_MSG)
            continue

        match choice[0]:
            case "c":
                if pay_by_card():
                    finish_payment(cart)
                    return

            case "g":
                if pay_by_cash(cart):
                    finish_payment(cart)
                    return

            case "b":
                if pay_by_blik():
                    finish_payment(cart)
                    return

            case "p":
                return

            case "k":
                end_machine(cart, prices)
                return

            case _:
                print(ERROR_MSG)


def pay_by_card():
    """Obsługuje płatność kartą."""
    print()
    input("Proszę zbliżyć kartę i nacisnąć ENTER...")

    print("Płatność kartą zakończona pomyślnie.")
    return True


def pay_by_cash(cart):
    """Obsługuje płatność gotówką."""
    to_pay = sum(ticket["price"] for ticket in cart)
    paid = 0.0

    print()
    print(f"Do zapłaty: {to_pay:.2f} zł")

    while paid < to_pay:
        print(f"Pozostało do zapłaty: {to_pay - paid:.2f} zł")

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


def pay_by_blik():
    """Obsługuje płatność BLIK."""
    while True:
        blik = input("Podaj 6-cyfrowy kod BLIK: ").strip()

        if len(blik) == 6 and blik.isdigit():
            print("Płatność BLIK zakończona pomyślnie.")
            return True

        print("Niepoprawny kod BLIK, spróbuj ponownie.")


def finish_payment(cart):
    """Kończy proces płatności i symuluje drukowanie biletów."""
    print()
    print("Drukowanie biletów...")

    time.sleep(len(cart))

    print("Bilety zostały wydrukowane.")
    print("Dziękujemy za skorzystanie z automatu biletowego!")

    cart.clear()


def end_machine(cart, prices):
    """Kończy działanie programu po potwierdzeniu użytkownika."""
    while True:
        choice = input(
            "Czy na pewno chcesz porzucić koszyk?\n"
            "t - tak\n"
            "n - nie\n"
            f"{PROMPT}"
        ).strip().lower()

        if not choice:
            print(ERROR_MSG)
            continue

        if choice[0] == "t":
            print("Dziękujemy za skorzystanie z automatu.")
            raise SystemExit

        if choice[0] == "n":
            return

        print(ERROR_MSG)


def add_ticket(cart, prices):
    """Dodaje nowy bilet do koszyka."""
    ticket = {}

    # Wybór rodzaju biletu
    while True:
        print()
        print("Wybierz rodzaj biletu:")
        print("n - normalny")
        print("u - ulgowy")
        print("p - powrót")
        print("k - koniec")

        choice = input(PROMPT).strip().lower()

        if not choice:
            print(ERROR_MSG)
            continue

        match choice[0]:
            case "n":
                ticket["discount"] = "normalny"
                break

            case "u":
                ticket["discount"] = "ulgowy"
                break

            case "p":
                return

            case "k":
                end_machine(cart, prices)
                return

            case _:
                print(ERROR_MSG)

    # Wybór typu biletu
    while True:
        print()
        print("Wybierz typ biletu:")
        print("o - okresowy")
        print("c - czasowy")
        print("j - jednorazowy")
        print("p - powrót")
        print("k - koniec")

        choice = input(PROMPT).strip().lower()

        if not choice:
            print(ERROR_MSG)
            continue

        match choice[0]:
            case "o":
                ticket["type"] = "okresowy"

                validity = choose_validity_from_map(
                    cart,
                    prices,
                    (
                        "Wybierz okres ważności biletu:\n"
                        "1 - półroczny\n"
                        "2 - miesięczny\n"
                        "3 - tygodniowy\n"
                        "4 - jednodniowy\n"
                        "p - powrót\n"
                        "k - koniec"
                    ),
                    {
                        "1": "półroczny",
                        "2": "miesięczny",
                        "3": "tygodniowy",
                        "4": "jednodniowy",
                    },
                )

                if validity is None:
                    return

                ticket["validity"] = validity
                break

            case "c":
                ticket["type"] = "czasowy"

                validity = choose_validity_from_map(
                    cart,
                    prices,
                    (
                        "Wybierz okres ważności biletu:\n"
                        "1 - 60 minut\n"
                        "2 - 30 minut\n"
                        "3 - 10 minut\n"
                        "p - powrót\n"
                        "k - koniec"
                    ),
                    {
                        "1": "60 - minutowy",
                        "2": "30 - minutowy",
                        "3": "10 - minutowy",
                    },
                )

                if validity is None:
                    return

                ticket["validity"] = validity
                break

            case "j":
                ticket["type"] = "jednorazowy"

                validity = choose_validity_from_map(
                    cart,
                    prices,
                    (
                        "Wybierz obszar ważności biletu:\n"
                        "1 - miejski\n"
                        "2 - aglomeracyjny\n"
                        "p - powrót\n"
                        "k - koniec"
                    ),
                    {
                        "1": "miejski",
                        "2": "aglomeracyjny",
                    },
                )

                if validity is None:
                    return

                ticket["validity"] = validity
                break

            case "p":
                return

            case "k":
                end_machine(cart, prices)
                return

            case _:
                print(ERROR_MSG)

    # Pobranie ceny z prices.json
    try:
        ticket["price"] = prices[
            ticket["discount"]
        ][
            ticket["type"]
        ][
            ticket["validity"]
        ]

    except KeyError:
        print("Nie znaleziono ceny tego biletu w prices.json.")
        return

    cart.append(ticket)

    print()
    print(
        f"Dodano do koszyka bilet "
        f"{ticket['discount']} "
        f"{ticket['type']} "
        f"{ticket['validity']} "
        f"za cenę {ticket['price']:.2f} zł."
    )


def choose_validity_from_map(
    cart,
    prices,
    prompt_text,
    options_map,
):
    """Pozwala wybrać okres/obszar ważności biletu."""
    while True:
        print()
        print(prompt_text)

        choice = input(PROMPT).strip().lower()

        if not choice:
            print(ERROR_MSG)
            continue

        if choice[0] in options_map:
            return options_map[choice[0]]

        if choice[0] == "p":
            return None

        if choice[0] == "k":
            end_machine(cart, prices)
            return None

        print(ERROR_MSG)


def main():
    """Główna funkcja programu."""
    try:
        with open("prices.json", "r", encoding="utf-8") as file:
            prices = json.load(file)

    except FileNotFoundError:
        print("Błąd: nie znaleziono pliku prices.json.")
        print("Upewnij się, że prices.json znajduje się w folderze projektu.")
        return

    except json.JSONDecodeError:
        print("Błąd: plik prices.json ma niepoprawny format.")
        return

    cart = []

    print("================================")
    print("     AUTOMAT BILETOWY")
    print("================================")

    display_menu(cart, prices)


if __name__ == "__main__":
    main()
