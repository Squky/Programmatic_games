




def fib_upto(upto):
    new_num,  f_num = 0,0
    sec_num = 1
    while new_num < upto:
        new_num = f_num + sec_num
        print(f_num)
        f_num = sec_num
        sec_num = new_num

fib_upto(5)
print("\n")



def nth_fib(n):
    new_num, f_num = 0 , 0
    sec_num = 1
    for i in range(n):
        new_num = f_num + sec_num
        print(f_num)
        f_num = sec_num
        sec_num = new_num





nth_fib(5)

def validate(f_num,sec_num,upto):
    if ((f_num or sec_num or upto)!=int  ):
        return False
    else :
        return True



