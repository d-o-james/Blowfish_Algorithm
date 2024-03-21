def post_processing(parray, text):
  #S plit left and right
  left = text >> 32       # Gets rid of the 32 bits on the right by shifting right 
  right = text & 0xFFFFFFFF    # Gets rid of the 32 bits on the left by performing the & operation on the whole 64 bit text with only 32 bits
  
  # Final xor with parray
  left = left ^ parray[16]     
  right = right ^ parray[17]

  # Swap left and right
  left, right = right, left

  # Recombine the two halfs
  cipher_text = (left << 32) | right   # Shift the 32 left bits left, to make it 64 bits with lower 32 bits all 0, then or with right bits

  return cipher_text
