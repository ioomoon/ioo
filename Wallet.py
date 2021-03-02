class Wallet:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def client_information(self):
        return f"Клиент: {self.name} {self.surname}" '\n'f"Баланс: {self.balance}"


client_1 = Wallet("Иван", "Иванов", 50)
print(client_1.client_information())


