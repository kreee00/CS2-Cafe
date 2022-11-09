print('Welcome to CS2 Cafe!')
name = input('What\'s your name? ')
menu = '''
[a] Black Coffee - RM5
[b] Tea - RM6
[c] Caramel Coffee - RM7 '''
option = 1
while option == 1:
    print('\nHi {}, please select the drink below:\n {}'.format(name,menu))
    choice = input('Which drink would you like? ')
    if choice == 'a':
      cup = eval(input('How many cup(s) do you want? '))
      totPrice = 5*cup
      drink = 'Black Coffee'
      option = int(input('''
      Press [1] to restart or [2] to finish order.
      '''))
    elif choice == 'b':
      cup = eval(input('How many cup(s) do you want? '))
      totPrice = 6*cup
      drink = 'Tea'    
      option = int(input('''
      Press [1] to restart or [2] to finish order.
      '''))
    elif choice == 'c':
      cup = eval(input('How many cup(s) do you want? '))
      totPrice = 7*cup
      drink = 'Caramel Coffee' 
      option = int(input('''
      Press [1] to restart or [2] to finish order.
      '''))
    elif choice:
      print('Sorry, we don\'t have that in our menu yet :( ')
      option = int(input('''
      Press [1] to restart or [2] to cancel order.
      '''))
      if option == 2:
        print('Have a good day!')
        break
else:
  print(f'''
      You ordered {cup} cup(s) of {drink}.
      The total price is RM {totPrice}.00.
      You may pay at the counter by using
      cash, debit card, credit card or even
      online banking.
    
      Thank you for visiting our humble cafe :).
      Have a good day!
    ''')