
user = int(input('What is your favorite number? '))

if user >= 10:
    print('You have multi-digit taste')
elif user > 0:
    print('You have single digit taste')
elif user < 0:
    print('You have negative taste')
elif user == 0:
    print('You have zero taste')