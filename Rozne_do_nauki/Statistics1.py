from statistics import mean
from statistics import median
from statistics import mode
from statistics import variance

l = [1,2,2,3,5,9,1,5,5,4]
# srednia arytmetyczna
mean = mean(l)

# mediana
median = median(l)

# dominanta
mode = mode(l)

# wariancja
variance = variance(l)

print(mean, median, mode, variance)