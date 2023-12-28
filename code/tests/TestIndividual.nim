import ../Individual

import unittest

suite "test flip operation":

    setup:
        let test = newIndividual(96) #solution represented by array of 3 integers

    test "flip bit in first block":
        flip(test, 3)
        let t = get(test, 3)
        check: t == 1

    test "flip bit in middle block":
        flip(test, 42)
        let t1 = get(test, 42)
        flip(test, 42)
        let t2 = get(test, 42)
        check:
            t1 == 1
            t2 == 0

    test "flip bit in last block":
        flip(test, 90)
        let t = get(test, 90)
        check: t == 1

suite "test set/reset operations":
    setup:
        let test = newIndividual(128) #solution represented by array of 4 integers

    test "set and reset several bits":
        set(test, 3)
        set(test, 41)
        set(test, 94)
        set(test, 100)
        set(test, 111)
        reset(test, 41)
        reset(test, 100)

        let t1 = get(test, 3)
        let t2 = get(test, 41)
        let t3 = get(test, 94)
        let t4 = get(test, 100)
        let t5 = get(test, 111)
        check:
            t1 == 1
            t2 == 0
            t3 == 1
            t4 == 0
            t5 == 1

suite "test count operation":
    setup:
        let test = newIndividual(160)#solution represented by array of 5 integers

    test "test count 1":
        set(test, 3)
        set(test, 41)
        set(test, 94)
        set(test, 100)
        set(test, 111)
        set(test, 150)

        let t = count(test)

        check: t == 6

    test "test count 2":
        set(test, 33)
        set(test, 94)
        set(test, 142)
        set(test, 153)

        let t = count(test)

        check: t == 4
