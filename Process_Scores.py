"""
Problem: Process Scores (process_scores)
Write a Python function named process_scores(scores) that takes a list of integers scores and uses
a while loop to process elements from left to right.

Rules:
1. Iterate through scores using a while loop (do not use a for loop).
2. Stop processing immediately if you encounter a negative number (< 0) or reach the end of the list.
3. For each valid non-negative number before stopping:
    If it is even, add it to a running sum even_sum.
    If it is odd, append it to a new list odd_numbers.
4. Return a tuple formatted as (even_sum, odd_numbers).
"""