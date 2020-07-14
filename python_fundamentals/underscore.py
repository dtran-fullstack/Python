class Underscore:
    def map(self, list, callback):
        for i in range (len(list)):
            list[i] = callback(list[i])
        return list    
        
    def find(self, list, callback):
        for i in range (len(list)):
            if callback(list[i]) == True:
                return list[i]

    def filter(self, list, callback):
        newlist = []
        for i in range (len(list)):
            if callback(list[i]) == True:
                newlist.append(list[i])
        return newlist

    def reject(self, list, callback):
        newlist = []
        for i in range (len(list)):
            if callback(list[i]) == False:
                newlist.append(list[i])
        return newlist

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore

double = _.map([1,2,3], lambda x: x*2)
print(double)
target = _.find([1,2,3,4,5,6], lambda x: x>4)
print(target)
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(odds)
