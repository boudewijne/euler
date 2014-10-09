def is_palindromic(nr):
    s = str(nr)
    return (s[::-1] == s)
    
result=-1
for i in range(100,999):
    for j in range(100,999):
        if is_palindromic(i*j):
            if(i*j) > result:
                result=i*j           
print (result)