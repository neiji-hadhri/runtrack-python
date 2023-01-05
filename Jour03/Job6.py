string = "abcdefghijklmnopqrstuvwxyz" * 10
n = len(string)
line_length = 1
i = 0
while i + line_length <= n:

  print(string[i:i+line_length])

  i += line_length

  line_length += 1