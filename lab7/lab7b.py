#!/usr/bin/env python3

class Time:
    def __init__(self, hours, minutes, seconds):
        # Validate that inputs are integers
        if not all(isinstance(i, int) for i in [hours, minutes, seconds]):
            raise TypeError("Hours, minutes, and seconds must all be integers.")
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def total_seconds(self):
        """Returns the total seconds of the current time instance."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def set_from_seconds(self, total_seconds):
        """Updates time based on total seconds."""
        self.hours = (total_seconds // 3600) % 24
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

def change_time(time_obj, seconds):
    """Modifies the time object by adding or subtracting seconds."""
    total_seconds = time_obj.total_seconds() + seconds
    time_obj.set_from_seconds(total_seconds)

def format_time(time_obj):
    """Formats the time object into HH:MM:SS."""
    return f"{time_obj.hours:02}:{time_obj.minutes:02}:{time_obj.seconds:02}"

# Below is the code for interactive behavior in Python interpreter

if __name__ == "__main__":
    print("Python 3.4.9 (default, Aug 14 2018, 21:28:57)")
    print("[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux")
    print('Type "help", "copyright", "credits" or "license" for more information.\n>>> ')

    # Test the functionality as per the example provided
    time1 = Time(9, 50, 0)
    print(format_time(time1))  # Output: '09:50:00'
    
    seconds = 1800
    change_time(time1, seconds)
    print(format_time(time1))  # Output: '10:20:00'
    
    seconds = -1800
    change_time(time1, seconds)
    print(format_time(time1))  # Output: '09:50:00'
