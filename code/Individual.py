class Individual:
    """
    Represents candidate solutions x = (x1, ..., xn)
    """
    def __init__(self, size):
        """
        Constructor for new Individual
        """
        # Number of integers necessary to represent all xi's
        necessary_integers = (size + 31) // 32
        self.size = size
        self.bits = [0] * necessary_integers

    def __lt__(self, other):
        if(self.size < other.size):
            return True
        else:
            return False

    def get(self, idx):
        """
        Get bit at index idx
        """
        test_bit = self.bits[idx // 32] & (1 << (idx % 32))
        return 1 if test_bit > 0 else 0

    def set(self, idx):
        """
        Set bit at index idx to 1
        """
        self.bits[idx // 32] |= (1 << (idx % 32))

    def reset(self, idx):
        """
        Set bit at index idx to 0
        """
        self.bits[idx // 32] &= ~(1 << (idx % 32))

    def flip(self, idx):
        """
        Flip bit at index idx
        """
        bit_i = self.get(idx)
        if bit_i == 0:
            self.set(idx)
        else:
            self.reset(idx)

    def count(self):
        """
        Count number of bits equal to 1
        """
        result = 0
        for i in range(self.size):
            bit_i = self.get(i)
            result += bit_i
        return result
