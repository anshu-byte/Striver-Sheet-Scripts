# Top - Down
def recursiveKnapsack(weights, values, capacity, n):
    # no item left or capacity is 0
    if n == 0 or capacity == 0:
        return 0

    # If the weight of the nth item is more than the capacity, it cannot be included
    if weights[n - 1] > capacity:
        return recursiveKnapsack(weights, values, capacity, n - 1)
    else:
        # Return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        return max(
            values[n - 1]
            + recursiveKnapsack(weights, values, capacity - weights[n - 1], n - 1),
            recursiveKnapsack(weights, values, capacity, n - 1),
        )


# Bottom - Up
def recursiveKnapsack2(weights, values, capacity, index):
    if index == len(weights) or capacity == 0:
        return 0

    # If the weight of the index th item is more than the capacity, it cannot be included
    if weights[index] > capacity:
        return recursiveKnapsack2(weights, values, capacity, index + 1)
    else:
        # Return the maximum of two cases:
        # (1) index th item included
        # (2) not included

        return max(
            values[index]
            + recursiveKnapsack2(weights, values, capacity - weights[index], index + 1),
            recursiveKnapsack2(weights, values, capacity, index + 1),
        )


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
n = len(weights)

max_value = recursiveKnapsack(weights, values, capacity, n)
print(f"The maximum value that can be obtained is: {max_value}")

max_value = recursiveKnapsack2(weights, values, capacity, 0)
print(f"The maximum value that can be obtained is: {max_value}")
