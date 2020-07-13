import random
class kelimetahmin:
    def __init__(self,tahmin):
        self.tahmin = tahmin
        self.words = []
        self.word = " "
    def dosya(self):
        with open ("kelimeler.txt","r",encoding="utf-8") as fp:
            kelimeler = fp.readlines()
            for i in kelimeler:
                self.words.append(i)
            self.word = random.choice(self.words)
        return self.word
    def kelime(self):
        self.secret = []
        for i in range(len(self.word)-1):
            if self.word[i]!=" ":
                self.secret.append("-")
            else:
                self.secret.append("    ")

        return self.secret
    def tahminn(self):
            self.tahmin = input("harf giriniz: ")
            for i in range(len(self.word)):
                if self.word[i] == self.tahmin:
                    self.secret[i]= self.tahmin
            print(self.secret)
    def yazdir(self):
        print(self.word)
    def gameover(self,sontahmin):
        if sontahmin == self.word:
            print("kazandınız")
        else:
            print("kaybettiniz")


kto = kelimetahmin("d")
kto.dosya()
print(kto.kelime())
i = 0
while i <5:
    kto.tahminn()
    i+=1
tahmin = input("harf hakkınız bitti tahminizi giriniz :")
kto.gameover(tahmin)


kto.yazdir()
