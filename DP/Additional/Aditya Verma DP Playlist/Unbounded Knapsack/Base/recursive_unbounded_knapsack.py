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
        # (1) nth item in process
        # (2) not included
        return max(
            values[n - 1]
            + recursiveKnapsack(weights, values, capacity - weights[n - 1], n),
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
        # (1) index th item in process
        # (2) not included

        return max(
            values[index]
            + recursiveKnapsack2(weights, values, capacity - weights[index], index),
            recursiveKnapsack2(weights, values, capacity, index + 1),
        )


if __name__ == "__main__":
    weights = [5, 10, 15]
    values = [10, 30, 20]
    capacity = 100
    n = len(weights)
    max_value = recursiveKnapsack(weights, values, capacity, n)
    print(f"The maximum value that can be obtained is: {max_value}")

    max_value = recursiveKnapsack2(weights, values, capacity, 0)
    print(f"The maximum value that can be obtained is: {max_value}")
