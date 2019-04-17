import matplotlib.pyplot as plt
import math, os

def func(t):
    return math.cos(t)

def shift(array, new_value):
    for i in range(len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = new_value
    return array

def iteration(answers):
    weights[0] = 0
    for answer in answers:
        weights[0] += answer
    weights[0] /= window_size
    net = weights[0]
    for i in range(1,window_size+1):
        net += weights[i]*answers[i-1]
    return net

def period():
    sum_mistake = 0.0
    answers = []
    for i in range(window_size):
        answers.append(right_answers[i])
    for i in range(N-window_size):
        new_value = iteration(answers)
        mistake = right_answers[i+window_size]-new_value
        for j in range(window_size):
            weights[j+1] += norma*answers[j]*mistake
            sum_mistake += mistake*mistake
        answers = shift(answers, right_answers[i+window_size])
    return sum_mistake

N = 20
a = 1
b = 1.5
norma = 0.4                                         #начальные данные
epsilon = 0.001
window_size = 6
inputs = []
right_answers = []
weights = [0.0]
for i in range(N):
    inputs.append(a+i*(b-a)/N)
for i in range(N):
    right_answers.append(func(inputs[i]))
for i in range(window_size):
    weights.append(0.0)
    
os.system("cls")
x = []
y = []
for i in range(1000):
    x.append(a-0.5+i*(1+2*b-a)/1000)
for i in range(1000):
    y.append(func(x[i]))

measures = []
normas = []
gens = []
res = []
s = 1
#for gen in range(500,5000,100):
    #gens.append(gen)
    #for i in range(gen):
    #    s = period()
for window_size in range(2,20):
    res = []
    weights = [0.0]
    for i in range(window_size):
        weights.append(0.0)
    for i in range(window_size+1):
        res.append(0)
    s = 1
    normas.append(window_size)
    while (epsilon < math.sqrt(s)):
        s = period()
    measure = 0.0
    new_inputs = [inputs[N-1]]                        #проверка
    for i in range(N):
        new_inputs.append(b+i*(b-a)/N)
    new_answers = []
    answers = []
    for i in range(N):
        new_answers.append(func(new_inputs[i]))
    for i in range(window_size):
        answers.append(right_answers[N-window_size+i])
    new_values = [right_answers[N-1]]
    for i in range(N):
        new_value = iteration(answers)
        mistake = func(new_inputs[i+1])-new_value
        #print(measure)
        #print(new_value)
        #print(new_answers)
        measure += mistake*mistake
        answers = shift(answers, new_value)
        new_values.append(new_value)
    measures.append(math.sqrt(measure))
    for i in range(window_size+1):
        res[i]=weights[i]
        weights[i]*=0

print("Weights: ", end = "")
for r in res: print(round(r,3), end = "\t")
print("\nError =",measure)
fig = plt.figure()
#plt.axis([0, 19, 0, 20])
#plt.plot(gens, measures)
plt.plot(normas, measures)
plt.grid(True)
plt.show()
        
fig2 = plt.figure()
plt.plot(x, y)
plt.plot(inputs, right_answers, marker='.', color='r')
plt.plot(new_inputs, new_values, marker='.', color='g')
plt.grid(True)  
plt.show()
