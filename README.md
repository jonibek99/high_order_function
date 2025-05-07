📘 Homework: High-Order Functions (min, max, map, filter, lambda)
🔹 1. min() Tasks
1.1 Find the smallest number in the list.
Input: [3, 1, 4, 2]
Output: 1

1.2 Find the shortest word.
Input: ["apple", "banana", "kiwi", "pear"]
Output: "kiwi"

1.3 Find the string with the smallest number of vowels.
Input: ["book", "sky", "quiet", "data"]
Output: "sky"
(Hint: Use key=lambda word: count_vowels(word))

1.4 Find the dictionary with the smallest value.
Input: [{'a': 5}, {'a': 3}, {'a': 7}]
Output: {'a': 3}
(Hint: key=lambda d: d['a'])

1.5 Find the tuple with the smallest second element.
Input: [(1, 3), (2, 2), (3, 1)]
Output: (3, 1)

🔹 2. max() Tasks
2.1 Find the largest number in the list.
Input: [7, 4, 9, 1]
Output: 9

2.2 Find the longest word.
Input: ["pen", "notebook", "eraser"]
Output: "notebook"

2.3 Find the name with the highest number of letters.
Input: ["Ann", "Robert", "Charlotte", "Mike"]
Output: "Charlotte"

2.4 Find the word with the most vowels.
Input: ["tree", "education", "sky", "road"]
Output: "education"

2.5 Find the person with the highest age.
Input: [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Tom", "age": 28}]
Output: {"name": "Bob", "age": 45}

🔹 3. map() Tasks
3.1 Add 10 to each number.
Input: [1, 2, 3]
Output: [11, 12, 13]

3.2 Convert all words to uppercase.
Input: ["cat", "dog", "fish"]
Output: ["CAT", "DOG", "FISH"]

3.3 Get the lengths of each word.
Input: ["hi", "hello", "bye"]
Output: [2, 5, 3]

3.4 Square each number.
Input: [1, 4, 5]
Output: [1, 16, 25]

3.5 Extract names from a list of dictionaries.
Input: [{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}]
Output: ["Alice", "Bob", "Carol"]

🔹 4. filter() Tasks
4.1 Filter out even numbers.
Input: [1, 2, 3, 4, 5]
Output: [1, 3, 5]

4.2 Keep words longer than 4 letters.
Input: ["hi", "hello", "world", "cat"]
Output: ["hello", "world"]

4.3 Keep numbers greater than 10.
Input: [5, 11, 20, 7, 10]
Output: [11, 20]

4.4 Filter names that start with "A".
Input: ["Alice", "Bob", "Anna", "Charlie"]
Output: ["Alice", "Anna"]

4.5 Keep words that contain the letter "e".
Input: ["dog", "elephant", "cat", "eagle"]
Output: ["elephant", "eagle"]

🔹 5. lambda Function Tasks
5.1 Use lambda to square a number.
Input: lambda x: x**2, input 5
Output: 25

5.2 Use lambda to return the last character of a string.
Input: lambda s: s[-1], input "apple"
Output: "e"

5.3 Sort a list of strings by their length using lambda.
Input: ["apple", "kiwi", "banana"]
Output: ["kiwi", "apple", "banana"]

5.4 Sort a list of tuples by the second value using lambda.
Input: [(1, 3), (2, 1), (3, 2)]
Output: [(2, 1), (3, 2), (1, 3)]

5.5 Use lambda to check if a number is even.
Input: lambda x: x % 2 == 0, input 4
Output: True