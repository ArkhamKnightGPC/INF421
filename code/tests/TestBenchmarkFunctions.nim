import ../Individual
import ../BenchmarkFunctions

import unittest

suite "Test OneMax function":
    setup:
        let test = newIndividual(64)
    
    test "test OneMax 1":
        for i in countup(1, 10):
            set(test, 5*i)
        let t = OneMax(test)
        check: t == 10

    test "test OneMax 2":
        for i in countup(1, 20):
            set(test, 3*i)
        let t = OneMax(test)
        check: t == 20

suite "Test LeadingOnes function":
    setup:
        let test = newIndividual(64)
    
    test "test LeadingOnes 1":
        for i in countup(0, 10):
            set(test, i)
        let t = LeadingOnes(test)
        check: t == 11

    test "test LeadingOnes 2":
        for i in countup(0, 63):
            set(test, i)
        reset(test, 30)

        let t = LeadingOnes(test)
        check: t == 30

suite "Test Jump_k function":
    setup:
        let test = newIndividual(64)
    
    test "test Jump_k 1":
        for i in countup(0, 63):
            set(test, i)
        let t = JumpK(test, 6)
        check: t == 70 # k + 64

    test "test Jump_k 2":
        for i in countup(0, 40):
            set(test, i)

        let t = JumpK(test, 24)
        check: t == 23 #returns n - OneMax(test)