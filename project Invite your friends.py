try:
    guests = dict()
    amount = int(input("Enter the number of friends joining (including you): \n"))
    if amount <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(0, amount):
            guests[input()] = 0
            
        bill = int(input("Enter the total bill value: \n"))
        for i in guests:
            guests[i] = round(bill / len(guests),2)
        print(guests)
    
except:
    print("No one is joining for the party")
