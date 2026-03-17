
def permutation_with_backtracking(X, result, path, used):
    if len(path) == len(X):
        result.append(path.copy()) 
        return 
    
    for i, x in enumerate(X):
        if used[i] == False:
            path.append(x)
            used[i] = True
            
            permutation_with_backtracking(X, result, path, used)
            
            used[i] = False
            path.pop()

X = [1, 2, 3]
result = []
path = []
used = [False] * len(X)

permutation_with_backtracking(X, result, path, used)
print(result)
    