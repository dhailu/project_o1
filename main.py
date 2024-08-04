import df_function as fuc

def main():
    user = 'user name'
    balance = 0
    is_running = True

    while is_running:
        
        print('***************************')
        print("Welcome to xx Bank {user}\nHow can we help you today? ")

        print('****************************************************************')
        print('1) Balance', ' 2) Deposit', ' 3) Withdraw', ' 4) Exit',  sep="      ")
        print('****************************************************************')
        

        choice = input('Enter your choice (1 - 4): ')

        if choice == '1':
            fuc.show_balance(balance)
        elif choice == '2':
            balance += fuc.deposit()
        elif choice == '3':
            balance -= fuc.withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('PLease enter a valid input ')
    print('Thank you for visiting us today!')
if __name__ == '__main__':
    main()
   



