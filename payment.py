class Payment:
    def __init__(self, amount, method):
        self.amount = amount 
        self.method = method

    def __str__(self):
        return f"Payment(amount={self.amount}, method={self.method})"