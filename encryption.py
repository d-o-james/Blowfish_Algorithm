def Enc(M, K):

    M = M.encode("utf-8") # encodes string to bit string

    subkey_array = subkey_gen(K) # gets subkey array

    m_L = M[0:len(M)//2]
    m_R = M[len(M)//2:]
    #splits strings into left and right halfs

    for i in range(16): # blowfish has a 15 round
        temp = m_L ^ subkey_array[i].encode("utf-8")
        temp = pseudorandom(temp) ^ m_R
        # uses temp values to get the new left sides value after being run through F_k
        
        m_R = m_L # copies left side to new right side
        m_L = temp # copies f_k's output to the new left side

    preprocessed_c = m_L + m_R # combines left and right sides

    return post_processing(subkey_array, preprocessed_c).decode("utf-8") #returns the values after post processing
