#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_square=sum(list(map(lambda x:pow(x,2),range(0,101))))
square_sum=pow(sum(range(0,101)),2)
print square_sum-sum_square