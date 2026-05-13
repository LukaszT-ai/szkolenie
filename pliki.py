file = open("plik.txt", "rt", encoding="utf8")

zawartosc = file.read()
print(zawartosc)

zawartosc = file.read(10)

print(zawartosc)

for wiersz in file:
    print(wiersz.strip())
file.close()

file = open("plik2.txt","w")
file.write("Zosia ma kotka")
file.close()


file = open("plik2.txt", "a", encoding="utf8")
file.write("\nKrzyś ma Jelcza.")
file.close()


