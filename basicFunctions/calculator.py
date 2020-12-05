#!/usr/bin/env python3

#program calculator

print("Ini adalah program calculator")
print("=============================")
#print("masukan angka pertama?")
number1 = float(input("masukan angka pertama? "))
#print("masukan angka kedua?")
number2 = float(input("masukan angka kedua? "))


menu = str(input("Pilih Menu Operasi * /  + - = "))
if menu == "*":
    hasil = ( number1 * number2)
    print("Hasil Operasi adalah = " + str(hasil)  )
elif menu == "+":
    hasil = (number1 + number2)
    print("Hasil Operasi adalah = " + str(hasil)  )
elif menu == "-":
    hasil = (number1 - number2)
    print("Hasil Operasi adalah = " + str(hasil)  )
else:
    hasil = (number1 / number2)
    print("Hasil Operasi adalah = " + str(hasil)  )
