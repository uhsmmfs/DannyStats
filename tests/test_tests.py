from dannystats import tests
import numpy

sample = numpy.random.normal(0, 1, 1000)

tests.test_normality(sample)