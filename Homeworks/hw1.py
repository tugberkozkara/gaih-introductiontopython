#Homework-1
#Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.
#Merge these two lists. Multiply all values in the new list by 2.
#Use a loop to print the data type of all values in the new list.

list1 = [0,2,4,6,8,10,12,14,16,18]
list2 = [1,3,5,7,9,11,13,15,17,19]

list3 = list1 + list2
list3 = [i*2 for i in list3]
for x in list3:
    print(type(x))
    x += 1