import random as rd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli as brn

def factorial(n) -> float:
    fact = 1
    while i<=n:
        fact *= i
    return fact

def combination(n, r) -> float:
    comb = factorial(n)/(factorial(n-r) * factorial(r))
    return comb



sample = 1000
n = 10
prob_one = 1/4
prob_zero = 1 - prob_one
data = []
for i in range(n):
    temp = brn.rvs(size = sample, p = prob_one)
    data.append(temp)
#print(data)
yn = []
for j in range(sample):
    sum = 0
    for i in range(n):
        sum += data[i][j]
    temp = sum / n
    yn.append(temp)

#print(yn)
prob_yn = []
for i in range(n+1):
    prob_yn.append(0)

for i in range(sample):
    temp = int(yn[i] * n)
    prob_yn[temp] += 1

for i in range(n+1):
    prob_yn[i] /= sample

#print(prob_yn)
mean = 0
for i in range(n+1):
    temp = i * prob_yn[i] / n
    mean += temp

print(mean)

variance = 0
for i in range(n+1):
    temp = ((i/n - mean)**2 ) * prob_yn[i]
    variance += temp

print(variance)
x_axis = []
for i in range(n+1):
    x_axis.append(i/n)

prob_yn_theory = []
for i in range(n+1):
    temp = combination(n, i) * ((1/4) ** i) * ((3/4) ** (n-i))
    prob_yn_theory.append(temp)

#Plotting
plt.stem(x_axis,prob_yn, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem(x_axis,prob_yn_theory, markerfmt='o',use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()