def toBinary(String, GraphKeys):
  Encoding = ""
  Sense = 'Even'
  for char in String:
    Encoding += (str(GraphKeys[char]))

  if len(Encoding)%2 != 0:
    Encoding += str(0)
    Sense = 'Odd'
  return Encoding, Sense
