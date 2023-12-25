import heapq


def merge_k_sorted_arrays(k_arrays, k):
    min_heap = []

    for i in range(k):
        if k_arrays[i]:
            heapq.heappush(min_heap, (k_arrays[i][0], i, 0))

    result = []
    while min_heap:
        min_element, list_number, indx = heapq.heappop(min_heap)
        result.append(min_element)

        if indx < len(k_arrays[list_number]) - 1:
            heapq.heappush(
                min_heap, (k_arrays[list_number][indx + 1], list_number, indx + 1)
            )

    return result


k_arrays_example = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]

k_example = 3
result_example = merge_k_sorted_arrays(k_arrays_example, k_example)
print(result_example)
