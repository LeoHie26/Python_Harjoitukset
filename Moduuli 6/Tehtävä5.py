
og_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

def filter_even_numbers(numbers):
    result = []
    for num in numbers:

        if num % 2 == 0:
            result.append(num)
    return result

even_list = filter_even_numbers(og_list)



print(f"Original list: {og_list}")
print(f"List with even numbers only: {even_list}")
