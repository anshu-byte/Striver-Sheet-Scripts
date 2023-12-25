class StockSpanner:
    def __init__(self):
        self.stack = []
        self.prices = []
        self.index = 0

    def next(self, price: int) -> int:
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        if self.stack:
            prev_index = self.stack[-1]
        else:
            prev_index = -1

        span = self.index - prev_index
        self.stack.append(self.index)
        self.prices.append(price)
        self.index += 1

        return span
