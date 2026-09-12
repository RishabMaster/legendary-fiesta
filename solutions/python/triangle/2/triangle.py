"""Functions to check if sides are making a valid triangle and returns True of False based on triangle function type like equilateral, isosceles, and scalene.
"""

def is_a_triangle(sides):
    """Checks if the sides are actually making a triangle

    Args:
        sides (list of int,float): A list containing the 3 sides of the triangle

    Returns: 
        bool: True or False based on conditions like all side have postive length and belong to int or float
    """
    if 0 in sides: return False
        
    if len(sides) != 3 : return False
        
    if not all(isinstance(side,(int,float)) for side in sides): return False
        
    return all(sum(sides) >= 2 * side for side in sides) 

def equilateral(sides):
    """Checks if the triangle is equilateral

    Args:
        sides (list of int,float): A list containing the 3 sides of the triangle

    Returns: 
        bool: True if all sides are of same length, False otherwise
    """
    
    if is_a_triangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False

def isosceles(sides):
    """Checks if the triangle is isosceles

    Args:
        sides (list of int,float): A list containing the 3 sides of the triangle

    Returns: 
        bool: True if any two sides have the same length, False otherwise 
    """
    
    if is_a_triangle(sides):
        if sides[0] in sides[1:]:
            return True
        return sides[1] == sides[2]
    return False

def scalene(sides):
    """Checks if the triangle is scalene

    Args:
        sides (list of int,float): A list containing the 3 sides of the triangle

    Returns: 
        bool: True if no two sides are of the same length, False otherwise.
    """
    
    if is_a_triangle(sides):
        return sides[0] not in sides[1:] and sides[1] != sides[2]
    return False
    
