from dataclasses import dataclass


@dataclass
class Author():
    id: int
    idBook: int
    firstName: str
    lastName: str
    
    
        