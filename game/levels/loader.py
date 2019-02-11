import logging
import game.models

log = logging.getLogger(__name__)


def ascii_map(filename, models=None):
    if not models:
        models = game.models.ASCII_MAP
    with open(filename) as ascii_file:
        return [
            models.get(char, game.models.Block)(x, y)
            for y, line in enumerate(ascii_file)
            for x, char in enumerate(line)
            if models.get(char)
        ]
