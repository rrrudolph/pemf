import urequests

class Time():
    def __init__(self):
        r = urequests.get("http://worldtimeapi.org/api/timezone/America/Chicago")
        dt = r.json()
        
        date = dt['datetime'].split('T')[0]
        time = dt['datetime'].split('T')[1]
        
        self.year = int(date.split('-')[0])
        self.month = int(date.split('-')[1])
        self.day = int(date.split('-')[2])
        self.day_of_year = dt['day_of_year']
        self.weekday = dt['day_of_week']

        self.hour = int(time.split(':')[0])
        self.minute = int(time.split(':')[1])
        self.second = int(time.split(':')[2].split('.')[0])
    
    def __gt__(self, other):
        if self.hour >= other.hour:
            return True
        if (
            self.hour >= other.hour and
            self.minute >= other.minute
        ):
            return True
    
    def __lt__(self, other):
        if self.hour <= other.hour:
            return True
        if (
            self.hour <= other.hour and
            self.minute <= other.minute
        ):
            return True
    
    def __repr__(self):
        return f"""Time({self.year}, {self.month}, {self.day}, {self.day_of_year}, {self.weekday}, {self.hour}, {self.minute}, {self.second})"""

    def copy(self, hour_delta=0, minute_delta=0):
        copy = Time()
        copy.year = self.year 
        copy.month = self.month
        copy.day = self.day
        copy.day_of_year = self.day_of_year
        copy.weekday = self.weekday
        copy.hour = self.hour + hour_delta
        copy.minute = self.minute + minute_delta
        copy.second = self.second 

        return copy
