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
        """Initializes serial generator instance"""
        self.start = start
        self.next = start
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"
    def generate(self):
        """Return the next number in sequence"""
        self.next += 1
        return self.next-1
    def reset(self):
        """Reset the serial generator to its original number"""
        self.next = self.start


