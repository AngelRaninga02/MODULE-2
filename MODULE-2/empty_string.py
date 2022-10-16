def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('raninga'))
print(string_both_ends('ra'))
print(string_both_ends('r'))