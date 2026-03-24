import itertools
import time
# X = [1,2,3,4]
# X_per = itertools.permutations(X)
# print([per for per in X_per])

#Brute Force
cost = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]
def find_visited(cost):

    cities = list(range(len(cost)))

    permutation_cities = itertools.permutations(cities[1:])
    permutation_cities = [[cities[0]] + list(per) + [cities[0]] for per in permutation_cities]

    min_resolve = 9999

    for per in permutation_cities:

        cost_visit = 0

        for i in range(len(per[:-1])):

            cost_visit += cost[per[i]][per[i+1]]

        min_resolve = min(min_resolve, cost_visit)
        
    return min_resolve

print(find_visited(cost))

#Optimal solution
#20 điểm:
cost_ = cost + cost + cost + cost
start = time.time()
print(find_visited(cost_))
print(time.time()-start)
