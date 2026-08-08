# 🐍 Python & Data Analytics Practice

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented%20Programming-6f42c1?style=for-the-badge)
![Practice](https://img.shields.io/badge/Practice-Data%20%26%20Programming-F7DF1E?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github\&logoColor=white)

> A hands-on repository for revising **Python programming, Object-Oriented Programming, data structures, and NumPy fundamentals**, with a focus on practical coding and technical interview preparation.

---

## 📌 About This Repository

This repository contains small, focused Python programs created while learning and revising important programming concepts.

The current practice progression covers:

```text
🐍 Python Basics
      ↓
🔧 Functions
      ↓
📦 Lists & Tuples
      ↓
🔢 Sets
      ↓
🏗️ Classes & Objects
      ↓
🧬 Inheritance
      ↓
💎 Diamond Inheritance
      ↓
🔬 NumPy Basics
      ↓
🎯 Advanced Indexing
```

The repository is useful for building a strong foundation before moving into:

* 📊 Data Analytics
* 🤖 Machine Learning
* 🧠 Data Science
* 💻 Software Development
* 🧩 DSA
* 🎯 Technical Interviews

---

# 📚 Topics Covered

## 🐍 1. Python Basics

Fundamental Python programming concepts including:

* Variables
* Data types
* Input / Output
* Operators
* Conditional statements
* Loops
* Functions
* Basic problem solving

---

## 🔧 2. Functions

Practice with Python functions:

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Concepts include:

* Function declaration
* Parameters
* Arguments
* Return values
* Reusable functions
* Basic function-based problem solving

---

## 📦 3. Lists & Tuples

Python's commonly used collection types.

### Lists

```python
numbers = [10, 20, 30, 40]
```

Practice includes:

* Creating lists
* Indexing
* Slicing
* Updating elements
* Iterating
* Common list operations

### Tuples

```python
data = (10, 20, 30)
```

Key concept:

> Lists are mutable, while tuples are immutable.

---

## 🔢 4. Set Operations

Practice with Python sets:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

Important operations:

```text
Union
Intersection
Difference
Symmetric Difference
Membership
```

Example:

```python
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
```

---

# 🏗️ 5. Classes & Objects

Introduction to Object-Oriented Programming in Python.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)
```

Core concepts:

* Classes
* Objects
* Attributes
* Methods
* Constructors
* `self`
* Encapsulation

---

# 🧬 6. Inheritance

Practice inheritance using Python classes.

```text
Parent Class
     │
     ↓
Child Class
```

Example:

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")
```

Important concepts:

* Parent class
* Child class
* Method inheritance
* Method overriding
* Code reuse

---

# 💎 7. Diamond Inheritance

Diamond inheritance occurs when a class inherits from two classes that ultimately originate from the same base class.

```text
        A
       / \
      B   C
       \ /
        D
```

Python handles this using **Method Resolution Order (MRO)**.

You can inspect MRO using:

```python
print(D.mro())
```

or:

```python
print(D.__mro__)
```

This is an important concept when studying multiple inheritance in Python.

---

# 🔬 8. NumPy Basics

NumPy is one of the most important Python libraries for numerical and data-oriented programming.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

Topics include:

* NumPy arrays
* Array creation
* Dimensions
* Shape
* Data types
* Array operations
* Reshaping
* Mathematical operations

---

# 🎯 9. Advanced Indexing

Practice selecting and manipulating NumPy data using advanced indexing techniques.

Examples include:

### Boolean Indexing

```python
arr[arr > 10]
```

### Fancy Indexing

```python
arr[[0, 2, 4]]
```

### Multi-dimensional indexing

```python
matrix[1, 2]
```

These techniques are especially useful when working with:

* 📊 Data analysis
* 🤖 Machine learning datasets
* 🧮 Numerical computation
* 📈 Scientific computing

---

# 📂 Repository Structure

Current practice files are organized as progressive Python exercises:

```text
DAP/
│
├── 1__Python_Basics_Functions.py
├── 2__Set_Operations_basics.py
├── 3__List__Tuple.py
├── 4__Classes_basics.py
├── 5__Inheritance_Classes_Diamond.py
├── 6__Numpy_Basics.py
└── 7__Advance_Indexing.py
```

---

# 🧭 Learning Roadmap

Follow the repository in this order:

```text
                 🐍 Python
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
      Functions          Collections
          │              /    |    \
          ↓            List  Tuple  Set
          │
          ↓
      🏗️ OOP
          │
     ┌────┴────┐
     ↓         ↓
  Classes   Inheritance
                │
                ↓
        💎 Diamond Inheritance
                │
                ↓
            🔬 NumPy
                │
                ↓
        🎯 Advanced Indexing
```

---

# 🎯 Interview Preparation

These concepts form a useful foundation for Python-based technical interviews.

### 🟢 Beginner

* What are Python's basic data types?
* Difference between list and tuple?
* What is a set?
* How do sets handle duplicates?
* What is a function?
* What is the difference between `return` and `print`?
* What is list slicing?
* What is mutability?

### 🟡 Intermediate

* What is a class?
* What is an object?
* What does `self` represent?
* What is `__init__()`?
* What is inheritance?
* What is method overriding?
* What is multiple inheritance?
* What is MRO?
* What is the diamond problem?

### 🔴 NumPy / Data-Oriented

* What is NumPy?
* List vs NumPy array?
* What is vectorization?
* What is array broadcasting?
* What is array shape?
* What is boolean indexing?
* What is fancy indexing?
* How do you reshape an array?

---

# 🧠 Important Python Concepts to Revise

Before moving into advanced Python/Data Science topics, make sure you understand:

```text
☑ Variables & Data Types
☑ Operators
☑ Conditions
☑ Loops
☑ Functions
☑ Lists
☑ Tuples
☑ Sets
☑ Dictionaries
☑ List Comprehensions
☑ Classes & Objects
☑ Constructors
☑ Inheritance
☑ Multiple Inheritance
☑ MRO
☑ Exception Handling
☑ File Handling
☑ NumPy Arrays
☑ Indexing & Slicing
☑ Boolean Indexing
☑ Broadcasting
```

---

# 🧪 Practice Method

For every concept, follow this cycle:

```text
📖 Learn
   ↓
✍️ Write Code
   ↓
▶️ Run
   ↓
🐛 Debug
   ↓
🧠 Explain
   ↓
🔄 Modify
   ↓
🎯 Solve a Problem
```

### ⭐ Recommended rule

Don't simply copy the examples.

After understanding a program:

1. Close the reference.
2. Rewrite it yourself.
3. Change the input.
4. Add another condition.
5. Break the code intentionally.
6. Debug it.
7. Explain the result.

---

# 🚀 Future Expansion

This repository can be extended with the following modules:

### 🐍 Advanced Python

* Decorators
* Iterators
* Generators
* Lambda functions
* `map()`, `filter()`, `reduce()`
* Exception handling
* File handling
* Modules & packages
* Virtual environments

### 📊 Data Analytics

* Pandas
* Matplotlib
* Seaborn
* Data cleaning
* Exploratory Data Analysis
* Data visualization

### 🤖 Machine Learning

* Scikit-learn
* Data preprocessing
* Feature engineering
* Regression
* Classification
* Model evaluation

### 🧠 Interview Preparation

* Python coding problems
* OOP interview questions
* NumPy questions
* Data manipulation problems
* Output-based questions

---

# 📈 Progress Tracker

| Topic                  | Status |
| ---------------------- | :----: |
| 🐍 Python Basics       |    ⬜   |
| 🔧 Functions           |    ⬜   |
| 📦 Lists               |    ⬜   |
| 🔗 Tuples              |    ⬜   |
| 🔢 Sets                |    ⬜   |
| 🏗️ Classes            |    ⬜   |
| 🧬 Inheritance         |    ⬜   |
| 💎 Diamond Inheritance |    ⬜   |
| 🔬 NumPy Basics        |    ⬜   |
| 🎯 Advanced Indexing   |    ⬜   |
| 📊 Pandas              |    ⬜   |
| 📈 Data Visualization  |    ⬜   |
| 🤖 Machine Learning    |    ⬜   |

---

# 💻 Running the Programs

Make sure Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

Run any file with:

```bash
python filename.py
```

For example:

```bash
python 1__Python_Basics_Functions.py
```

For NumPy-based programs, install NumPy if required:

```bash
pip install numpy
```

Then run:

```bash
python 6__Numpy_Basics.py
```

---

# 🛠️ Tech Stack

* 🐍 Python
* 🔢 NumPy
* 💻 VS Code
* 🐙 Git & GitHub

---

# 🎓 Learning Objective

The purpose of this repository is to build a strong foundation in:

```text
Python
  +
Programming Logic
  +
Object-Oriented Programming
  +
Data Structures
  +
Numerical Computing
  +
Data-Oriented Programming
```

These fundamentals provide a base for progressing toward:

**Data Analytics → Machine Learning → AI → Software Development**

---

## ⭐ Keep Practicing

> **Don't focus on memorizing code. Focus on understanding why the code works.**

```text
Learn → Code → Experiment → Debug → Explain → Repeat 🔁


### ⭐ If this repository helps you learn Python, consider giving it a star!
