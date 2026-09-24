#list in python
#list is an ordered and changeable collection that can store multiple values
marks = [80,90,75,85]

print(marks)

#accessing elements in a list 
marks = [80,90,75,85]

print(marks[0])
print(marks[1])
print(marks[2])

#change elements in a list 
marks = [80,90,75]
marks[1] = 95

print(marks)


#change element h.w
marks = [75,95,86,70,69,98]
marks[1] = 60
marks[3] = 75
marks[5] = 100

print(marks)


#accessing element h.w
marks = [75,95,86,70,69,98]

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

#add elements to a list
marks = [80,90,75]

marks.append(85)
print(marks)


#remove elements from a list
marks = [80,90,75]

marks.remove(90)

print(marks)


#insert elements to a list
numbers = [10,20,30]

numbers.insert(1,15)

print(numbers)

#extend method
a=[1,2,3]
b=[4,5,6]
a.extend(b)

print(a)

#clear 
numbers = [10,20,30]

numbers.clear()

print(numbers)

#
numbers =[10,20,30,40]

print(numbers.index(30))

#
numbers = [10,20,20,30,20]
print(numbers.count(20))

#

numbers =[40,10,30,20]

numbers.sort()

print(numbers)

numbers.sort(reverse=True)

print(numbers)

#
#reverse method
numbers =[10,30,20]
numbers.reverse()
print(numbers)

#
#copy method
a = [1,2,3]

b = a.copy()

print(b)

#

#slice
numbers =[10,20,30,40,50]

print(numbers[1:4]) #print start at 1 and stop when 4 comes
print(numbers[:3])#print start at 0 and stops when 3 comes
print(numbers[2:])# print starts from 3 and continuous upto list
print(numbers[::-1]) # start from end and jumps at 1
print(numbers[::-3]) 


#various methods
numbers = (10,20,30,40,50,60)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


#sets in python

#set is a colletion of unique values that is unordered and mutable
numbers = {10,20,30,40,20,30,40}
print(numbers)

#add values to a set
subjects={"Python","Java"}

subjects.add("SQL")
print(subjects)

#remove values from the set
subjects.remove("Java")
print(subjects) 

#sets do not allow the duplicate values
numbers={1,2,3,3,2,4}
print(numbers)

#Dictionaries in python
#dictionary is a collection of key-value pairs that is unordered,changable and indexed
student ={
    "name":"Madhan",
    "age": 20,
    "Course": "Python",
}
print(student)

#access elements in dictionary
print(student["name"])
print(student["age"])
print(student["Course"])
print(student)




#add new data to a dictionary
student["city"]="Tirupathi"

print(student)

#
print(student.keys())
#keys() returns all the keys in the dictionary
print(student.values())
#values() returns all the values in the dictionary
print(student.items()) 
#items() returns all the key-value pairs in the dictionary
print(student.get("name"))
# get() returns the value for the specified key
student.update({"age": 22})
# update() update the value of the specified key
student.pop("Course")
# pop() removes the specified key-value pair from the dictionary

print(student)

#popitem() removes the last inserted key-value pair from the dictionary
student={
    "name":"Madhan",
    "age": 22,
    "course":"Python",
}
student.popitem()
print(student)

#setdefault() returns the value of the specified key. If the key does not exist, it inserts the key with the specified value
student = {
    "name":"Madhan"
    }
student.setdefault("age",21)
print(student)
