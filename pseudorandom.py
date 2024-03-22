def pseudorandom(input_num):
    # Extract bytes from input num
    byte_1 = (input_num >> 24) & 0b11111111 # Uses bitwise operations to extract bytes
    byte_2 = (input_num >> 16) & 0b11111111 # >> is binary shift (equivalent to dividing by 2^num of bits shifted)
    byte_3 = (input_num >> 8) & 0b11111111  # & is binary AND with 11111111 (equivalent to modulo 2^8)
    byte_4 = input_num & 0b11111111
    # Consider decimal value 1024; extract 1 (thousands place) by doing 1024 / 10^3 = 1.024, take integer component of answer (1)
    # Extract 0 (hundreds place) by removing 1st digit (1024 % 1000 = 24), do 24 / 10^2 = 0.24, integer component of answer (0)
    # And so on

    # Retrieve 32-bit numbers from S-boxes based on the bytes
    s1 = S_BOXES[0][byte_1 % len(S_BOXES[0])]
    s2 = S_BOXES[1][byte_2 % len(S_BOXES[1])]
    s3 = S_BOXES[2][byte_3 % len(S_BOXES[2])]
    s4 = S_BOXES[3][byte_4 % len(S_BOXES[3])]

    # Combine using bitwise operations
    s12 = (s1 + s2) & 0xFFFFFFFF # 0xFFFFFFFF represents 32 1's in binary; max value represented by 32 bits
    s123 = s12 ^ s3              # & 0xFFFFFFFF: any bits beyond bit 32 of result are set to 0, preventing overflow
    output_num = (s123 + s4) & 0xFFFFFFFF

    return output_num
