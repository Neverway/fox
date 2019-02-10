from game.models import Grass, Stone, Dirt

terrain = [
    # Floor (cover)
    Stone(0, 18),
    Stone(1, 18),
    Stone(2, 18),
    Stone(3, 18),
    Stone(4, 18),
    Stone(5, 18),
    Stone(6, 18),
    Stone(7, 18),
    Stone(8, 18),
    Stone(9, 18),
    Stone(10, 18),
    Stone(11, 18),
    Stone(12, 18),
    Stone(13, 18),
    Stone(14, 18),
    Stone(15, 18),
    Stone(16, 18),
    Stone(17, 18),
    Stone(18, 18),
    Stone(19, 18),
    Stone(20, 18),
    Stone(21, 18),
    Stone(22, 18),
    Stone(23, 18),
    Stone(24, 18),

    # Left wall (fit)
    Stone(0, 1),
    Stone(0, 2),
    Stone(0, 3),
    Stone(0, 4),
    Stone(0, 5),
    Stone(0, 6),
    Stone(0, 7),
    Stone(0, 8),
    Stone(0, 9),
    Stone(0, 10),
    Stone(0, 11),
    Stone(0, 12),
    Stone(0, 13),
    Stone(0, 14),
    Stone(0, 15),

    # Right wall (fit)
    Stone(24, 1),
    Stone(24, 2),
    Stone(24, 3),
    Stone(24, 4),
    Stone(24, 5),
    Stone(24, 6),
    Stone(24, 7),
    Stone(24, 8),
    Stone(24, 9),
    Stone(24, 10),
    Stone(24, 11),
    Stone(24, 12),
    Stone(24, 13),
    Stone(24, 14),
    Stone(24, 15),
    Stone(24, 16),
    Stone(24, 17),

    # Roof (cover)
    Stone(0, 0),
    Stone(1, 0),
    Stone(2, 0),
    Stone(3, 0),
    Stone(4, 0),
    Stone(5, 0),
    Stone(6, 0),
    Stone(7, 0),
    Stone(8, 0),
    Stone(9, 0),
    Stone(10, 0),
    Stone(11, 0),
    Stone(12, 0),
    Stone(13, 0),
    Stone(14, 0),
    Stone(15, 0),
    Stone(16, 0),
    Stone(17, 0),
    Stone(18, 0),
    Stone(19, 0),
    Stone(20, 0),
    Stone(21, 0),
    Stone(22, 0),
    Stone(23, 0),
    Stone(24, 0),

    # Inside
    Stone(6, 17),
    Stone(6, 16),
    Stone(6, 15),
    Stone(6, 14),
    Stone(15, 17),
    Stone(15, 16),

]
