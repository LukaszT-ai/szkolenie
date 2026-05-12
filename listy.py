owoce = ["jablko", "malina" , "gruszka"]
liczby = [1,4,7,7,24] #duplikaty są dozwolone
mieszana= ["Lukasz",8, True] # różne typy danych

print(owoce)

print(owoce[0]) #"jablko" (pierwszy element)
print(owoce[-1]) #"gruszka" (ostatni element)

owoce[1] = "truskawka"
print(owoce) #['jablko','truskawka','gruszka']

owoce.append("wiśnia")
print(owoce)

owoce.insert(1,"mango")
print(owoce)

owoce.pop()
print(owoce)

owoce.extend(liczby)
print(owoce)

owoce.append([1,2]) #robi liste w liscie
print(owoce)

owoce.extend([1,2]) 
print(owoce)

macierz = [[1,2,3] , [4,5,6] , [7,8,9]]
print(macierz[0]) #5 (srodkowy element)
print(macierz[1][1]) #7 (pierwszy element w trzecim wierszu)
macierz [0][2] = 100
print(macierz)


x = 5

y = x
x = 10

print(y)

x = 'avbc'

y = x
x = 'asfa'

print(y)

x = ["a", "b" , "c"]

y = x
x = ["w", "y" , "u"]

print(y)

x = ["a", "b" , "c"]

y = x

x.append("v")

print(y)

x = ["a", "b" , "c"]

y = x
y=x.copy()
x.append("v")

print(y)