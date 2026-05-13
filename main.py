# 1.	Uruchom program.
# 2.	Wczytaj dane z pliku prices.json.
import json 
import time

#stałe
PROMPT = "Twój wybór"
ERROR_MSG = "Niepoprawny wybór spróbuj ponownie ."

with open("./prices.json", "r", encoding="UTF-8") as jf:
    prices = json.load(jf)

cart = []
end = False 

while not end: 

    print("""Wybierz jedną z opcji: 
    1 - dodaj bilet
    2 - pokaż koszyk
    3 - zapłać
    4 - zakończ program
    """)

    # 9.	Pobierz jeden znak.
    option = input(PROMPT)[0]

    # Jeśli użytkownik wybierze 1:
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
                    exit()
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
                                exit()
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
                                exit()
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
                                exit()
                            case _: 
                                print(ERROR_MSG)
                    if not cont: 
                        break
                    break
                elif ticket2 == "p":
                    cont = False 
                    break 
                elif ticket2 == "k":
                    exit()
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









    # 10.	
    # Na podstawie wyboru wybierz:
    # •	normalny
    # •	ulgowy
    # 11.	Wyświetl:
    # •	o – okresowy
    # •	c – czasowy
    # •	j – jednorazowy
    # 12.	Pobierz jeden znak.
    # 13.	Wyświetl dostępne opcje z pliku JSON (np. dla okresowego):
    # •	1 – półroczny
    # •	2 – miesięczny
    # •	3 – tygodniowy
    # •	4 – jednodniowy
    # 14.	Pobierz jeden znak.
    # 15.	Na podstawie wyboru:
    # •	odczytaj cenę z cennik
    # •	zapisz nazwę biletu
    # 16.	Dodaj bilet do listy koszyk.
    # 17.	Dodaj cenę do suma.
    # 18.	Wyświetl komunikat:
    # •	„Dodano bilet: X, cena: Y zł”
    # Jeśli użytkownik wybierze 2:
    # 19.	Jeśli koszyk jest pusty → pokaż komunikat.
    # 20.	W przeciwnym razie:
    # •	wypisz wszystkie bilety
    # •	pokaż sumę
    # Jeśli użytkownik wybierze 3:
    # 21.	Jeśli koszyk jest pusty → komunikat i powrót do menu.
    # 22.	Wyświetl:
    # •	„Do zapłaty: X zł”
    # 23.	Zapytaj o metodę płatności:
    # •	g – gotówka
    # •	k – karta
    # Jeśli g:
    # 24.	Poproś użytkownika o wpisanie kwoty (może być liczba).
    # 25.	Pobierz kwotę.
    # 26.	Jeśli kwota < suma:
    # •	komunikat „za mało pieniędzy”
    # •	wróć do wpisywania
    # 27.	Jeśli kwota ≥ suma:
    # •	oblicz resztę:
    
    # reszta = kwota - suma
    
    # •	wyświetl:
    # •	„Reszta: X zł”
    # Jeśli k:
    # 28.	Wyświetl komunikat:
    # •	„Płatność zaakceptowana”
    # 29.	Wyświetl:
    # •	„Dziękujemy za zakup”
    # 30.	Wyczyść:
    # •	koszyk
    # •	suma = 0
    # 3.	Zapisz dane do zmiennej (np. cennik jako słownik/dictionary).
    # 4.	Utwórz pusty koszyk (np. lista koszyk = []).
    # 5.	Ustaw zmienną suma = 0.
    # 6.	Wyświetl użytkownikowi opcje:
    # •	1 – dodaj bilet
    # •	2 – pokaż koszyk
    # •	3 – zapłać
    # •	4 – zakończ program
    # 7.	Pobierz jeden znak od użytkownika (np. input()[0]).


    # Jeśli użytkownik wybierze 4:
    # 31.	Zakończ działanie programu.
