pins = ['Arif', 'Samed', 'Alik', 'Farid', 'Baba']
x = input("Enter your name: ")
if x in pins:
    a= (input("Enter your pin: "))
    if a == "Sapir":
        print("You are logged in")
    else:
        input("Enter your pin again: ")
else:
    input("Enter your name again: ")
