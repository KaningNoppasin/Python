mylist = [[1,2,3,4],"LOVE",11,22,"Runeterra"]

print(mylist,mylist[0],mylist[4],mylist[-3],mylist[-1])
                    #[[1, 2, 3, 4], 'LOVE', 11, 22, 'Runeterra'] [1, 2, 3, 4] Runeterra 11 Runeterra
print(mylist)       #[[1, 2, 3, 4], 'LOVE', 11, 22, 'Runeterra']
print(mylist[0])    #[1, 2, 3, 4]
print(mylist[4])    #Runeterra
print(mylist[-3])   #11
print(mylist[-1])   #Runeterra

mylist[-1] = 29 
print(mylist)                   #[[1, 2, 3, 4], 'LOVE', 11, 22, 29]
print(len(mylist[0]))           #4
print(mylist[len("LUCK")])      #29

mylist.append(16)

print(mylist)                   #[[1, 2, 3, 4], 'LOVE', 11, 22, 29, 16]

mylist[0:0] = [-1]
print(mylist)                   #[-1, [1, 2, 3, 4], 'LOVE', 11, 22, 29, 16]

