"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
#Loop through all possible combinations of 2 elements in q.
#store pairs that equal targeted sum
#store pairs that equal targeted difference
#check if a key is in summs && differences. if so the sums must equal the differences

 # dicts to hold sum and diff values
sums = {}
diffs = {}


#Loop through all possible combinations of 2 elements in q.
#store pairs that equal targeted sum
#store pairs that equal targeted difference

for i in q:
    for j in q:
        #Sums
        s = f(i) + f(j)
        #store a pair that equals this sum
        if s in sums:
            sums[s].append((i,j))

        else:
            sums[s] = [(i,j)]

        #Differences
        d = f(i) - f(j)
        #store pair that equal this difference
        if d in diffs:
            diffs[d].append((i,j))

        else:
            diffs[d] = [(i,j)]

#If a key appears in sums and differences all of the sums must equal the differences
for sum_key in sums:
    if sum_key in diffs:

        #If yes, print all possible combinations of sums and differences which are equal to each other
        for s in sums[sum_key]:
            for d in diffs[sum_key]:  
                # these 0's and 1's are equivelent to (i,j) 
                a, b, c, d = s[0], s[1], d[0], d[1]

                #Make sure it is actually correct
                assert f(a) + f(b) == f(c) - f(d)
                

                print(
                    f"f({a}) + f({b}) = f({c}) - f({d})"
                    f"    {f(a)} + {f(b)} = {f(c)} - {f(d)}"
                    )