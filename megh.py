import random as rd

one = []
second = []
third = []
for i in range(100000):
    temp_one = rd.randint(1, 6)
    one.append(temp_one)
    temp_two = rd.randint(1, 6)
    second.append(temp_two)
    temp = temp_one * temp_two
    third.append(temp)
count = 0
for i in range(100000):
    for j in range(1, 7):
        if third[i] == j**2:
            count += 1
prob = count / 100000
print(prob)
