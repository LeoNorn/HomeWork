class Bank:
    def __init__(self, name, age, money, password):
        self.name = name
        self.age = age
        self._money = money
        self.__passw = password

    def pname(self):
        print(self.name, self._money)

    def __ppas(self):
        print(self.__passw)

    def pasww(self):
        self.__ppas()

beka = Bank('бека', 20, 0, '12345678987543')
beka._money = 123456789

print(beka._money)
beka.pname()

beka.__passw = '0'
print(beka.__passw)
beka.pasww()
print(dir(Bank))


