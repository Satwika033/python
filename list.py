'''l1 = []
print(l1)
print(type(l1))'''
'''l3 = []
l3 = eval(input("enter the elements"))
print(l3)
print(type(l3))'''
'''l1 = [1,2,3]
print(l1)
print(id(l1))
print(type(l1))
l2 = l1.copy()
print(l2)
print(id(l2))
print(type(l2))'''
a = eval(input("enter the value of a"))
b = eval(input("enter the value of b")) 
sum = a+b
avg = sum/2
print('sum=',sum)
print('avg=',avg)
'''square = [(x*x),int(x) for x in input("enter the values of x").split(' ')]
print(a)
print(b)
sum = a+b
print(sum)'''
'''a = [int(x) for x in input("enter the values of a").split(' ')]
print(a)'''
'''l1 = [10,20,30]
l2 = [10,[20],30]
l2[0][1] = 222
print(l1)
print(l2)
print(type(l1))
print(id(l1))
print(type(l2))
print(id(l2))'''
l1 = [12,34,45,63,78,90,23,45,23,54]
#odd = [int(x) for x in l1 if x % 2 == 0]
#print(odd)
l1.pop(0)
print(l1)
#list
l1 = [60,67,34,65,90,45]
print(l1)
print(type(l1))
print(id(l1))
print(len(l1))
l1.insert(0,True)
print(l1)
print(l1.index(60))
print(l1.count(60))
l2 =[True]
l1.extend(l2)
print(l1)
l2 = l1.copy()
print(l2)
print(l1.pop(1))
print(l1)
l1.sort(reverse = True)
print(l1)
l1.sort()
print(l1)




