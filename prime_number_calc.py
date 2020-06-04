



#user_inp = input("Please enter a number: ")


def prime_func(num):
    for i in range(2,num+1):
        if(check_prime(i)):
             print(i)



def check_prime(num):
    if(num!= 2 and num%2==0):

        return False
    elif(num>5 and str(num).endswith('5')):

        return False
    elif(num!=7 and num%7==0):
        return False
    else:
        return True

prime_func(50)