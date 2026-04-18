class Mahsulot:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

class Savat:
    def __init__(self):
        self.mahsulotlar = []

    def mahsulot_qoshish(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def mahsulot_ochirish(self, nomi):
        for mahsulot in self.mahsulotlar:
            if mahsulot.nomi == nomi:
                self.mahsulotlar.remove(mahsulot)
                break

    def umumiy_narx(self):
        umumiy_narx = 0
        for mahsulot in self.mahsulotlar:
            umumiy_narx += mahsulot.narxi
        return umumiy_narx

    def savat_korish(self):
        for i, mahsulot in enumerate(self.mahsulotlar, start=1):
            print(f"{i}. {mahsulot.nomi} - {mahsulot.narxi} so'm")

def asosiy():
    savat = Savat()
    while True:
        print("\n1. Mahsulot qo'shish")
        print("2. Mahsulot o'chirish")
        print("3. Umumiy narxni hisoblash")
        print("4. Savatni ko'rish")
        print("5. Chiqish")
        tanlash = input("Tanlang: ")
        if tanlash == "1":
            nomi = input("Mahsulot nomi: ")
            narxi = int(input("Mahsulot narxi: "))
            mahsulot = Mahsulot(nomi, narxi)
            savat.mahsulot_qoshish(mahsulot)
        elif tanlash == "2":
            nomi = input("Mahsulot nomi: ")
            savat.mahsulot_ochirish(nomi)
        elif tanlash == "3":
            print(f"Umumiy narx: {savat.umumiy_narx()} so'm")
        elif tanlash == "4":
            savat.savat_korish()
        elif tanlash == "5":
            break
        else:
            print("Noto'g'ri tanlov")

asosiy()