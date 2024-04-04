#!/usr/bin/python3
"""
handles the UTF-8 encoding problem
"""


def validUTF8(data):
    """
    Returns true if data is a valid UTF-8 encoding,
    else return False
    """
    def countbytes(byte):
        """
        returns the number of leading ones in a byte
        """
        count = 0
        mask = 1 << 7
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    def isValid(start, length):
        """
        verifies whether a sequence of bytes is in the given data
        """
        if length == 1:
            return True
        for i in range(start + 1, start + length):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    j = 0
    while j < len(data):
        leadingbytes = countbytes(data[j])

        if leadingbytes == 0:
            j += 1
            continue
        elif leadingbytes == 1 or leadingbytes > 4:
            return False

        elif not isValid(j, leadingbytes):
            return False

        j += leadingbytes

    return True
