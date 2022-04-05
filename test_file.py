import matplotlib.pyplot as plt

input_values = [19, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
cubes = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()
ax.plot(input_values, squares, 'mD:')
ax.set_ylabel("Squares",color='m')
ax.set_yticks(range(5,26,5))
ax1 = ax.twinx()
ax1.plot(input_values, cubes, 'ro--')
ax1.set_ylabel("Cubes",color='r')
ax1.set_yticks(range(25,126,25))
plt.show()
