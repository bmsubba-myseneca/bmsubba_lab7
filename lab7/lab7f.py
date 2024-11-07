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

    def __add__(self, other):
        """Overload the + operator to add two Time objects."""
        if not isinstance(other, Time):
            raise TypeError("Operands must be instances of the Time class.")
        
        # Convert both times to seconds, sum them, and convert back to hours, minutes, seconds
        total_seconds = self.to_seconds() + other.to_seconds()
        
        # Calculate hours, minutes, seconds from total seconds
        hours = (total_seconds // 3600) % 24
        total_seconds %= 3600
        minutes = (total_seconds // 60) % 60
        seconds = total_seconds % 60
        
        return Time(hours, minutes, seconds)

    def to_seconds(self):
        """Convert time to total seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

# Ensure this file is recognized as a Python module
if __name__ == "__main__":
    t1 = Time(9, 50, 0)
    t2 = Time(1, 10, 0)
    sum_time = t1 + t2  # Uses the __add__ method
    print(str(sum_time))  # Output: 11:00:00
