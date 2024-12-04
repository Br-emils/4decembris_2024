#Masīvs
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))
#ievadi skaitli
new_list = []

for i in a:
    if i < num:
        new_list.append(i)
#Pievieno sarakstu kas parādīs visus masīva skaitļus līdz tavam skaitlim-1 (ja ievadīts 13 tad termināli 13 nerādīsies)
print(new_list)
#parāda to terminālī