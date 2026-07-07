
def distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.

    Parameters:
    point1 (tuple): A tuple representing the coordinates of the first point (x1, y1).
    point2 (tuple): A tuple representing the coordinates of the second point (x2, y2).

    Returns:
    float: The Euclidean distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

point1 = tuple(map(float, input("Enter the coordinates of the first point (x1, y1) separated by a comma: ").split(',')))
point2 = tuple(map(float, input("Enter the coordinates of the second point (x2, y2) separated by a comma: ").split(',')))
print("The distance between the two points is:", distance(point1, point2))