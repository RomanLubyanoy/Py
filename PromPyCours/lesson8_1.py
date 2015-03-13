class CombStr(object):
    # text = None

    def __init__(self, text=None):
        self.text = text

    def count_substrings(self, length=0):
        rez = 0
        l1 = []
        if length < 1:
            return 0

        for i in range(0, len(self.text)):
            for j in range(i, len(self.text), length):
                if len(self.text[j:j + length]) == length:
                    l1.append(self.text[j:j + length])

        return len(set(l1))


# qqqqqqweqqq%
s0 = CombStr('qqqqqqweqqq%')

print s0.text
print s0.count_substrings(1)
