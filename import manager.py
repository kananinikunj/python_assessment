import manager


print('Welcome to fruit market : '.upper().center(100))
manager.blank(1)
print('1) Manager '.center(85))
print('2) Customer '.center(85))
manager.blank(2)
user = input('Select your Role : > ')

if user == '1':

    inp = 'y'
    
    while inp == 'y' or inp == 'Y':
        print('Fruit market Manager  '.title().center(95))
        manager.blank(1)
        print(' '.center(35), '1) Add Fruit Stock ')
        print(' '.center(35), '2) View Fruit Stock')
        print(' '.center(35), '3) Update Fruit Stock')
        manager.blank(2)
        
        man = input('Enter Your Choice : > ')
        while man not in ['1','2']:
            print("Please Enter a valid choice !!")
            man = input('Enter Your Choice : > ')

        manager.blank(2)

        if man == '1':

            print('add fruit stock'.upper())
            name = input('Enter Fruit Name : ').capitalize()
            qty = int(input('Enter qty in Kg : '))
            price = int(input('Enter price for Kg : '))
            manager.Manager.add_stock(name,qty,price)
            manager.blank(1)
            ###       You can comment below lines if you want         ###
            print(f"'{name}' of '{qty}' Kg with the price of '{price}/-' added in your stocks")
            manager.blank(2)
            # print(manager.Manager.stock)

        elif man == '2':

            print('Your Fruit stocks are as listed below : ')
            manager.blank(1)
            fruits = manager.Manager.view_stock()
            print('Name'.center(20), "||",'Qty'.center(10), "||", "Price".center(10))
            print("="*50)
            for name,fruit in fruits.items():
                print(name.center(20),'||',str(fruit['qty']).center(10),"||",str(fruit['price']).center(10))
                
        manager.blank(2)
        inp = input('Do you want to perform more operations : press "y" for Yes and any key for No : ')

else:

    print('With Half Assessment details we can not complete whole code!!')
    print("We are Humans not God!! So, We can not predict your later half Doc!!")