from datetime import datetime, date, timedelta

#1. Pobranie aktualnego czasu

teraz = datetime.now()
print(f"Teraz jest: {teraz}")

#2. Tworzenie konkretnej daty

Urodziny = date(1981,4,18)
print(f"Urodziny: {Urodziny}")

#3. Arytmetyka dat (timedelta)

# Co bedzie za 100 dni?

przyszlosc = teraz + timedelta(days=100)
print(f"Za 100 dni będzie: {przyszlosc.date()}")


#4. Odejmowanie dat
teraz = date.today()
#lub
#teraz = datetime.now().date()
wynik_dni=(teraz - Urodziny).days
print("Dni, które minęły: ", wynik_dni)

# Obiekt -> Tekst
ladna_data = teraz.strftime("%d.%m.%Y %H:%M")
print(f"Format europejski: {ladna_data}")

