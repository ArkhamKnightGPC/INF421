import Individual

import std/random

proc generateRandomOffspring(x: Individual, p: float): Individual =
    #[ generate copy of x flipping each bit independently with probability p ]#
    let n = x.size
    let y = newIndividual(n)
    for idx in countup(0, n-1):
        var xi = get(x, idx)
        let randVar = rand(1.0)
        if (xi == 0 and randVar < p) or (xi == 1 and randVar >= p):
            set(y, idx)
    return y

proc EvolutionaryAlgorithm*(f: proc (x: Individual): int, n: int): Individual =
    #[ (1+1) Evolutionary Algorithm ]#

    # Call randomize() once to initialize the default random number generator.
    # If this is not called, the same results will occur every time these
    # examples are run.
    randomize()

    var t = 0
    var Pt = generateRandomOffspring(newIndividual(n), 0.5) #random initial solution
    
    while t < 100:

        let y = generateRandomOffspring(Pt, 1/n)
        var Qt: array[2, Individual]

        if(f(y) < f(Pt)): #we sort population and offspring with respect to f
            Qt = [y, Pt]
        else:
            Qt = [Pt, y]

        t += 1
        Pt = Qt[1] #we pick solution in population that maximises f
    return Pt