"""Utility functions for the party app."""


def is_mel(name, email):
    """Return True if name and email are related to Mel.

    Not Mel, return False
        >>> is_mel('hi', 'hi')
        False

        >>> is_mel('john', 'john@gmail.com')
        False

    If Mel's info in either name or email, return True
        >>> is_mel('Mel Melitpolski', 'test@gmail.com')
        True

        >>> is_mel('test', 'mel@ubermelon.com')
        True

    If Mel's info in both, return True
        >>> is_mel('Mel Melitpolski', 'mel@ubermelon.com')
        True

    """

    return name == 'Mel Melitpolski' or email == 'mel@ubermelon.com'


def most_and_least_common_type(treats):
    """Given list of treats, return most and least common treat types.

    Return most and least common treat types in tuple of format
    (most, least). If there's a tie, the dessert that appears
    first in alphabetical order should win.
    
    Basic
        >>> treats_1 = [ {'type': 'dessert'}, {'type': 'dessert'}, {'type': 'drink'},]
        >>> most_and_least_common_type(treats_1)
        ('dessert', 'drink')

    Empty list return None
        >>> treats_2 = []
        >>> most_and_least_common_type(treats_2)
        (None, None)

    Only one type return same for least and most
        >>> treats_3 = [ {'type': 'dessert'},]
        >>> most_and_least_common_type(treats_3)
        ('dessert', 'dessert')


    If there's a tie, the dessert that appears first in alphabetical
        >>> treats_4 = [ {'type': 'dessert'}, {'type': 'dessert'}, {'type': 'drink'}, {'type': 'drink'},{'type': 'appetizer'},]
        >>> most_and_least_common_type(treats_4)
        ('dessert', 'appetizer')
    """

    if not treats:
        return (None, None)

    types = {}

    # Count number of each type
    for treat in treats:
        types[treat['type']] = types.get(treat['type'], 0) + 1

    # Get tuples of (treat type, count) in alphabetical order
    types = sorted(types.items())

    # Find the min & max using the count of each tuple (which
    # is stored at index 1)
    most_type, _ = max(types, key=lambda treat_type: treat_type[1])
    least_type, _ = min(types, key=lambda treat_type: treat_type[1])

    return (most_type, least_type)
