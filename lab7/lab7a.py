# lab7a.py

class Time:
    def __init__(self, hours, minutes, seconds):
        if not all(isinstance(i, int) for i in [hours, minutes, seconds]):
            raise ValueError("All arguments must be integers")
        if hours < 0 or minutes < 0 or seconds < 0:
            raise ValueError("Time values cannot be negative")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def sum_times(time1, time2):
    """Add two Time objects and return a new Time object with the result."""
    total_seconds = time1.seconds + time2.seconds
    total_minutes = time1.minutes + time2.minutes + total_seconds // 60
    total_hours = time1.hours + time2.hours + total_minutes // 60
    return Time(total_hours % 24, total_minutes % 60, total_seconds % 60)

def format_time(time_obj):
    """Return a formatted string 'HH:MM:SS' from a Time object."""
    return f"{time_obj.hours:02}:{time_obj.minutes:02}:{time_obj.seconds:02}"

# Example usage (optional, for standalone run)
if __name__ == "__main__":
    time1 = Time(9, 50, 0)
    time2 = Time(1, 1, 1)
    time_sum = sum_times(time1, time2)
    print(format_time(time_sum))  # Expected output: '10:51:01'
