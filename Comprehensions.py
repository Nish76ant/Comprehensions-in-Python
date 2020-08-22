#list Comrehension
"""
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)

print(ls)
"""

#List Comrehension
"""
ls = [i for i in range(100) if i%3==0]
print(ls)
"""
#Dictionary Comrehension
#dict1 = {0:"Item0",1:"Item1"------100}

"""
# dict1 = {i:f"item{i}" for i in range(5)}
# print(dict1)

dict1 = {i:f"item{i}" for i in range(5)}
dict1 = {value:key for key,value in dict1.items()}
print(dict1)
"""

#Set Comprehension
"""

dresses = {dress for dress in ['dress1','dress2','dress1','dress2','dress1','dress2']}
print(dresses)
print(type(dresses)) #Set

"""

#Genrators Comprehension
evens = (i for i in range(100) if i%2==0)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())
