import datetime as dt
import time


class Timer:
    def __init__(self, targetTime: str, timeBuffer: float = 0.01):
        self.targetTime = dt.datetime.strptime(
            dt.date.today().strftime("%Y-%m-%d") + targetTime, "%Y-%m-%d%H:%M:%S"
        )
        self.currentTime = dt.datetime.now()
        self.timeBuffer = dt.timedelta(seconds=timeBuffer)
        self.STATUS = False

        print("Target time:", self.targetTime)

    def currentTimeReport(self):
        print("Current time:", self.currentTime, end="\r")

    def run(self):
        while True:
            self.currentTime = dt.datetime.now()
            if self.targetTime <= self.currentTime + self.timeBuffer:
                self.currentTimeReport()
                print("time is up")
                self.STATUS = True
                return True
            else:
                if self.targetTime - self.currentTime >= dt.timedelta(seconds=10):
                    self.currentTimeReport()
                    time.sleep(1)
                else:
                    self.currentTimeReport()


if __name__ == "__main__":
    target_time = "01:03:00"
    timer = Timer(targetTime=target_time)
    timer.run()
