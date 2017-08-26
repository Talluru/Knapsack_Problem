

# ------------------------------------------------------------------------------

# Student name:
# Date:

# need some python libraries
import copy
from random import Random, random
from math import exp

import math
import numpy as np

# to setup a random number generator, we will specify a "seed" value
# need this for the random number generation -- do not change
seed = 5113
myPRNG = Random(seed)
n = 100
# to get a random number between 0 and 1, use this:             myPRNG.random()
# to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
# to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

# number of elements in a solution


# create an "instance" for the knapsack problem
value = []
for i in range(0, n):
    value.append(myPRNG.uniform(10, 100))

weights = []
for i in range(0, n):
    weights.append(myPRNG.uniform(5, 20))


maxWeight = 5 * n

print(value)
print(weights)

# change anything you like below this line ------------------------------------

# monitor the number of solutions evaluated
solutionsChecked = 0

def evaluate(x):
    a = np.array(x)
    b = np.array(value)
    c = np.array(weights)

    totalValue = np.dot(a, b)  # compute the value of the knapsack selection
    totalWeight = np.dot(a, c)  # compute the weight value of the knapsack selection

    if totalWeight > maxWeight:
        return [totalWeight-maxWeight, totalWeight]
    else:
        return [totalValue, totalWeight]  # returns a list of both total value and total weight

def OneflipNeighborhood(x):
    nbrhood = []

    for i in range(0, n):
        temp=list(x)
        nbrhood.append(temp)
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1

    return nbrhood

def TwoflipNeighborhood(x):
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

                if nbrhood[a][j] == 1:
                    nbrhood[a][j] = 0
                else:
                    nbrhood[a][j] = 1
    print("neighborhood size:", len(nbrhood))
    return nbrhood

def ThreeflipNeighborhood(x):
    nbrhood = []
    a=-1
    for i in range(0, n):
        for j in range(i, n):
            for k in range(j, n):
                if i != j and i != k and j != k:
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
                    # end

                    if nbrhood[a][k] == 1:
                        nbrhood[a][k] = 0
                    else:
                        nbrhood[a][k] = 1
    print("neighborhood length:",len(nbrhood))
    return nbrhood

def SwapNeighborhood(x):
    nbrhood = []

    for i in range(0, n):
        nbrhood.append(x[:])
        nbrhood[i][i], nbrhood[i][i-3]=nbrhood[i][i-3], nbrhood[i][i]
    print("neighborhood size:", len(nbrhood))
    return nbrhood

def InsertNeighborhood(x):
    nbrhood = []

    for i in range(0, n):
        nbrhood.append(x[:])
        nbrhood[i].append(nbrhood[i][i])
        nbrhood[i].remove(nbrhood[i][i])
    print("neighborhood size:", len(nbrhood))
    return nbrhood

def Initial_solution(initial_prop_of_items):  #initial prop of items is proportion of items in initial solution
    np.random.seed(1)    #seed
    x = np.random.binomial(1, initial_prop_of_items, size=n)
    print("Random Initial Solution with one_prop: ", initial_prop_of_items )
    print(x)
    print("\n\n")
    return x

def Random_Initial_solution(initial_prop_of_items, random_seed):
    #Random initial solution of hill climbing wiht random restarts
    np.random.seed(random_seed)
    x = np.random.binomial(1, initial_prop_of_items, size=n)
    print("Random Initial Solution with one_prop: ", initial_prop_of_items )
    print(x)
    print("\n\n")
    return x

def print_results(solutionsChecked, f_best, x_best):
    print("\nFinal number of solutions checked: ", solutionsChecked)
    print("Best value found: ", f_best[0])
    print("Weight is: ", f_best[1])
    print("Total number of items selected: ", np.sum(x_best))
    print("Best solution: ", x_best)

def hill_climbing_with_best_improvement(initial_prop_of_items):
    print("Hill Climbing with best improvement")
    print("Initial Prop of items:", initial_prop_of_items)

    solutionsChecked = 0

    x_curr = Initial_solution(initial_prop_of_items)  # x_curr will hold the current solution
    x_best = x_curr[:]  # x_best will hold the best solution

    f_curr = evaluate(x_curr)  # f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]

    # begin local search overall logic ----------------

    i = 1
    done = 0

    while done == 0:

        Neighborhood = OneflipNeighborhood(x_curr)  # create a list of all neighbors in the neighborhood of x_curr

        for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
            solutionsChecked = solutionsChecked + 1
            # print(i)
            # i = i + 1
            if (evaluate(s)[0] > f_best[0]):  # and (evaluate(s)[1]< maxWeight):
                x_best = s[:]  # find the best member and keep track of that solution
                f_best = evaluate(s)[:]  # and store its evaluation
                print(evaluate(s)[1])

        if f_best == f_curr:  # if there were no improving solutions in the neighborhood
            done = 1
        else:

            x_curr = x_best[:]  # else: move to the neighbor solution and continue
            f_curr = f_best[:]  # evalute the current solution

            print("\nTotal number of solutions checked: ", solutionsChecked)
            print("Best value found so far: ", f_best)

    print_results(solutionsChecked,f_best, x_best)

    print("\n\n\n")

def hill_climbing_with_first_improvement(initial_prop_of_items):
    print("Hill Climbing with first improvement")
    print("Initial Prop of items:", initial_prop_of_items)

    solutionsChecked = 0

    x_curr = Initial_solution(initial_prop_of_items)  # x_curr will hold the current solution
    x_best = x_curr[:]  # x_best will hold the best solution

    f_curr = evaluate(x_curr)  # f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]

    # begin local search overall logic ----------------

    i = 1
    done = 0

    while done == 0:

        Neighborhood = OneflipNeighborhood(x_curr)  # create a list of all neighbors in the neighborhood of x_curr

        for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
            solutionsChecked = solutionsChecked + 1
            # print(i)
            # i = i + 1
            if (evaluate(s)[0] > f_best[0]):  # and (evaluate(s)[1]< maxWeight):
                x_best = s[:]  # find the best member and keep track of that solution
                f_best = evaluate(s)[:]  # and store its evaluation
                print(evaluate(s)[1])
                break    #the loop will break once improvement is found

        if f_best == f_curr:  # if there were no improving solutions in the neighborhood
            done = 1
        else:

            x_curr = x_best[:]  # else: move to the neighbor solution and continue
            f_curr = f_best[:]  # evalute the current solution

            print("\nTotal number of solutions checked: ", solutionsChecked)
            print("Best value found so far: ", f_best)

    print_results(solutionsChecked, f_best, x_best)
    print("\n\n\n")

def hill_climbing_with_random_restarts(initial_prop_of_items, restarts):
    print("Hill Climbing with random restarts")
    print("Initial Prop of items:", initial_prop_of_items)
    print("No. of restarts:", restarts)

    solutionsChecked=0
    f_super_best= [0,0]
    for restart in range(restarts):
        seed = restart

        # begin local search overall logic ----------------
        done = 0
        print(restart)
        x_curr = Random_Initial_solution(0.2, restart)  # x_curr will hold the current solution
        x_best = x_curr[:]  # x_best will hold the best solution
        f_curr = evaluate(x_curr)[:]  # f_curr will hold the evaluation of the current soluton
        f_best = f_curr[:]     #best solution in current restart


        while done == 0:

            Neighborhood = OneflipNeighborhood(x_curr)  # create a list of all neighbors in the neighborhood of x_curr

            for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
                solutionsChecked = solutionsChecked + 1
                # print(i)
                # i = i + 1
                if (evaluate(s)[0] > f_best[0]):  # and (evaluate(s)[1]< maxWeight):
                    x_best = s[:]  # find the best member and keep track of that solution
                    f_best = evaluate(s)[:]  # and store its evaluation


            if f_best == f_curr:  # if there were no improving solutions in the neighborhood
                done = 1
            else:

                x_curr = x_best[:]  # else: move to the neighbor solution and continue
                f_curr = f_best[:]  # evalute the current solution


                print("Best value found so far: ", f_best)

        print(f_best[0])
        if (f_best[0] > f_super_best[0]):
            f_super_best = f_best[:]     #best value so far
            x_super_best = x_best[:]     #best solution so far

    print("Solutions checked:", solutionsChecked,
          "Super best value:", f_super_best,
          "Super best solution", x_super_best)
    print("\n\n\n")

def hill_climbing_with_random_walk(initial_prop_of_items, random_walk_prob,
                                   max_super_best_steps):

    print("Hill Climbing with random walk")
    print("Initial Prop of items:", initial_prop_of_items)
    print("Random walk probability", random_walk_prob)
    print("Max No. of steps without improvement", max_super_best_steps)

    import random
    solutionsChecked = 0

    x_curr = Initial_solution(initial_prop_of_items)  # x_curr will hold the current solution
    x_best = x_curr[:]  # x_best will hold the best solution

    f_curr = evaluate(x_curr)[:]  # f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]          #Best solution in neighbourhood
    f_super_best = f_curr[:]
    # begin local search overall logic ----------------
    count=0   #number of iteration with out improvement


    while (count < max_super_best_steps) :

        Neighborhood = OneflipNeighborhood(x_curr)  # create a list of all neighbors in the neighborhood of x_curr

        eeta = random.uniform(0, 1)
        if (eeta > random_walk_prob):

            f_best[0]=0
            for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
                solutionsChecked = solutionsChecked + 1

                if (evaluate(s)[0] > f_best[0]):  # and (evaluate(s)[1]< maxWeight):
                    x_curr = s[:]  # find the best member and keep track of that solution
                    f_best = evaluate(s)[:]  # and store its evaluation
        else:
            x_curr = Neighborhood[random.randint(0, len(Neighborhood)-1)]

        if (evaluate(x_curr)[0] > f_super_best[0]):   #to remember best solution
            f_super_best = evaluate(x_curr)[:]      #best solution so far
            x_super_best = x_curr[:]
            change = 1        #To record change

        count = count + 1    #counting number of iterations without improvement

        if(change == 1):      #Reseting count and change
            count=0
            change=0

    print_results(solutionsChecked,f_super_best, x_super_best)
    print("\n\n\n")

def simulated_Annealing(initial_prop_of_items, initial_temp,
                        iter_per_temp, final_temp):

    print("Simulated Annealing")
    print("Initial Prop of items:", initial_prop_of_items)
    print("Initial temp", initial_temp)
    print("Final temp", final_temp)
    print("Iteration per temperature", iter_per_temp)

    import random
    solutionsChecked = 0
    total_improvements=0    #No of improving moves
    total_randomsteps=0     #No of random moves

    x_curr = Initial_solution(initial_prop_of_items)  # x_curr will hold the current solution
    x_best = x_curr[:]  # x_best will hold the best solution

    f_curr = evaluate(x_curr)[:]  # f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]

    k=0
    while (initial_temp/(k+1) > final_temp):     #Temp check

        m=0     # Counting iteration in current temp

        improvements=0   # improvements in current iteration
        randomsteps=0    # Random steps in current iteration

        while (m < iter_per_temp):
            solutionsChecked = solutionsChecked + 1

            Neighborhood = OneflipNeighborhood(x_curr)

            s= Neighborhood[random.randint(0, len(Neighborhood)-1)]   #Selecting random neighbour

            if (evaluate(s)[0] > f_curr[0]):
                x_curr = s[:]
                f_curr = evaluate(s)[:]
                improvements=improvements+1

            else:
                delta = evaluate(x_curr)[0] - evaluate(s)[0]
                eeta = random.uniform(0,1)
                randomness= math.exp(-1 * delta * (k+1) / (initial_temp))
                #print(delta,"    ",randomness, eeta<randomness)
                if (eeta < randomness):
                    x_curr=s[:]
                    f_curr=evaluate(s)[:]
                    randomsteps = randomsteps+1

            if(f_curr[0]>f_best[0]):    #Recording best value found so far
                x_best=x_curr[:]
                f_best=f_curr[:]

            m = m+1

        total_improvements = total_improvements + improvements      #total improvements
        total_randomsteps = total_randomsteps + randomsteps         #total random steps
        k = k + 1


    print("Final best solution", x_best,"\n",
          "Value:", f_best[0],
          "Weight:", f_best[1])

    print("Total random steps:", total_randomsteps,
          "Total improvements", total_improvements)

    print("Solutions checked", solutionsChecked)
    print("\n\n\n")

def taboo_search(initial_prop_of_items, taboo_tenure,
                 max_super_best_steps):
    print("Taboo Search")
    print("Initial Prop of items:", initial_prop_of_items)
    print("taboo tenure", taboo_tenure)
    print("Max super best steps", max_super_best_steps)

    solutionsChecked = 0

    x_curr = Initial_solution(initial_prop_of_items)  # x_curr will hold the current solution
    x_best = x_curr[:]  # x_best will hold the best solution

    f_curr = evaluate(x_curr)  # f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]          #Best solution in neighbourhood
    f_super_best=f_curr[:]     #Best solution so far

    taboo_list=[0]*n            #taboo status of each element in solution
    count=0                     #counting number of non improving steps


    while (count< max_super_best_steps):

        Neighborhood = OneflipNeighborhood(x_curr)  # create a list of all neighbors in the neighborhood of x_curr
        neighbor=0      #Number of element changed in current step
        f_best[0]=0     #Reseting best neighbour value to zero
        for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
            solutionsChecked=solutionsChecked+1

            if (evaluate(s)[0] > f_best[0]) and (taboo_list[neighbor]==0):  # and (evaluate(s)[1]< maxWeight):
                x_curr = s[:]  # find the best member and keep track of that solution
                f_best = evaluate(s)[:]    #Best solution in neighbourhood
                neighbor_selected = neighbor   #neighbour selected in current step

            if (evaluate(s)[0]> f_super_best[0]):    #Updating best solution fourd so far
                x_curr = s[:]
                f_best = evaluate(s)[:]
                f_super_best = evaluate(s)[:]
                x_super= s[:]
                neighbor_selected = neighbor
                change=1

            neighbor = neighbor + 1

        count = count + 1           #Counting number of steps with our improvement

        if(change == 1):            #Recording change status
            count=0
            change=0

        for i in range(0,len(taboo_list)-1):   #Updating taboo status of each item
            xx=taboo_list[i]
            if(xx>0):
                taboo_list[i]=xx-1

        taboo_list[neighbor_selected]=taboo_tenure   #Updating taboo status of selected item

        #print(x_curr)
        #print(taboo_list)
        print("Neighbor selected:", neighbor_selected, "Best_value", f_best[0])
        print("Highest value found:", f_super_best[0])
        print("\n")

    print("Final best", x_super,"\n",
          "Solutions checed", solutionsChecked,
          "Value:", f_best[0],
          "Weight:", f_best[1],
          "Highest value found:", f_super_best[0],
          "Best Solution:", x_super)
    print("\n\n\n")


# #hill climbing with best improvement
#
hill_climbing_with_best_improvement(0)      #0 initial items
hill_climbing_with_best_improvement(0.1)    #10 initial items
hill_climbing_with_best_improvement(0.2)    #20 initial items
hill_climbing_with_best_improvement(0.3)
hill_climbing_with_best_improvement(0.5)
#
#
# #hill climbing with first improvement
hill_climbing_with_first_improvement(0)
hill_climbing_with_first_improvement(0.1)
hill_climbing_with_first_improvement(0.2)
hill_climbing_with_first_improvement(0.3)
hill_climbing_with_first_improvement(0.5)
#
#
# #Hill climbing with random restarts
hill_climbing_with_random_restarts(0.1, 100)  #0.1 initial prop of items, 100 restarts
hill_climbing_with_random_restarts(0.3, 100)
hill_climbing_with_random_restarts(0.5, 100)
#
#
# #hill climbing with random walk
hill_climbing_with_random_walk(0.1, 0.1, 500) #500 steps with out change in max value
#
#
# #simulate Annealing
simulated_Annealing(initial_prop_of_items=0.1, initial_temp=8000,
                 iter_per_temp = 50, final_temp=5)
simulated_Annealing(initial_prop_of_items=0.1, initial_temp=8000,
                   iter_per_temp = 100, final_temp=5)
simulated_Annealing(initial_prop_of_items=0.1, initial_temp=8000,
                   iter_per_temp = 300, final_temp=5)
simulated_Annealing(initial_prop_of_items=0.1, initial_temp=8000,
                   iter_per_temp = 1000, final_temp=5)

# #Taboo search
taboo_search(0.1, 30, 10000)   #Taboo tenure 30, #max steps without improvement 10,000
taboo_search(0.1, 30, 2000)
taboo_search(0.1, 30, 1000)
taboo_search(0.1, 30, 100)
