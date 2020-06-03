

def remv_dup(list):
    new_list=[]
    for i in list:
        if new_list.count(i)<1:
            new_list.append(i)
    return new_list

mylist = ['a', 'b', 'lemon', 'c', 'lemon', 'd', 'a', 'pineapple']

dupe_list =  [1, 1,2, 3, 1, 2, 4, 5, 6, 6, 1, 7, 8, 1,2, 5, 2, 4]
print(remv_dup(mylist))

print(remv_dup(dupe_list))