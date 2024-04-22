import itertools


class RunLengthEncoder:
    def __init__(self, operator='|', seperator='-'):
        self.operator = operator
        self.separator = seperator

    def encode(self, data):
        encoded = ''
        for char, group in itertools.groupby(data):
            cnt = sum(1 for _ in group)
            if cnt == 1:
                encoded += char
            else:
                encoded += f'{self.operator}{cnt}{self.separator}{char}'
        return encoded

    def decode(self, data):
        decoded = ''
        count = ''
        enc = False
        num = False
        # run = False
        print('char | enc | num')
        for i, char in enumerate(data):
            print(char, enc, num)

            if char == self.operator and enc and not num:
                decoded += char
                enc = False
            if char == self.operator and not enc and not num:  # number is next
                num = True
                continue

            if char == self.separator and enc and not num:
                decoded += char
                # run = True
            if char == self.separator and not enc and num:  # encoded char is next
                enc = True
                num = False
                continue
            # if char == self.separator and enc

            if num:
                count += char
            if enc:
                decoded += char * int(count or 1)
                count = ''
                enc = False
        return decoded

    @staticmethod
    def compression_ratio(original, encoded):
        orig = len(original)
        enc = len(encoded)
        return round(1 - enc / orig, 2)
