from subkey_gen.py import subkey_gen
from pseudorandom.py import pseudorandom
from post_processing.py import post_processing

def Encryption(Text, Key):

    Text = Text.encode("utf-8") # encodes string to bit string

    subkey_array = subkey_gen(K) # gets subkey array

    T_L = Text[0:len(M)//2]
    T_R = Text[len(M)//2:]
    #splits strings into left and right halfs

    for i in range(16): # blowfish has a 15 round
        temp = T_L ^ subkey_array[i].encode("utf-8")
        temp = pseudorandom(temp) ^ T_R
        # uses temp values to get the new left sides value after being run through F_k
        
        T_R = T_L # copies left side to new right side
        T_L = temp # copies f_k's output to the new left side

    preprocessed_c = T_L + T_R # combines left and right sides

    return post_processing(preprocessed_c, subkey_array[17], subkey_array[16]).decode("utf-8") #returns the values after post processing
