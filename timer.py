class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours % 24
        self.minutes = minutes % 60
        self.seconds = seconds % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def next_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0

    def prev_second(self):
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minutes -= 1
        if self.minutes == -1:
            self.minutes = 59
            self.hours -= 1
        if self.hours == -1:
            self.hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer1 = Timer(23, 59, 59)
timer1.prev_second()
print(timer1)