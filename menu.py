class Menu:
    def __init__(self, options):
        self.options = options

    def display(self):
        print("Wybierz jedną z opcji:")
        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")

    def choose_option(self):
        while True:
            try:
                choice = int(input("Wybierz opcję: "))
                return self.select_option(choice)
            except ValueError:
                print("Nieprawidłowa opcja. Spróbuj ponownie.")

    def select_option(self, choice):
        if 1 <= choice <= len(self.options):
            return self.options[choice - 1]
        else:
            raise ValueError("Invalid menu option selected.")