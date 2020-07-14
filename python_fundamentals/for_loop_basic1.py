# Basic
for i in range(151):
    print(i)

# Multiplies of Five
for i in range(0,1001,5):
    print(i)

# Counting
for i in range(1,101):
    if(i%10 == 0):
        print(i,"Coding Dojo")
    elif(i%5 == 0):
        print(i,"Coding")

# Add Odd
sum = 0
for i in range(500000):
    if(i%2 != 0):
        sum+=i

print(sum)

# Print positive num starting from 2018, count down by 4
for i in range(2018,0,-4):
    print(i)

# Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if(i%3 == 0):
        print(i)