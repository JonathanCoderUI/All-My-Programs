# ### **Problem: Sum Until Duplicate (** **sum\_until\_duplicate** **)**

# Write a Python function named **sum\_until\_duplicate(numbers)** that takes a list of integers `numbers` and processes them from left to right using a **while** **loop**.

# #### **Rules:**

# 1. Iterate through `numbers` using a **while** **loop** (do not use a `for` loop).
# 2. Keep a running sum of the numbers processed.
# 3. Stop the loop immediately if you encounter a number that is **identical to the number immediately before it** (an adjacent duplicate).
# 4. Return the total sum of all numbers processed **before** the duplicate was encountered (do not add the second duplicate number to the sum).

def sum_until_duplicate(numbers):

    i = 1
    final_number = numbers[0]

    while i < len(numbers):

        if numbers[i] == numbers[i-1]:
            break

        final_number += numbers[i]

        i += 1

    return final_number

print(sum_until_duplicate([3, 5, 2, 2, 8]))
print(sum_until_duplicate([1, 4, 6]))
print(sum_until_duplicate([7, 7, 3]))