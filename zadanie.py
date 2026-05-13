from tkinter import messagebox

ceny_pln= [45000, 120000, 32500, 89900, 55000]
suma_cen=sum(ceny_pln)
srednia_cena=sum(ceny_pln)/len(ceny_pln)

odpowiedz = messagebox.askyesno("pytanie" , "czy chcesz wyświetlić wyniki w walucie Euro?")
if odpowiedz == False:
    messagebox.showinfo("info",f"suma cen: {suma_cen:.0f}PLN\nwartość średnia: {srednia_cena:.02f}PLN")
else:
    kurs = 4.33
    suma_euro = suma_cen/kurs
    srednia_euro = srednia_cena/kurs
    messagebox.showinfo("info",f"suma cen: {suma_euro:.0f}EUR\nwartość średnia: {srednia_euro:.02f}EUR")