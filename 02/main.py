""" Method 1 """

num = int(input("Give me a number to check: "))
#Ievadi skaitli
check = int(input("Give me a number to divide by: "))
#Ievadi skaitli ar kuru dalīt iepriekš minēto skaitli
if num % 4 == 0:
    print(num, "is a multiple of 4")
#Ja skaitlis dalas ar 4 termināli parādīs šo ziņu
elif num % 2 == 0:
    print(num, "is an even number")
#Ja skaitlis dalas ar 2 tad tas tiks parādīts termināli kā pāra skaitlis
else:
    print(num, "is an odd number")
#Ja skaitlis nedalās ar 2 tiks parādīts terminālī ka tas ir nepāra skaitlis
if num % check == 0:
    print(num, "divides evenly by", check)
#Pārbauda vai tavs dotais skaitlis (rinda 3) dalās ar otru doto skaitli (rinda 7) --> Šī ziņa ja dalās
else:
    print(num, "doesn't divide evenly by", check)
#Pārbauda vai tavs dotais skaitlis (rinda 3) dalās ar otru doto skaitli (rinda 7) --> Šī ziņa ja nedalās
""" Method 2 """
num = int(input("Enter a number: "))
mod = num % 2
#pārbauda vai tavs ievadītais skaitlis dalās ar 2
if mod > 0:
    print("You picked an odd number.")
#dalās
else:
    print("You picked an even number.")
#nedalās