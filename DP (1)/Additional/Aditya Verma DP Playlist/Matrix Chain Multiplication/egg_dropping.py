def eggDropRecursive(eggs, floors):
    if floors <= 1:
        return floors
    if eggs == 1:
        return floors

    result = float("inf")
    for currentFloor in range(1, floors + 1):
        movesForUnbrokenEggs = eggDropRecursive(eggs, floors - currentFloor)
        movesForBrokenEggs = eggDropRecursive(eggs - 1, currentFloor - 1)
        worstCase = 1 + max(movesForUnbrokenEggs, movesForBrokenEggs)
        result = min(result, worstCase)
    return result


def eggDrop(eggs, floors, dp):
    if floors <= 1:
        return floors
    if eggs == 1:
        return floors

    if dp[eggs][floors] != -1:
        return dp[eggs][floors]

    result = float("inf")
    for currentFloor in range(1, floors + 1):
        movesForUnbrokenEggs = eggDrop(eggs, floors - currentFloor, dp)
        movesForBrokenEggs = eggDrop(eggs - 1, currentFloor - 1, dp)
        worstCase = 1 + max(movesForUnbrokenEggs, movesForBrokenEggs)
        result = min(result, worstCase)
    dp[eggs][floors] = result
    return dp[eggs][floors]


def eggDropOptimize(eggs, floors, dp):
    if floors <= 1:
        return floors
    if eggs == 1:
        return floors

    if dp[eggs][floors] != -1:
        return dp[eggs][floors]

    result = float("inf")
    for currentFloor in range(1, floors + 1):
        if dp[eggs][floors - currentFloor] != -1:
            movesForUnbrokenEggs = dp[eggs][floors - currentFloor]
        else:
            movesForUnbrokenEggs = eggDropOptimize(eggs, floors - currentFloor, dp)

        if dp[eggs - 1][currentFloor - 1] != -1:
            movesForBrokenEggs = dp[eggs - 1][currentFloor - 1]
        else:
            movesForBrokenEggs = eggDropOptimize(eggs - 1, currentFloor - 1, dp)
        worstCase = 1 + max(movesForUnbrokenEggs, movesForBrokenEggs)
        result = min(result, worstCase)
    dp[eggs][floors] = result
    return dp[eggs][floors]


if __name__ == "__main__":
    floors = 6
    eggs = 2
    print(eggDropRecursive(eggs, floors))
    dp = [[-1 for _ in range(floors + 1)] for _ in range(eggs + 1)]
    print(eggDrop(eggs, floors, dp))
    print(eggDropOptimize(eggs, floors, dp))
