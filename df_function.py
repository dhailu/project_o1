def show_balance(balance):
    print(f'Your balance is = {balance:.2f}')
     
def deposit():
    amount = float(input('How much you need to deposite today? '))
    if amount < 0:
        print('Please deposit a valid amount')
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input('how much you need to be withdraw? '))
    if amount > balance:
        print('insuffeceint balance')
        return 0
    elif amount < 0:
        print('please enter a valied amount')
        return 0
    else: 
        return amount
   