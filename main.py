# 1.	Uruchom program.
# 2.	Wczytaj dane z pliku prices.json.
import json 
import time

#stałe
PROMPT = "Twój wybór"
ERROR_MSG = "Niepoprawny wybór spróbuj ponownie ."

def display_menu(cart, prices):
    print()
    print("Wybierz jedną z opcji:\n1 - dodaj bilet\n2 - pokaż koszyk\n3 - zapłać\n4 - zakończ program")
    
    option = input(PROMPT)[0]

    match option: 
        case "1":
            add_ticket(cart, prices)\
        case "2":
            display_cart(cart)
        case "3":
            register_payment(cart, prices)
        case "4":
            end_machine(cart, prices)
        case _:
            print(ERROR_MSG)
        
def display_cart(cart):
    if not cart:
        print("W koszyku nie ma jeszcze żadnych biletów.")
    else:
        print("Zawartość koszyka")
        print()
        print("Lp. I   Cena   I  Bilet")
        for index, ticket in enumerate(cart):
            print(f"{index:3}  I  {ticket['price']:7.2f} zł  I  Bilet {ticket['discount']} {ticket['type']} {ticket['validity']}")
        print()
        print(get_cart_value(cart))

def register_payment(cart, prices):
    if not cart: 
        print("W koszyku nie ma jeszcze żadnych biletów.")
    else: 
        print(get_cart_value(cart))
        while True:
            print("Wybierz metodę płatności:\nc - karta\ng - gotówka\nb - blik\np - powrót\nk - koniec")
            payment_method = input(PROMPT)[0]
            match payment_method:
                case "c":
                    pay_by_card()
                    break
                case "b":
                    pay_by_blik(cart, prices)
                    break 
                case "g":
                    pay_by_cash(cart)
                    break
                case "p":
                    display_menu(cart, prices)
                case "k"

def pay_by_card():
    input("Proszę zbliżyć kartę ...")

def pay_by_cash(cart):
    to_pay = sum(ticket["price"] for ticket in cart)
    paid = 0
    while paid < to_pay:
        print(f"Kwota do zapłaty: {(to_pay - paid): 5.2} zł.")
        paid += float(input("Wrzuć pieniądze: "))
        if paid > to_pay: 
            print(f"Reszta: {(paid - to_pay):5.2} zł.")
def pay_by_blik(cart,prices):
    blik = input("Podaj kod BLIK: ")
    if len(blik) != 6 or not blik.isdigit():
        print("Płatność nie powiodła się, spróbuj ponownie")
        register_payment(cart, prices)
def get_cart_value(cart):
    return f"Wartość biletów w koszyku: {sum(ticket['price'] for ticket in cart):5.2f} zł."
def end_machine(cart, prices):
    choice = input("Czy na pewno chcesz porzucić koszyk (t - tak)? ")[0]
    if  choice == "t":
        exit()
    else: display_menu(cart, prices)

def add_ticket(cart, prices):
    ticket = {}
    def choose_discount():
        while True: 
            print("Wybierz typ biletu:\nn - normalny\nu - ulgowqy\np - powrót\nk - koniec") 
            ch = input(PROMPT)[0]
            if ch == "n":
                ticket["discount"] = "normalny"
                return 
            elif ch == "u":
                ticket["discount"] = "ulgowy"
                return 
            elif ch == "p":
                display_menu(cart, prices)
                return 
            elif ch == "k":
                end_machine(cart, prices)
            else: 
                print(ERROR_MSG)
    def choose_validity_from_map(prompt_text, options_map):
        while True:
            print(prompt_text)
            ch = input(PROMPT)[0]
            if ch in options_map:
                ticket["validity"] = options_map[ch]
                return
            elif ch == "p": 
                display_menu(cart, prices)
                return 
            elif ch == "k":
                end_machine(cart, prices)
            else: 
                print(ERROR_MSG)
    def choose_type():
        while True: 
            print("Wybierz typ biletu:\no - okresowy\nc - czasowy\nj - jednorazowy\np - powrót\nk - koniec")") 
            ch = input(PROMPT)[0]

            if ch == "o": 
                ticket["type"] = "okresowy"
                choose_validity_from_map(
                    "Wybierz okres ważności biletu:\n1 - półroczny\n2 - miesięczny\n3 0- tygodniowy\n4 - jednodniowy\np - powrót\nk - koniec"
                    {"1": "półroczny", "2": "miesięczny, "3": "tygodniowy", "4": "jednodniowy"},
                )
                return 
                4x To 

    choose_discount()
    choose_type()

    print(ticket["discount"], ticket["type"], ticket["validity"])
    ticket["price"] = prices[ticket["discount"]][ticket["type"]][ticket["validity"]]
    cart.append(ticket)
    print(f"Dodano do koszyka bilet {ticket['discount']} {ticket['type']} {ticket['validity']} za cenę {ticket['price']}")

def main():
    with open("./prices.json", "r", encoding="UTF-8") as jf:
        prices = json.load(jf)

    cart = []
    while True: 
        display_menu(cart, prices)
if __name__ == "__main__": 
    main()

   









    match option:
        case "1": 
            ticket = {}
    # 8.	Wyświetl typ biletu:
            while True: 
                print("Wybierz typ biletu:\nn - normalny\nu - ulgowy")

    # Pobierz jeden znak
                ticket1 = input(PROMPT)[0]

                if ticket1 == "n":
                    ticket["discount"] = "normalny"
                    break 
                elif ticket1 == "u":
                    ticket["discount"] = "ulgowy"
                    break 
                elif ticket1 == "p": 
                    break
                elif ticket1 == "k":
                    end_machine()
                else:
                    print(ERROR_MSG)
            if not ticket:
                continue 

            cont = True
            while True: 
                print("Wybierz typ biletu:\no - okresowy\nc - czasowy\nj - jednorazowy\np - powrót\nk - koniec")
    
                ticket2 = input(PROMPT)[0]

                if ticket2 == "o":
                    ticket["type"] = "okresowy"
                    while True: 

                        print("Wybierz okres ważności biletu:\n1 - półroczny\n2 - miesięczny\n3 - tygodniowy\n4 - jednodniowy\np - powrót\nk - koniec")

                        ticket3 = input(PROMPT)[0]
                        match ticket3: 
                            case "1": 
                                ticket["validity"] = "półroczny"
                                break 
                            case "2": 
                                ticket["validity"] = "miesięczny"
                                break
                            case "3": 
                                ticket["validity"] = "tygodniowy"
                                break 
                            case "4": 
                                ticket["validity"] = "jednodniowy"
                                break 
                            case "p":
                                cont = False
                                break
                            case "k": 
                                end_machine()
                            case _: 
                                print(ERROR_MSG)
                    if not cont: 
                        break
                    break 

                elif ticket2 =="c":
                    ticket["type"] = "czasowy"
                    while True: 
                        print("Wybierz okres ważności biletu:\n1 - 60 minut\n2 - 30 minut\n3 - 10 minut\np - powrót\nk - koniec")
                        ticket3 = input(PROMPT)[0]
                        match ticket3:
                            case "1": 
                                ticket["validity"] = "60 - minutowy"
                                break
                            case "2": 
                                ticket["validity"] = "30 - minutowy"
                                break
                            case "3": 
                                ticket["validity"] = "10 - minutowy"
                                break
                            case "p": 
                                cont = False
                                break
                            case "k":
                                end_machine()
                            case _: 
                                print(ERROR_MSG)
                    if not cont:
                        break
                    break
                elif ticket2 =="j":
                    ticket["type"] = "jednorazowy"
                    while True: 
                        print("Wybierz okres ważności biletu:\n1 - miejski\n2 - aglomeracyjny\np - powrót\nk - koniec")
                        ticket3 = input(PROMPT)[0]
                        match ticket3:
                            case "1": 
                                ticket["validity"] = "miejski"
                                break 
                            case "2": 
                                ticket["validity"] = "aglomeracyjny"
                                break
                            case "p": 
                                cont = False 
                                break 
                            case "k":
                                end_machine()
                            case _: 
                                print(ERROR_MSG)
                    if not cont: 
                        break
                    break
                elif ticket2 == "p":
                    cont = False 
                    break 
                elif ticket2 == "k":
                    end_machine()
                else: 
                    print(ERROR_MSG)
            if not cont: 
                continue 

            ticket["price"] = prices[ticket["discount"]][ticket["type"]][ticket["validity"]]
            cart.append(ticket)
            print(f"Dodano do koszyka bilet {ticket['discount']} {ticket['type']} {ticket['validity']} za cenę {ticket['price']}")

        case "2":
            if not cart: 
                print("W koszyku nie ma jeszcze żadnych biletów.")
            else: 
                print(cart)
                print(f"Wartość biletów w koszyku: {sum(ticket["price"] for ticket in cart)}")
        case "3": 
            if not cart: 
                print("W koszyku nie ma jeszcze żadnych biletów.")
            else: 
                print(f"Do zapłaty: {sum(ticket["price"] for ticket in cart):5.2} zł,")
            while True: 
                print("Wybierz metodę płatności:\nk - karta\ng - gotówka\nb-blik")    
                payment_method = input(PROMPT)[0]
                match payment_method:
                    case "k": input("Proszę zbliżyć kartę ...")
                    case "b": 
                        blik = input("Podaj kod BLIK: ")
                        if len(blik) !=6: 
                            print("Płatność nie powiodła się, spróbuj ponownie")
                    case "g": 
                        to_pay = sum(ticket["price"] for ticket in cart)
                        paid = 0 
                        while paid < to_pay: 
                            paid += float(input("Wrzuć pieniądze: "))
                            if paid > to_pay: 
                                print(f"Reszta: {(paid - to_pay):5.2} zł.")
                    case _: 
                        print(ERROR_MSG)

                print("Drukowanie biletów...")
                time.sleep(len(cart))
                print("Dziękujemy za skorzystanie z automatu biletowego ")
                cart = []

        case "4": 
            choice = input("Czy na pewno chcesz porzucić koszyk?\nt - tak\nn - nie: ")[0] 
            if choice == "t":
                end = True
            if choice == "n": 
                continue 
            else: print(ERROR_MSG)
        case _:
            print(ERROR_MSG)








