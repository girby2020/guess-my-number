###
secret_nr=int(input(" Please think of a number between 0 and 100! : - "))
#variables#
min1= 0
max1= 100
counter=0
computer_guess = abs(max1-min1)//2
difference = abs(computer_guess-secret_nr)
error_margin=0.5
#-------while-------#
while difference > error_margin:
    counter+=1

    print('difference',difference)
    print('The computer guess is ',computer_guess,'...')
    user_question=input('Is computer guess lower[l] \nor highr[h] \nthan secret number \nor correct[c] ? ')
    if user_question =='l':
        min1=computer_guess
        computer_guess=computer_guess+(abs(max1-min1)//2)
    elif user_question =='h':
        max1=computer_guess
        computer_guess=computer_guess-(abs(max1-min1)//2)

    
    elif user_question =='c':
        break
    
    difference = abs(computer_guess-secret_nr)


#----------------------#
print('computer final guess is : ',computer_guess)
print("the number of guesses are : ", counter)

