def displacement(x1, y1, x2, y2):
    """
    Calculate the displacement between two points.

    :param x1: X axis starting point
    :param y1: Y axis starting point
    :param x2: X axis ending point
    :param y2: Y axis ending point
    :return:  The X and Y displacement
    """
    delta_x = x2 - x1
    delta_y = y2 - y1
    return delta_x, delta_y
