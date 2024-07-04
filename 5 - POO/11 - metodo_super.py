class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price


    def __str__(self):
        return f"{self._brand} - {self._model_name}"
    
    @staticmethod
    def make_a_call(phone_number):
        print(f"Ligando para {phone_number}...")


class smartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price)

        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera


Moto = Phone('Motorola', 'Moto G7', 1000)
print(Moto)
Moto.make_a_call('11999999999')
print(f'Valor do {Moto._brand} - {Moto._model_name}: R$ {Moto._price}')
print(vars(Moto))

Iphone = smartPhone("Iphone", "Iphone 12", 10000, "4GB", "256GB", "12MP")
print(Iphone)
Iphone.make_a_call(254548)
print(f'Valor do {Iphone._brand} - {Iphone._model_name}: R$ {Iphone._price}')
print(vars(Iphone))