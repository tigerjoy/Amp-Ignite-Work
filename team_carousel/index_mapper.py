import sys

def map_index_to_number(index):
    if index < 0:
        raise ValueError("Index cannot be negative")
    
    index = index % 517189516

    # Define the start points and counts for each positive range
    positive_ranges = [
        (2 * (10 ** 1), (10 ** 1)),                 # Two-digit: 20-29 (10 numbers)
        (2 * (10 ** 2), (10 ** 2)),               # Three-digit: 200-299 (100 numbers)
        (2 * (10 ** 3), (10 ** 3)),             # Four-digit: 2000-2999 (1000 numbers)
        (2 * (10 ** 4), (10 ** 4)),           # Five-digit: 20000-29999 (10,000 numbers)
        (2 * (10 ** 5), (10 ** 5)),         # Six-digit: 200000-299999 (1,00,000 numbers)
        (2 * (10 ** 6), (10 ** 6)),       # Seven-digit: 2000000-2999999 (1000000 numbers)
        (2 * (10 ** 7), (10 ** 7)),     # Eight-digit: 20000000-29999999 (10000000 numbers)
        (2 * (10 ** 8), (10 ** 8)),   # Nine-digit: 200000000-299999999 (100000000 numbers)
        (2 * (10 ** 9), 147483648)   # Ten-digit: 2000000000-2147483647 (147483647 numbers)
    ]

    total_positive_numbers = sum(count for _, count in positive_ranges)
    # print("total_positive_numbers:", total_positive_numbers)

    if index < total_positive_numbers:
        # Map within the original positive ranges
        for start, count in positive_ranges:
            if index < count:
                return start + index
            index -= count
    else:
        # Map beyond the positive numbers to negative numbers starting with -2
        negative_index = (index - total_positive_numbers) % total_positive_numbers
        print("negative_index:", negative_index)
        for start, count in positive_ranges[::-1]:
            if negative_index < count:
                return -(start + count - negative_index)
            negative_index -= count

    raise ValueError("Index out of range")

# Example usage:
# test_indices = [
#     0, 9, 10, 109, 110, 1109, 1110, 111109, 111110, 258594757, 258594758, 
#     258594759, 258594760, 258594758 + 1, 258594758 + 147483648, 
#     258594758 + 258594758
# ]

# for i in test_indices:
#     print(f"Index {i} maps to number {map_index_to_number(i)}")

# Test the above code
index_start = 0
index_end = 9
result_start = 20
result_end = 29

power_of_10 = 10

counter = 0

while index_end != 111111109:
    for index in range(index_start, index_end + 1):
        i = index - index_start
        mapped_value = map_index_to_number(index)
        if mapped_value != (result_start + i) or not (result_start <= mapped_value <= result_end):
            print("index:", index)
            print("i:", i)
            print("result_start:", result_start)
            print("result_start + i:", result_start + i)
            print("result_end:", result_end)
            print("mapped_value:", mapped_value)
            print("counter: ", counter)
            sys.exit()
        counter += 1
    
    power_of_10 *= 10
    index_start = index_end + 1
    index_end = power_of_10 + index_end
    
    result_start *= 10
    result_end = (result_end * 10) + 9

for index in range(index_start, 258594758):
    i = index - index_start
    mapped_value = map_index_to_number(index)
    if mapped_value != (result_start + i) or not (result_start <= mapped_value <= result_end):
        print("index:", index)
        print("i:", i)
        print("result_start:", result_start)
        print("result_start + i:", result_start + i)
        print("result_end:", result_end)
        print("mapped_value:", mapped_value)
        print("counter: ", counter)
        sys.exit()
    counter += 1

print("counter: ", counter)