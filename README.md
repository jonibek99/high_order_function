# 📘 Homework: High-Order Functions

## Table of Contents
- [1. min() Tasks](#1-min-tasks)
- [2. max() Tasks](#2-max-tasks)
- [3. map() Tasks](#3-map-tasks)
- [4. filter() Tasks](#4-filter-tasks)
- [5. lambda Functions](#5-lambda-functions)

## 1. min() Tasks

| Task | Description | Input | Output |
|------|-------------|-------|--------|
| 1.1  | Find the smallest number in the list | `[3, 1, 4, 2]` | `1` |
| 1.2  | Find the shortest word | `["apple", "banana", "kiwi", "pear"]` | `"kiwi"` |
| 1.3  | Find the string with the smallest number of vowels | `["book", "sky", "quiet", "data"]` | `"sky"` <br> (Hint: Use `key=lambda word: count_vowels(word)`) |
| 1.4  | Find the dictionary with the smallest value | `[{'a': 5}, {'a': 3}, {'a': 7}]` | `{'a': 3}` <br> (Hint: `key=lambda d: d['a']`) |
| 1.5  | Find the tuple with the smallest second element | `[(1, 3), (2, 2), (3, 1)]` | `(3, 1)` |

## 2. max() Tasks

| Task | Description | Input | Output |
|------|-------------|-------|--------|
| 2.1  | Find the largest number in the list | `[7, 4, 9, 1]` | `9` |
| 2.2  | Find the longest word | `["pen", "notebook", "eraser"]` | `"notebook"` |
| 2.3  | Find the name with the highest number of letters | `["Ann", "Robert", "Charlotte", "Mike"]` | `"Charlotte"` |
| 2.4  | Find the word with the most vowels | `["tree", "education", "sky", "road"]` | `"education"` |
| 2.5  | Find the person with the highest age | `[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 45}, {"name": "Tom", "age": 28}]` | `{"name": "Bob", "age": 45}` |

## 3. map() Tasks

| Task | Description | Input | Output |
|------|-------------|-------|--------|
| 3.1  | Add 10 to each number | `[1, 2, 3]` | `[11, 12, 13]` |
| 3.2  | Convert all words to uppercase | `["cat", "dog", "fish"]` | `["CAT", "DOG", "FISH"]` |
| 3.3  | Get the lengths of each word | `["hi", "hello", "bye"]` | `[2, 5, 3]` |
| 3.4  | Square each number | `[1, 4, 5]` | `[1, 16, 25]` |
| 3.5  | Extract names from a list of dictionaries | `[{"name": "Alice"}, {"name": "Bob"}, {"name": "Carol"}]` | `["Alice", "Bob", "Carol"]` |

## 4. filter() Tasks

| Task | Description | Input | Output |
|------|-------------|-------|--------|
| 4.1  | Filter out even numbers | `[1, 2, 3, 4, 5]` | `[1, 3, 5]` |
| 4.2  | Keep words longer than 4 letters | `["hi", "hello", "world", "cat"]` | `["hello", "world"]` |
| 4.3  | Keep numbers greater than 10 | `[5, 11, 20, 7, 10]` | `[11, 20]` |
| 4.4  | Filter names that start with "A" | `["Alice", "Bob", "Anna", "Charlie"]` | `["Alice", "Anna"]` |
| 4.5  | Keep words that contain the letter "e" | `["dog", "elephant", "cat", "eagle"]` | `["elephant", "eagle"]` |

## 5. lambda Functions

| Task | Description | Input | Output |
|------|-------------|-------|--------|
| 5.1  | Use lambda to square a number | `lambda x: x**2, input 5` | `25` |
| 5.2  | Use lambda to return the last character of a string | `lambda s: s[-1], input "apple"` | `"e"` |
| 5.3  | Sort a list of strings by their length using lambda | `["apple", "kiwi", "banana"]` | `["kiwi", "apple", "banana"]` |
| 5.4  | Sort a list of tuples by the second value using lambda | `[(1, 3), (2, 1), (3, 2)]` | `[(2, 1), (3, 2), (1, 3)]` |
| 5.5  | Use lambda to check if a number is even | `lambda x: x % 2 == 0, input 4` | `True` |