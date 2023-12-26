import Individual

# Benchmark functions

proc OneMax(individual: Individual): int =
    #[ returns the number of 1s of the input ]#
    return count(individual)

proc LeadingOnes(individual: Individual): int =
    #[ returns the length of the longest consecutive prefix of 1s ]#
    let n = individual.size
    result = 0
    for i in countup(1, n):
        var prefixProduct = 1
        for j in countup(1, i):
            prefixProduct = prefixProduct*get(individual, j)
        result += prefixProduct
    return result

const k = 50 #we set k value as a constant
proc JumpK(individual: Individual): int =
    #[ analog to OneMax but penalises individuals with number of ones in n-k+1,...,n-1 ]#
    let n = individual.size
    let OneMax_x = OneMax(individual)
    if OneMax_x <= n - k or OneMax_x == n:
        return k + OneMax_x
    return n - OneMax_x