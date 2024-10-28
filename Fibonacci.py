# Fibonacci
n = int(input("Enter a number: "))

# assign the first two numbers 0 and 1 to two variables
prev = 0
next = 1

# total is the sum of prev and next values
total = 1

print(f"{prev},{next}",end=",")

for i in range(n):
    
    # sum up 2 last 2 numbers
    total = prev + next
    
    print(total,end=",")
    
    # assign last number to the previous and total to the last number
    prev = next
    next = total