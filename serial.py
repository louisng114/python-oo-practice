"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,start):
        self.start = start
        self.progress = -1
    
    def __repr__(self):
        return f"SerialGenerator(start={self.start})"

    def generate(self):
        self.progress += 1
        return self.start + self.progress
    
    def reset(self):
        self.progress = -1