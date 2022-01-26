#import matplotlib.pyplot as plt
import matplotlib.pyplot
# User inserts r value
print('What is the value of r: ')
r = float(input())
# This is Xo
initial = 0.02
array = []
array.append(initial)
#For loop finds the next term in the sequence and stores it in an array to be plotted later
for x in range(100):
       initial = r * initial * (1 - initial)
       array.append(initial)

print(array)
#Matplotlib functions to graph the array
# plt.plot(array)
# plt.title('Logistic Exercise')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

matplotlib.pyplot.plot(array)
matplotlib.pyplot.title('Logistic Exercise')
matplotlib.pyplot.xlabel('x')
matplotlib.pyplot.ylabel('y')
matplotlib.pyplot.show()