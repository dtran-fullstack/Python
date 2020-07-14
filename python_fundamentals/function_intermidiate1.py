import random
def randInt(min=0   , max=100   ):
    if min > max:
        print("max need to be greater than min")
        return False
    elif max < 0:
        print("negative random number")
        return round(random.random() * (max-min) + min)
    else:
        return round(random.random() * (max-min) + min)

# should print a random integer between 0 to 100
print(randInt()) 		
# should print a random integer between 0 to 50
print(randInt(max=50))
# should print a random integer between 50 to 100
print(randInt(min=50))
# should print a random integer between 50 and 500
print(randInt(min=50, max=500))    
print(randInt(min=-55, max=-1))    

