# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


def Huffman_Compress(string, retainCase=False, outGraph=False):
  # Calculating frequency
  freq = {}
  for c in string:
      if c in freq:
          freq[c] += 1
      else:
          freq[c] = 1

  freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

  nodes = freq

  while len(nodes) > 1:
      (key1, c1) = nodes[-1]
      (key2, c2) = nodes[-2]
      nodes = nodes[:-2]
      node = NodeTree(key1, key2)
      nodes.append((node, c1 + c2))

      nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

  huffmanCode = huffman_code_tree(nodes[0][0])
  
  if outGraph == True:
    print(' Char | Huffman code ')
    print('----------------------')
    for (char, frequency) in freq:
        print(' %-4r |%12s' % (char, huffmanCode[char]))
  
  return huffmanCode
  
def toBinary(String, GraphKeys):
  Encoding = ""
  Sense = 'Even'
  for char in String:
    Encoding += (str(GraphKeys[char]))

  if len(Encoding)%2 != 0:
    Encoding += str(0)
    Sense = 'Odd'
  return Encoding, Sense
  
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
  
def Encrypt(String):
  !pip install cryptography # for Google Colab, use pip/pip3 on local env
  from cryptography.fernet import Fernet
  key = Fernet.generate_key()
  encryption_type = Fernet(key)
  String = str(encryption_type.encrypt(bytes(String, encoding='utf8')))

  return String

def Decrypt(String, key):
  !pip install cryptography # for Google Colab, use pip/pip3 on local env
  from cryptography.fernet import Fernet
  encryption_type = Fernet(key)  
  String = encryption_type.decrypt(String)

  return String


def Main_Compress(String, encrypt=False, retainCase = False, outGraph = False):

  #encrypt -- enables encryption
  #retainCase -- enables the Capitalization data to be preserved
  #outGraph -- Huffman key-values useful for decoding
  
  if encrypt == True:
    String = Encrypt(String)
  
  return(toDNA(toBinary(String, Huffman_Compress(String, retainCase, outGraph))))

  
