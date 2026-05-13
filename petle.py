#petle
cars = ['audi', 'bmw' , 'skoda' , 'kia']
#iteracja po liscie
for car in cars:
    print("pojad: ", car)

garaż = {"Toyota": "Corolla", "Mazda": "CX-5", "BMW": "M3" , "Tesla": "Model 5"}

for marka, model in garaż.items():
    print(f"Marka: {marka} | Model: {model}")

print("\n--- POSIADANE MARKI ---")
for marka in garaż.keys():
    print(f"Mam w garażu samochód marki: {marka}")
    pojazd = garaż[marka]

auta_szczegoly= {
    "WA45646":{"marka": "Toyota", "rok": 2020, "przebieg": 50000},
    "WA45e46":{"marka": "BMW", "rok": 2018, "przebieg": 120000}
}

for rejestracja, dane in auta_szczegoly.items():
    print(f"Auto o numerze {rejestracja}:")

    #odwolujemy sie do wew. slownika 'dane'
    marka    = dane["marka"]
    rok      = dane["rok"]
    przebieg = dane["przebieg"]

    print(f" ->{marka} z roku {rok} ma przebieg: {przebieg} ")


licznik = 0
while licznik <5:
    print(f"Licznik wynosi: {licznik}")
    licznik +=1


cars = ['audi', 'bmw' , 'skoda' , 'kia']
szukane = "audi"

for auto in cars:
    if auto == szukane:
        print(f"Znaleziono: {auto}!")
        break
else:
    print(f"Niestety, {szukane} nie ma na liście")
