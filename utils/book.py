from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Book():
    id: int
    title: str
    description: str
    pageCount: int
    excerpt: str
    publishDate: str
    
    def __eq__(self, other):
        # Custom comparison logic
        if self.id != other.id:
            return False
        
        if self.title != other.title:
            return False
        
        if self.description != other.description:
            return False
        
        if self.pageCount != other.pageCount:
            return False
        
        if self.excerpt != other.excerpt:
            return False
        
        # Calculate the difference in dates
        difference = abs(datetime.fromisoformat(self.publishDate) - datetime.fromisoformat(other.publishDate))
        
        if (difference < timedelta(hours=26) or difference > timedelta(hours=28)) and difference != timedelta(hours=0):
            return False

        return True
    
    def __post_init__(self):
        # Extract the date component
        self.publishDate = self.add_plus_timezone()
        self.publishDate = self.adjust_microseconds_digits()
        
    def adjust_microseconds_digits(self, position=26):
        """Removes the 7th microsecond because the datetime.fromisoformat() doesn't allow it.
        """
        pdate_array = self.publishDate.split("+")
        without_tz_date = pdate_array[0]
        if len(without_tz_date) > 26:
            return without_tz_date[:26] + "+" + pdate_array[-1]
        elif (date_length:=len(without_tz_date)) < 26:
            zeroes_to_add = 26 - date_length
            return without_tz_date + zeroes_to_add*"0" + "+" + pdate_array[-1]
        else:
            return self.publishDate
        
    def add_plus_timezone(self):
        """Add the +00:00 timezone when needed.
        """
        if self.publishDate.endswith("z"):
            return self.publishDate[:-1] + "+00:00"
        elif "+" not in self.publishDate:
            return self.publishDate + "+00:00"
        else:
            return self.publishDate
        