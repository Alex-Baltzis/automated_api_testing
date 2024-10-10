from dataclasses import dataclass


@dataclass
class Author:
    """
    Dataclass for Author objects.

    Attributes:
        id (int): The ID of the author.
        idBook (int): The ID of the book.
        firstName (str): The first name of the author.
        lastName (str): The last name of the author.
    """
    id: int
    idBook: int
    firstName: str
    lastName: str
    
    
        