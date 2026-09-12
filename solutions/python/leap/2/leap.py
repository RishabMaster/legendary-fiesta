"""Program to tell if a year is a leap year
"""

def leap_year(year):
    """Function to determine if the given year is a leap year

    Args:
        year (int): The year to check for leap year

    Returns:
        bool: returns True or False based on whether the year was a leap year
    """
    # checks for the second condition
    if year % 100 == 0: return year % 400 == 0

    # checks for the first condition
    return year % 4 == 0
