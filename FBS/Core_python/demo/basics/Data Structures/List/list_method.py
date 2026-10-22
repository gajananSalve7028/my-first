li = [40,10,40,30,20]

# li.append(50)
# li.clear()
# li2[5][0] = 70

#deepcopy & shallowcopy (nested list)
li = [40,10,40,30,20,[90,100]]
li2 = li.copy()
li[5][0] = 70
print(li)
print(li2)

#print(li.count(40))
#li.extend[70,80]



print(li.count(40))
li.extend([70,80])
print(li.index(80))
li.insert(1,90)
li.pop(10)
li.remove(50)
li.reverse()
li.sort(reverse=true)
print(li)


