#!/usr/bin/env python3

class Time:
    def __init__(self, hours, minutes, seconds):
        # Validate inputs to ensure they are integers
        if not all(isinstance(i, int) for i in [hours, minutes, seconds]):
            raise TypeError("Hours, minutes, and seconds must be integers.")
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time components cannot be negative.")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def total_seconds(self):
        """Returns total seconds represented by the current time."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def set_from_seconds(self, total_seconds):
        """Sets the time based on total seconds."""
        self.hours = (total_seconds // 3600) % 24
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

def time_to_sec(time_obj):
    """Converts a Time object into total seconds."""
    if not isinstance(time_obj, Time):
        raise TypeError("Input must be of type Time")
    return time_obj.total_seconds()

def sec_to_time(seconds):
    """Converts total seconds into a Time object."""
    if not isinstance(seconds, int):
        raise TypeError("Input must be an integer")
    time_obj = Time(0, 0, 0)
    time_obj.set_from_seconds(seconds)
    return time_obj

def format_time(time_obj):
    """Returns a formatted string 'HH:MM:SS' for the given Time object."""
    return f"{time_obj.hours:02}:{time_obj.minutes:02}:{time_obj.seconds:02}"

# This section allows for interactive use if run in an interpreter
if __name__ == '__main__':
    import sys
    print(f"Python {sys.version} on {sys.platform}")
    print("Type \"help\", \"copyright\", \"credits\" or \"license\" for more information.")
