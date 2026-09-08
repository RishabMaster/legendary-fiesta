"""
This program calculates the reaming bake time, preparation time for layers, and total elapse time for preparing a lasagna.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 60

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number of layers (int): The numbers of layers on the lasagna.

    Returns:
        int: The time (in minutes) required to prepare these number of layers.

    Function that takes the number of layers for the lasagna as
    an argument and returns the time required for making them.
    """
    return int(number_of_layers) * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time (in minutes).

    Parameters:
        number of layers (int): The number of layers for lasagna
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total time elapsed in baking of lasagna and layer making.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument along with the required number of layers for the lasagna and returns the       total elapsed time
    """
    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time