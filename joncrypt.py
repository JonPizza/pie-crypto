import random

def xor(bit1, bit2):
  if bit1 == 0:
    return 1 if bit2 else 0
  else:
    return 0 if bit2 else 1

class JonCrypt:
  def __init__(self, key=None):
    if not key:
      self.key = 'thisisagreatkey'
    else:
      self.key = key
      
