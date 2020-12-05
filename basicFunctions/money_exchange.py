#/usr/bin/env python3

import os

os.system("clear")

def menu():
  print ("""
  (" Rupiah Exchange Money 2020")

  Menu

  [1] Dolar
  [2] Euro comming soon
  [3] Yen comming soon

  """)

menu()
def dolar():
  print("Rupiah exchange dollar value \n")
  while(True):
    try:
      d = 14000
      inp = int(input("Enter $"))
      print("= Rp.", int(inp)*int(d))
    except:
      print("Type just number")

while(True):
  sel = input(" Enter Number ")
  if sel == '1' or sel == 'Dolar':
   os.system("clear")
   dolar()
  elif sel == "0":
    os.system("clear")
    menu()
  else:
    print(sel, "Not Found!")
