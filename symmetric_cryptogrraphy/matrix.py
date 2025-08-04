def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    list = [0] * 16
    for n in range(4):
      for i in range(4):
        list[i+(4*n)] = matrix[n][i]
    return(list)

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]
flag = matrix2bytes(matrix)
for i in range(16):
  flag[i] = chr(flag[i])
print("".join(flag))
