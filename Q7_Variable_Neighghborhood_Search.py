from random import Random
import numpy as np

# number of elements in a solution
n = 100

# maximum iteration
iteration = 1000

# maximum number of flip
MaxFlip = 3
flip = 1


# function to evaluate a solution x
def evaluate(x):
    a = np.array(x)
    b = np.array(values)
    c = np.array(weights)

    value = np.dot(a, b)  # compute the cost value of the knapsack selection
    totalWeight = np.dot(a, c)  # compute the weight value of the knapsack selection

    if totalWeight > maxWeight:
        value = maxWeight - totalWeight
    return [value, totalWeight]


# function to create a 1-flip neighborhood of solution x
def neighborhood(x):
    if flip == 1:
        nbrhood = []

        for i in range(0, n):
            nbrhood.append(x[:])
            if nbrhood[i][i] == 1:
                nbrhood[i][i] = 0
            else:
                nbrhood[i][i] = 1

    elif flip == 2:
        nbrhood = []
        a = -1
        for i in range(0, n):
            for j in range(i, n):
                if i != j:
                    a += 1
                    nbrhood.append(x[:])

                    if nbrhood[a][i] == 1:
                        nbrhood[a][i] = 0
                    else:
                        nbrhood[a][i] = 1
                    # end

                    if nbrhood[a][j] == 1:
                        nbrhood[a][j] = 0
                    else:
                        nbrhood[a][j] = 1

    else:
        nbrhood = []
        for i in range(0, n):
            nbrhood.append(x[:])
            nbrhood[i][i], nbrhood[i][i-3]=nbrhood[i][i-3], nbrhood[i][i]

    return nbrhood

# to setup a random number generator, we will specify a "seed" value
seed = 5113
myPRNG = Random(seed)

# let's create an instance for the knapsack problem
values = []
for i in range(0, n):
    values.append(myPRNG.randint(10, 100))


weights = []
for i in range(0, n):
    weights.append(myPRNG.randint(5, 20))


# define max weight for the knapsack
maxWeight = 5 * n

# monitor the number of solutions evaluated
solutionsChecked = 0

# define the solution variables
# x_curr will hold the current solution
# f_curr will hold the "fitness" of the current soluton
# x_best will hold the best solution
x_curr = []

# start with a random solution
for i in range(0, n):
    if myPRNG.random() < 0.7:
        x_curr.append(0)
    else:
        x_curr.append(1)

# begin local search overall logic
x_best = x_curr[:]
f_curr = evaluate(x_curr)[0]
totalWeight = evaluate(x_curr)[1]
f_best = f_curr

List = {}

for ite in range(iteration):
    flip = 1
    while flip < MaxFlip + 1:

        # create a list of all neighbors in the neighborhood of x_curr
        Neighborhood = neighborhood(x_curr)

        # selecting best neighbor
        x_neigh = Neighborhood[0]
        f_neigh = evaluate(x_neigh)[0]
        totalWeight_neigh = evaluate(x_neigh)[1]

        for s in Neighborhood:
            solutionsChecked = solutionsChecked + 1

            if evaluate(s)[0] > f_neigh:
                if evaluate(s)[0] > f_best:
                        # find the best member and keep track of that solution
                        x_neigh = s[:]
                        f_neigh = evaluate(s)[0]
                        totalWeight_neigh = evaluate(s)[1]

        # update the current list
        x_curr_old = x_curr
        x_curr = x_neigh

        # check if it is maximum
        if f_neigh > f_best:
            x_best = x_neigh
            f_best = f_neigh           #value
            totalWeight = totalWeight_neigh    #weight

            flip = MaxFlip + 1
        else:
            flip += 1


    #
    old_list = List
    List = {}

print("\nFinal: Total number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best)
print("Weight of knapsack: ", totalWeight)
print("Best solution: ", x_best)