class Calculator:
    @staticmethod
    def power(n, p):
        if n >= 0 and p >= 0:
            return pow(n, p)
        else:
            raise ValueError("n and p should be non-negative")
