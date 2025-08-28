#user_input = input("Enter array, with entries spaced with commas.")
#arrau = [int(x) for x in user_input.split(",")]
#min1 = arrau[0]
#for i in arrau:
#    if i < min1:
#        arrau.insert(i,arrau[0])
#print(arrau)


array2 = [4,5555,6,7777,3,34]
for i in array2:
    if i <array2[0]:
        array2.insert(array2[i],0)
print(array2)