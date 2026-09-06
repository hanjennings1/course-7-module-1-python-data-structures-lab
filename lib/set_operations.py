# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # Sets automatically discard duplicates, so this gives us each major only once
    return {student[2] for student in student_list}
