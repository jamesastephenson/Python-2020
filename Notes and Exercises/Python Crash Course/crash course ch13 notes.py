#Crash Course Chapter 13 notes

#plotting a simple line graph
    #begin by importing pyplot from the matplotlib library
    #abbreviating to plt for brevity
import matplotlib.pyplot as plt
#creating a list of squares that will be the data for our plot
squares = [1, 4, 9, 16, 25]
#the subplots() function can create one or more plots in the same figure
#the variable "fig" represents the entire figore or collection of plots-
#-that are generated
#the varibale "ax" represents a single plot in the figure
    #this is the variable we will be using most of the time
fig, ax = plt.subplots()
#now we use the plot method on our squares list
ax.plot(squares)
plt.show()
