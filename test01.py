n = 1
name = 'Sung'
n = n + 2
value = 1.2 * n

print('{0} = 1.2 * {1}'.format(value, n))
print(name)

greeting = 'Test'
print(greeting[:2]) # l
print(greeting[-2:]) # ld

numbers = {0, 1, 2, 3}
print(numbers)
print(numbers[0])
names = ['Kim', 'Lee', 'Park', 'Choi']
array = numbers + names
print(array)
print(array[-1])

#Tuple
person = ('Kim', 24, 'male')
print(person)
print(person[1])
name, age, gender = person
print(gender)