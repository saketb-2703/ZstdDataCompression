def getData(dictFile):
    with open(dictFile,'rb') as f1:
    
        # reading f1 contents
        S = f1.read()
        
        # print(type(S))
        # print("\n")
        # print("\n\n")

        hex_string =  S.hex()
        # print(hex_string)
        # print(type(hex_string))
        # print("\n\n")



        # # Adding 32

        # # Split the string into pairs (e.g., "37", "a4", "30", ...)
        # hex_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

        # # Add 32 (0x20) to each pair, convert to integers, and back to hexadecimal
        # modified_hex_pairs = [format((int(pair, 16) + 32) % 256, '02x') for pair in hex_pairs]

        # # Join the modified pairs back into a single string
        # result_hex_string = ''.join(modified_hex_pairs)

        # # Print the result
        # # print(result_hex_string)
        # # print('\n\n')




        # Find the index where (0000 0004 0000 0008 0000 00)+32 = "2020 2024 2020 2028 2020 20" appears in the string
        index = hex_string.find("0000 0004 0000 0008 0000 00")

        if index == -1:
            index = hex_string.find("00 0000 0400 0000 0800 0000") 
            if index != -1:
                print("Data not found in the input string.")
            else:
                data_after_substring = hex_string[index + len("00 0000 0400 0000 0800 0000"):]
                metaData = hex_string[:index]
        # Check if the substring was found
        elif index != -1:
            # Extract the data after "2020202420202028202020"
            data_after_substring = hex_string[index + len("0000 0004 0000 0008 0000 00"):]
            metaData = hex_string[:index]
        else:
            print("Data not found in the input string.")

    return data_after_substring, metaData


