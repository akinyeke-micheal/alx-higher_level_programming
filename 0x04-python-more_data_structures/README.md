# 0x04-python-more_data_structures

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains Python scripts and examples showcasing advanced data structures and manipulations. The focus is on expanding your knowledge beyond basic data structures and exploring more complex and versatile data structures available in Python.

## Table of Contents

- [Introduction](#introduction)
- [Content](#content)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this module, we delve into more sophisticated data structures and operations in Python. From dictionaries and sets to comprehensions and lambda functions, this repository aims to enhance your understanding of Python's powerful capabilities.

## Content

- **1. `0-square_matrix_simple.py`:** Function to compute the square value of all integers of a matrix.
- **2. `1-search_replace.py`:** Function to replace all occurrences of an element by another in a new list.
- **3. `2-uniq_add.py`:** Function to add all unique integers in a list.
- **4. `3-common_elements.py`:** Function to return a set of common elements in two sets.
- **5. `4-only_diff_elements.py`:** Function to return a set of all elements present in only one set.
- **6. `5-number_keys.py`:** Function to count the number of keys in a dictionary.
- **7. `6-print_sorted_dictionary.py`:** Function to print a dictionary sorted by keys.
- **8. `7-update_dictionary.py`:** Function to update a dictionary with key-value pairs.
- **9. `8-simple_delete.py`:** Function to delete a key in a dictionary.
- **10. `9-multiply_by_2.py`:** Function to multiply all values of a dictionary by 2.
- **11. `10-best_score.py`:** Function to get the key with the highest integer value.
- **12. `11-mutiply_list_map.py`:** Function to multiply all elements of a list using `map`.
- **13. `12-roman_to_int.py`:** Function to convert a Roman numeral to an integer.

## Usage

To use any of the scripts in this repository, simply clone the repository and run the Python scripts using a compatible Python interpreter (Python 3.x recommended).

```bash
git clone https://github.com/your_username/0x04-python-more_data_structures.git
cd 0x04-python-more_data_structures
python3 script_name.py
Examples
Here are a few examples demonstrating the usage of some scripts:

python
Copy code
# Example 1: Square Matrix
from square_matrix_simple import square_matrix_simple
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = square_matrix_simple(matrix)
print(result)
# Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

# Example 2: Common Elements
from common_elements import common_elements
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result_set = common_elements(set1, set2)
print(result_set)
# Output: {3, 4}
Contributing
Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request. Please follow the contribution guidelines.

License
This project is licensed under the MIT License. See the LICENSE file for details.
