owoce = {"jablko", "malina" , "gruszka","jablko"}
print(owoce)

#usuwanie duplikatow z listy

numery = [1,2,2,2,3,4,4,4,5,5,6,6,6,6,7]
unikalne=list(  set(numery))
print(unikalne) #wynik [1,2,3,4,5,6,7]

dict = {"brand": "Ford" , "model": "Mondeo" , "year": 2018}
print(dict)



x = dict.get("model")
print(dict)

dict["year"] = 2023 #zmiana wartosci
dict["kolor"] = "czarny" #dodanie nowej pary

print(dict)

mapa = {(52.2 , 21.0): "Warszawa" , (50.0 , 19.9): "Kraków"}

miejsce = mapa[(50.0 , 19.9)]

print(miejsce)

klucze = dict.keys()
print(klucze)

wartosci = dict.values()
print(wartosci)

