# Individual data type

type
    Individual* = ref object
        #[ represents candidate solutions x = (x1, ..., xn) ]#
        size*: int
        bits*: seq[int]

proc newIndividual*(size: int): Individual =
    #[ constructor for new Individual ]#

    #number of integers necessary to represent all xi's
    let necessaryIntegers = (size + 31) div 32

    result = new(Individual)
    result.size = size
    result.bits = newSeq[int](necessaryIntegers)

    return result

proc get*(individual: Individual, idx: int): int =
    #[ get bit at index idx ]#
    let testBit = individual.bits[idx div 32] and (1 shl (idx mod 32))

    if testBit > 0:
        return 1
    else:
        return 0

proc set*(individual: Individual, idx: int): void =
    #[ set bit at index idx to 1 ]#
    individual.bits[idx div 32] = individual.bits[idx div 32] or (1 shl (idx mod 32)) 
    return

proc reset*(individual: Individual, idx: int): void =
    #[ set bit at index idx to 0 ]#
    individual.bits[idx div 32] = individual.bits[idx div 32] and not (1 shl (idx mod 32))
    return

proc flip*(individual: Individual, idx: int): void =
    #[ flip bit at index idx ]#
    let bitI = get(individual, idx)
    if bitI == 0:
        set(individual, idx)
    else:
        reset(individual, idx)
    return

proc count*(individual: Individual): int =
    #[ count number of bits equal to 1 ]#
    result = 0
    for i in countup(0, individual.size - 1):
        let bitI = get(individual, i)
        result += bitI
    return result