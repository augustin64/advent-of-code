class Interval:
    """Définit des intervalles de $\\mathbb{R}$"""
    def __init__(self, a: float, b: float) -> None:
        assert a <= b

        self.low = a
        self.up = b

    def __repr__(self) -> str:
        if self.up == self.low:
            return '{'+str(self.up)+'}'
        return f"[{self.low}, {self.up}]"

    def __len__(self) -> float:
        return self.up - self.low

    def __contains__(self, item: float) -> bool:
        return self.low <= item and item <= self.up

    def __eq__(self, interval):
        return self.low == interval.low and self.up == interval.up

    def intersect(self, interval) -> bool:
        return not (interval.low > self.up or self.low > interval.up)

    def intersection(self, interval):
        if interval.low > self.up or self.low > interval.up:
            return None
        new_min = max(self.low, interval.low)
        new_max = min(self.up, interval.up)
        return Interval(new_min, new_max)