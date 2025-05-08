# Bubble Sort for Python Lists and Linked Lists

## 📌 Project Description
This project implements bubble sort that works both on regular Python lists and a custom linked list class. It includes unit tests and GitHub Actions integration for continuous testing.

## 🔄 Why `__iter__` is used?
We implemented the `__iter__` method in the LinkedList class to allow iteration using `for` loops and to convert the linked list to a Python list using `list()`. This makes testing and sorting easier.

## ⚠ Error vs Failure in Unit Testing
- **Error**: A problem that prevents the test from running (e.g., typo, wrong method call).
  - *Example*: Calling a method that doesn’t exist → `AttributeError`.
- **Failure**: The test runs but the output does not match the expected result.
  - *Example*: Sorting returns `[3, 2, 1]` but expected `[1, 2, 3]`.

## 🤖 Did you use AI?
Yes. I used AI tools to guide implementation and debugging, especially for test design and iteration logic.

## ✅ Unit Tests
- Works with Python lists
- Works with custom LinkedLists
- Handles edge cases: empty list, single element, negative numbers
