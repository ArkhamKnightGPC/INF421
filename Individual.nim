# Individual data type

type
    Individual* = object
        #[ represents candidate solutions x = (x1, ..., xn) ]#
        size*: int
        bits*: int

proc get*(individual: Individual, idx: int): int =
    #[ get bit at index idx ]#
    return

proc set*(individual: Individual, idx: int): void =
    #[ set bit at index idx to 1 ]#
    return

proc reset*(individual: Individual, idx: int): void =
    #[ set bit at index idx to 0 ]#
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
    for i in countup(1, individual.size):
        let bitI = get(individual, i)
        result += bitI
    return result