from datetime import datetime, date, timedelta

#zad. teksty

tekst_CSV = "03/12/2026 jan KOWalski wypłata PLN:8359"

mc = tekst_CSV[0:2]
dzien = tekst_CSV[3:5]
rok = tekst_CSV[6:10]
print(f'rok: {rok}  mc:{mc}  dzien: {dzien}')


imie_nazwisko = tekst_CSV[11:23].title()
print(imie_nazwisko)

pozycja = tekst_CSV.find(":")
liczba_str = tekst_CSV[pozycja + 2:]
wypłata_EUR = float(liczba_str) / 4.33
print(f'EUR: {wypłata_EUR:,.2f}')

data = tekst_CSV[0:10]
data_obiekt = datetime.strptime(data, '%m/%d/%Y') #parsowanie daty
#zmiana tekstu na "prawidłową" datę
data_ladna = data_obiekt.strftime( '%Y-%m-%d')
# zmiana formatu daty na inny - string (teskt)
print(data_ladna)

lista = tekst_CSV.split()
print(lista)

lista[1] = lista[1].title()
lista[2] = lista[2].title()
print(lista[1],lista[2])

lista = ["Ala", "ma", "kota"]
         
tekst= ' '.join(lista)

#przed krpką separator, który połączy elementy listy

print(tekst)

