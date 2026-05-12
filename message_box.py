from tkinter import messagebox

#messagebox.showinfo("info" , "komunikat")
#messagebox.showwarning("warning" , "komunikat")
#messagebox.showerror("error" , "komunikat")

odpowiedz=messagebox.askyesno("pytanie" , "czy chcesz dostac informacje o rabacie?")

if odpowiedz==False:
    print("wcisnieto nie")
else:

    Cena = 100000

    Marka = input("podaj marke:")

    if Marka == "":
        print("nie wpisano pojazdu")
    else:

        if Marka == "Opel":
            Cena=Cena*0.85
        elif Marka == "Skoda":
            Cena=Cena*0.82
        elif Marka == "Audi":
            Cena=Cena*0.80
        else:
            Cena=Cena*0.95
        
        messagebox.showinfo("info",f"Pojazd kosztuje: {Cena:.0f}PLN")
        