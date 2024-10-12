class WeekDayError(Exception):
    pass

class Weeker:
    __days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError()
        self.__current_day = self.__days.index(day)
        
    def __str__(self):
        return self.__days[self.__current_day]
    
    def add_days(self, n):
        self.__current_day = (self.__current_day + n) % len(self.__days)
        
    def subtract_days(self, n):
        self.__current_day = (self.__current_day - n) % len(self.__days)
        
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")