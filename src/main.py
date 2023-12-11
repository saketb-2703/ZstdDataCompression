import RLZ
import getDataFromDict
import binascii
import sys

if len(sys.argv) != 4:
    print("Usage: python3 src/main.py <reference_dict> <input_dict> <merged_dict>")
    sys.exit()

referenceFile = sys.argv[1]
inputFile = sys.argv[2]
mergedFile = sys.argv[3]

refFileData, metaData = getDataFromDict.getData(referenceFile)
inputFileData, _ = getDataFromDict.getData(inputFile)


# print("\n----------Metadata----------\n")
# print(metaData)
# print(refFileData)
# print("\n")
# print(inputFileData)
# print("\n")
# calling factorise function to create factors
factors = RLZ.factorise(inputFileData, refFileData)
print(factors)


# call addToRefDict to merge texts with less than the threshold length(tl)
th_length = 2
mergedData = RLZ.addToRefDict(inputFileData, refFileData, factors, th_length)

# convert to bytes
# mergedDataInBytes = mergedData.encode('utf-8')
mergedDataInBytes = mergedData.encode('utf-8')
# print("\nmerged data in bytes format")
# print(mergedDataInBytes)
# print(type(mergedDataInBytes))

# convert meta data from string to bytes
# metaDataInBytes = metaData.encode('utf-8')
metaDataInBytes = metaData.encode('utf-8')
# print("\n metaData in bytes fromat")
# print(metaDataInBytes)
# print(metaDataInBytes)
# print(type(metaDataInBytes))

patternData = "0000000400000008000000".encode('utf-8')
finalData = metaDataInBytes + patternData + mergedDataInBytes
# print(type(finalData))

# write merged data to reference file
with open(mergedFile, 'wb') as file:
    file.write(finalData)
