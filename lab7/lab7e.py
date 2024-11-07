import os

class Time:
    def __init__(self, hours, minutes, seconds):
        """Initialize the Time object with hours, minutes, and seconds."""
        if not all(isinstance(i, int) for i in [hours, minutes, seconds]):
            raise TypeError("Time values must be integers.")
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError("Invalid time values. Ensure hours are between 0 and 23, minutes and seconds between 0 and 59.")
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def __str__(self):
        """Return a string representation of the time in HH:MM:SS format."""
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __repr__(self):
        """Return a string representation of the time in HH.MM.SS format."""
        return f"{self.hours:02}.{self.minutes:02}.{self.seconds:02}"

# Ensure this file is recognized as a Python module
if __name__ == "__main__":
    t1 = Time(9, 50, 0)
    print(t1)  # This will use the __str__ method
    print(repr(t1))  # This will use the __repr__ method
