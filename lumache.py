"""
lumache - python library for cook and food lovers
"""

__version__ = "0.1.0"

class InvalidKindError(Exception):
    """Raised if Kind is invalid"""
    pass

def get_random_ingredients(Kind =  None):
    """
    Return a list of random ingredients as strings

    :param kind: Option "kind" of ingredients
    :type kind: list[str] or None
    :rtypr: list[str]
    """

    return ["shells", "gorgonzola", "parsley"]