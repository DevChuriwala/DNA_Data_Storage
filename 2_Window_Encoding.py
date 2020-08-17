def toDNA(From_Binary_Encoding):
  DNA = ''
  (Binary_Encoding, Sense) = From_Binary_Encoding
  for char in range(0,len(Binary_Encoding),2):
    if (Binary_Encoding[char]=='0' and Binary_Encoding[char+1]=='0'):
      DNA += 'A'
    elif (Binary_Encoding[char]=='0' and Binary_Encoding[char+1]=='1'):
      DNA += 'T'
    elif (Binary_Encoding[char]=='1' and Binary_Encoding[char+1]=='0'):
      DNA += 'G'
    elif (Binary_Encoding[char]=='1' and Binary_Encoding[char+1]=='1'):
      DNA += 'C' 

  return DNA, Sense
