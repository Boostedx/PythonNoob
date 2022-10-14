turnON = "Turn on Laptop"
Oclass = "Go to class"
bathroom = "Go to Bathroom"
print('Waking up Pseudocode')
pee = input("Pee? Yes or No: ")
if pee.upper() == "YES":
    print(f"{bathroom} then, {turnON}, then, {Oclass}")
elif pee.upper() == "NO":
    print(f"{turnON} then, {Oclass}")



