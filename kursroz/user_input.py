from datetime import datetime

class UserInput:
    def readDate(self, prompt, format):
        while True:
            try:
                str = input(prompt)
                date = datetime.strptime(str, format)
                return date
            except:
                print("You've entered a wrong date")
                pass

    def readDouble(self, prompt): 
        while True:
            try:
                value = float(input(prompt))
                return value
            except:
                print("You've entered a wrong value")
                pass



