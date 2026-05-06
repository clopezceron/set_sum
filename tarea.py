#Exercise

def set_sum(lst1, lst2):
    for x in lst1:
        if x not in lst2:
            lst2.append(x)
    return lst2
    

#Exercise

def sorted_set_sum(lst1, lst2):
    for x in lst1:
        if x not in lst2:
            i=0
            if len(lst2)==0:
                lst2.append(x)
            else:
                for y in lst2:
                    if x<y:
                        lst2[i:i]=[x]
                        break
                    else:
                        i=i+1
                        if i==len(lst2):
                            lst2.append (x)
                            break
    return lst2

#Examples 


set_sum([], []) == []
set_sum([1, 2, 3], [1, 2, 3]) 
set_sum([], [1, 2, 3]) 
set_sum([1, 2, 3], []) 
set_sum([1, 3, -2], [-2, -3, 0, 1, 34])
