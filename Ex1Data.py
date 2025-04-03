
#Creating list, tuple, set and dictionary
list1 = ['banana', 'maça', 3, True, 1, 'banana']
tuple1 = ('banana', 'maça', 2, True, 1,'banana')
set1 = {'banana', 'maça', 2, True, 1, 'banana'}
dict1 = {'banana':'amarela', 'maça':'vermelha', 'quantidade':2, 'Status':True, 'Quantidade':1, 'banana':'amarela'}


#Check "Duplicates", How many elements in the list
print(len(list1))   #6 Allow Duplicates
print(len(tuple1))  #6 Allow Duplicates
print(len(set1))    #4 Ignores Duplicates - because value: True = 1 and banana is repeated
print(len(dict1))   #5 Ignores Duplicates - 'banana':'amarela' is duplicated


#Calling every type by index to check
print(list1[1]) #maça
print(tuple1[2]) #2
# print(set1[3]) #Error - cant index set # Unordered
# print(dict1[0]) #Error - cant index dict # unordered

#Edit
list1[0]= 'cocada' #WRONG
#tuple1[1]= 'uva' # WORKAROUND - You can convert the tuple into a list, change the list, and convert the list back into a tuple

y = list(tuple1)
y[1] = 'morango'
tuple1 = tuple(y)

#set1[1]= 'manga' #WORKAROUND - You can convert the tuple into a list, change the list, and convert the list back into a tuple
yset = list(set1)
yset[1] = 'morango'
set1 = tuple(yset)

dict1['banana']= 'kiwi' 
print(list1)
print(tuple1)
print(set1)
print(dict1)
