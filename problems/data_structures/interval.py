class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __and__(self, other):
        return Interval(min(self.start, other.end), max(self.end, other.end))

    def overlaps(self, other):
        return min(self.end, other.end) - max(self.start, other.start) >= 0

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end