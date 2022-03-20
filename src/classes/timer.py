from datetime import datetime, timedelta


class Timer:
    start: datetime
    end: datetime
    final: timedelta

    def set_start(self):
        self.start = datetime.now()

    def set_end(self):
        if not self.start:
            raise Exception("Please start the timer before set an end.")

        self.end = datetime.now()

    def set_final(self):
        self.final = self.end - self.start

    def get_final(self):
        return self.final
