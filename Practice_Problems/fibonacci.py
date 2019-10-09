nterms = 100

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
a = 0
b = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(a)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(a,end=' , ')
       nth = a + b
       # update values
       a = b
       b = nth
       count += 1
