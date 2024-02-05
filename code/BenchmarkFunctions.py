from Individual import Individual

def OneMax(individual):
    """
    Returns the number of 1s of the input
    """
    return individual.count()

def LeadingOnes(individual):
    """
    Returns the length of the longest consecutive prefix of 1s
    """
    n = individual.size
    result = 0
    for i in range(n):
        prefix_product = 1
        for j in range(0, i + 1):
            prefix_product *= individual.get(j)
        result += prefix_product
    return result

def JumpK(individual, k):
    """
    Analog to OneMax but penalizes individuals with a number of ones in n-k+1,...,n-1
    """
    n = individual.size
    one_max_x = OneMax(individual)
    if one_max_x <= n - k or one_max_x == n:
        return k + one_max_x
    return n - one_max_x
