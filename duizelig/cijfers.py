import random

top_of_range = input('Type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 50:
        print('please type a number larger than 50 next time.')
        quit()
else:
    print('please type a number next time')
    quit()


random_number =random.randrange(50, 1001, top_of_range)



while True:
    
    user_guess =input('make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time')
        continue 

    if user_guess == random_number:
        print('you got it!')
    else:
        print('you got it wrong!')


