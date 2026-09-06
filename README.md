## Features Implemented

This project implements a simple Student Data Management System with the following functionality:

### Data Storage
- Student records are stored in `student_data.py` as a list of tuples in the format `(ID, Name, Major)`.

### Filtering (`filters.py`)
- `filter_students_by_major(student_list, major)` — returns a list of students matching a given major, using a case-insensitive list comprehension.

### Displaying Data (`data_processing.py`)
- `format_student_data(student)` — formats a single student tuple into a readable string: `"ID: 101 | Name: Maya Chen | Major: English"`.
- `display_students(student_list)` — loops through a list of students and prints each one using `format_student_data`.

### Set Operations (`set_operations.py`)
- `unique_majors(student_list)` — returns a set of all unique majors across the student list, using set comprehension.

### Generator Expressions (`data_generator.py`)
- `student_generator(student_list, major)` — returns a generator expression yielding students matching a given major one at a time, for memory-efficient processing of large datasets.

## Usage Example

```python
from lib.student_data import students
from lib.filters import filter_students_by_major
from lib.data_processing import display_students
from lib.set_operations import unique_majors
from lib.data_generator import student_generator

# Filter students by major
math_students = filter_students_by_major(students, "History")

# Display all students
display_students(students)

# Get unique majors
majors = unique_majors(students)

# Process students lazily by major
gen = student_generator(students, "English")
next(gen)
```

## Running Tests

```sh
pipenv install
pipenv shell
pytest
```