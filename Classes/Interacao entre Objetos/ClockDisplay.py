from NumberDisplay import NumberDisplay
class ClockDisplay:
    """__hours - classe NumberDisplay
       __minutes - classe NumberDisplay
       __displayString - string"""
    def __init__(self):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__updateDisplay()

    def __updateDisplay(self):
        self.__displayString = self.__hours.getDisplayValue() + ":" + self.__minutes.getDisplayValue()
    def getHours(self):
        return self.__hours.getDisplayValue()
    def getMinutes(self):
        return self.__minutes
    def getTime(self):
        return self.__displayString
    def setTime(self,hour,minute):
        if(hour < 24 and hour >= 0):
           self.__hours.setValue(hour)
        if (minute < 60 and hour >= 0):
            self.__minutes.setValue(minute)
        self.__updateDisplay()
