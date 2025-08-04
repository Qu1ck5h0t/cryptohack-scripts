state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    output = [[0] * 4 for _ in range(4)]
    for n in range(4):
      for i in range(4):
        output[n][i] = s[n][i] ^ k[n][i]
    return output

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    list = [0] * 16
    for n in range(4):
      for i in range(4):
        list[i+(4*n)] = matrix[n][i]
    return(list)

flag = matrix2bytes(add_round_key(state, round_key))
for i in range(16):
  flag[i] = chr(flag[i])
print("".join(flag))
