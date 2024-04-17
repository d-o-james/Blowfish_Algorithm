def Decryption(cipher, key):

    cipher = cipher.encode("utf-8") # encodes string to bit string

    subkey_array = subkey_gen(K) # gets subkey array

    cipher_L = cipher[0:len(cipher)//2]
    cipher_R = cipher[len(cipher)//2:]
    #splits strings into left and right halfs

    for i in range(16): # blowfish has a 15 round
        temp = cipher_L ^ subkey_array[15-i].encode("utf-8")
        temp = pseudorandom(temp) ^ cipher_R
        # uses temp values to get the new left sides value after being run through F_k
        
        cipher_R = cipher_L # copies left side to new right side
        cipher_L = temp # copies f_k's output to the new left side

    preprocessed_c = cipher_L + cipher_R # combines left and right sides

    return post_processing(preprocessed_c, subkey_array[0], subkey_array[1]).decode("utf-8") #returns the values after post processing
