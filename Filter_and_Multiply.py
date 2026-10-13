"""
### **Problem: Filter and Multiply (** **process_sequence** **)**

Write a Python function named **process_sequence(numbers)** that takes a list of integers and performs two steps:

#### **Step 1: Clean the List (using a** **while** **loop)**

* Iterate through `numbers` using a **while** **loop**.
* Stop processing immediately if you encounter a negative number (`&lt; 0`).
* Collect all non-negative numbers before the negative number into a new list called `clean_list`.

#### **Step 2: Transform the Clean List (using a** **for** **loop)**

* Iterate through `clean_list` using a **for** **loop** with `enumerate()` or `range()`.
* If the index is **even** (0, 2, 4...), add the number to a running total `even_indexed_sum`.
* If the index is **odd** (1, 3, 5...), multiply the number into a running product `odd_indexed_product` (start this product at `1`).
* Return a tuple: `(even_indexed_sum, odd_indexed_product)`.
"""

def process_sequence(numbers):

    clean_list = []
    i = 0

    while i < len(numbers):

        if numbers[i] < 0:
            break

        clean_list.append(numbers[i])

        i += 1

    even_indexed_sum = 0
    odd_indeced_product = 1

    for idx in range(len(clean_list)):
        num = clean_list[idx]

        if idx % 2 == 0:
            even_indexed_sum += num

        elif idx % 2 == 1:
            odd_indeced_product *= num

    return (even_indexed_sum, odd_indeced_product)

print(process_sequence([2, 3, 4, 5, -1, 8, 10]))