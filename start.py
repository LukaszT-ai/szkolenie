import cowsay
print ("Hello, World!")
#ConnectionResetError

cowsay.kitty("Cześć!!!")

print(cowsay.char_names)
#komentarz jedno

#wielolinijkowy

print("ala", "ma","kota")
print("****************************************")
print("ala"+"ma"    +     "kota")

#zmienne
x = 5
y = None
z = "tekst"
a = 'tekst'
e = 'a'
r = a

print(r)
print(a)
print(e)
print( z  )

#import keyword
#print(keyword.kwlist)

x = "100"
float(x)
print(x)

y = 10
y = y * 5

print(y)

print("="*60)

miasto = "Warszawa"
print(f"Jestem w {miasto}", "ladna pogoda", sep=",")

print("pobieranie...",end="-")
print("gotowe")

print("lista zakupów:\n\t*chleb\n\t\t*Maslo")

liczba = 12252365478345.546748486

print(f"wynik:{liczba:_}")

print(f"wynik:{liczba:,}")

print(f"zysk:{liczba:,.2f}PLN")

polska_liczba = f"{liczba:_.2f}".replace("," ,  "").replace("."  ,    ".")

print(f"Zysk netto:{polska_liczba}PLN")


x = 123

wynik = str(x).rjust(6,"0")

print(wynik)

print(16.48-16.71)

b = "Hello, Wordl!"