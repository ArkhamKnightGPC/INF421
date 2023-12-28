nim compile --hints:off code/Individual.nim
nim compile --hints:off code/BenchmarkFunctions.nim
nim compile --hints:off code/EA.nim

nim compile --run --verbosity:0 --hints:off code/tests/TestIndividual.nim

nim compile --run --verbosity:0 --hints:off code/tests/TestBenchmarkFunctions.nim