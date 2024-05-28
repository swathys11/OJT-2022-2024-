import statistics

numbers = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8, 9, 10]
mean = statistics.mean(numbers)
print("Mean:", mean)

median = statistics.median(numbers)
print("Median:", median)

mode = statistics.mode(numbers)
print("Mode:", mode)