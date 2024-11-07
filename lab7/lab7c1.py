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

    def add_time(self, time_obj):
        """Adds another Time object to the current time."""
        total_seconds = self.total_seconds() + time_obj.total_seconds()
        self.set_from_seconds(total_seconds)

    def add_seconds(self, seconds):
        """Adds seconds to the current time."""
        total_seconds = self.total_seconds() + seconds
        self.set_from_seconds(total_seconds)

def format_time(time_obj):
    """Returns a formatted string 'HH:MM:SS' for the given Time object."""
    return f"{time_obj.hours:02}:{time_obj.minutes:02}:{time_obj.seconds:02}"

# Testing the script
if __name__ == '__main__':
    # Test Case 1
    time1 = Time(8, 0, 0)
    time2 = Time(0, 50, 0)
    time1.add_time(time2)
    print(f"{format_time(Time(8, 0, 0))} + {format_time(time2)} --> {format_time(time1)}")

    # Test Case 2
    time3 = Time(8, 55, 0)
    time3.add_time(time2)
    print(f"{format_time(Time(8, 55, 0))} + {format_time(time2)} --> {format_time(time3)}")

    # Test Case 3
    time4 = Time(9, 50, 0)
    time4.add_seconds(1800)
    print(f"{format_time(Time(9, 50, 0))} + 1800 sec --> {format_time(time4)}")
