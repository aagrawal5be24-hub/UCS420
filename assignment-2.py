#ASSIGNMENT 2

#question 1

roll_no = "1024170052"

L = [int(digit) * 10 for digit in roll_no]

print("Original L:", L)

L.append(30)
print("After append(30):", L)

L.insert(2, 60)
print("After insert(2, 60):", L)

L.remove(0)
print("After remove(0):", L)

L.pop()
print("After pop():", L)

L.sort()
print("Ascending order:", L)

L.sort(reverse=True)
print("Descending order:", L)

print("First three elements:", L[:3])
print("Last three elements:", L[-3:])

average = sum(L) / len(L)

new_list = [x for x in L if x > average]

print("Average:", average)
print("Elements greater than average:", new_list)

#question 2

L = [70, 60, 50, 40, 20, 20, 10, 10, 0, 0]

scores = tuple(L[:8])

print("Scores:", scores)

highest = max(scores)
highest_index = scores.index(highest)

lowest = min(scores)
lowest_count = scores.count(lowest)

print("Highest score:", highest)
print("Index of highest score:", highest_index)
print("Lowest score:", lowest)
print("Number of times lowest appears:", lowest_count)

reversed_scores = list(reversed(scores))
print("Reversed tuple as list:", reversed_scores)

user_score = int(input("Enter a score: "))

if user_score in scores:
    print("First occurrence index:", scores.index(user_score))
else:
    print("Score not present")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

first, second, *remaining = scores

print("First score:", first)
print("Second score:", second)
print("Remaining scores:", remaining)

#question 3

import random

random.seed(1024170052)

numbers = [random.randint(100, 900) for i in range(100)]

print("Random numbers:", numbers)

odd_numbers = [x for x in numbers if x % 2 != 0]
print("Odd numbers:", odd_numbers)
print("Count of odd numbers:", len(odd_numbers))

even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)
print("Count of even numbers:", len(even_numbers))

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

prime_numbers = [x for x in numbers if is_prime(x)]

print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", len(prime_numbers))

most_frequent = max(set(numbers), key=numbers.count)
frequency = numbers.count(most_frequent)

print("Most frequent number:", most_frequent)
print("Number of occurrences:", frequency)

#question 4

digits = [1, 0, 2, 4, 1, 7, 0, 0, 5, 2]

A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("Set A:", A)
print("Set B:", B)

union = A.union(B)
print("Union:", union)

intersection = A.intersection(B)
print("Intersection:", intersection)

A_difference_B = A.difference(B)
B_difference_A = B.difference(A)

print("A - B:", A_difference_B)
print("B - A:", B_difference_A)

symmetric_difference = A.symmetric_difference(B)
print("Symmetric Difference:", symmetric_difference)

print("A is subset of B:", A.issubset(B))
print("B is superset of A:", B.issuperset(A))

X = int(input("Enter a value to remove from A: "))

A.discard(X)
print("Set A after discard:", A)

#question 5

my_dict = {
    "name": "Abhi Agrawal",
    "roll_no": "1024170052",
    "branch": "CSE",
    "age": 20,
    "city": "Delhi"
}

my_dict["location"] = my_dict.pop("city")
print(my_dict)

my_dict["cgpa"] = 8.5
print(my_dict)

my_dict["age"] = my_dict["age"] + 1
print(my_dict)

dict1 = my_dict.copy()
dict1.pop("branch")
print(dict1)

dict2 = my_dict.copy()
del dict2["branch"]
print(dict2)

for key, value in my_dict.items():
    print(key, "→", value)

if "email" in my_dict:
    print(my_dict["email"])
else:
    print("Email not found")

friend_dict = {
    "name": "Rahul Sharma",
    "roll_no": "1024170060",
    "branch": "CSE",
    "age": 20,
    "city": "Mumbai"
}

merged = {**my_dict, **friend_dict}
print(merged)

string_dict = {}

for key, value in my_dict.items():
    if isinstance(value, str):
        string_dict[key] = value

print(string_dict)
