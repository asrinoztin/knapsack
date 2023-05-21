import time
import matplotlib.pyplot as plt
import random
import numpy as np

wt = [1, 4, 5]

bag_capacities = []
selections = []
times_recursive = []
times_dynamic = []



def flow():
    rand_size(20)  # try with 20 different bag capacities
    for i in bag_capacities:        
        dynamic_table = np.zeros(i).astype(int)
        W = i

        end_time_recursive = time.time()
        item_count = knapsack_recursive(W)
        print("Recursive Approach Results\n")
        print("For maximum bag capacity of ", W, " item count is ", item_count)
        times_recursive.append(end_time_recursive)

        selections.clear()  # in order to clear the list (otherwise the program needs another list to be created)

        end_time_dynamic = time.time()
        item_count = knapsack_dynamic(W, dynamic_table)
        print("Dynamic Approach Results\n")
        print("For maximum bag capacity of ", W, " item count is ", item_count)
        times_dynamic.append(end_time_dynamic)
        
    plot_time()


def rand_size(count):  # generates unique bag capacities in the interval selected and sorts them to see runtimes better
    for i in range(count):
        to_append = random.randint(5, 50)
        if to_append not in bag_capacities:
            bag_capacities.append(to_append)
    return bag_capacities.sort()  # sorted in order to see runtimes better


def knapsack_recursive(W):
    if W <= 0:
        return 0
    else:
        return 1 + min(
            knapsack_recursive(W - wt[0]),
            knapsack_recursive(W - wt[1]),
            knapsack_recursive(W - wt[2]),
        )


def knapsack_dynamic(W, dynamic_table):
    if W <= 0:
        return 0
    else:    
        if dynamic_table[W - 1] == 0:
            dynamic_table[W - 1] = 1 + min(
                knapsack_dynamic(W - wt[0], dynamic_table),
                knapsack_dynamic(W - wt[1], dynamic_table),
                knapsack_dynamic(W - wt[2], dynamic_table),
            )
            return dynamic_table[W - 1]
        else:
            return dynamic_table[W - 1]


def plot_time():
    plt.title("Run Times Comparison")
    plt.xlabel("knapsack weight capacities selected")
    plt.ylabel("run times in millis")

    plt.plot(bag_capacities, times_recursive, color="g", label="Recursive Approach")
    plt.plot(bag_capacities, times_dynamic, color="r", label="Dynamic Approach")

    plt.show()


def main():
    flow()


if __name__ == "__main__":
    main()
