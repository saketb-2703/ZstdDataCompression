import RLZ
import getDataFromDict
import binascii
# opening both the files in reading modes
# referenceFile = "../textFiles/dictionary1.zst"
# inputFile = "../textFiles/dictionary2.zst"
referenceFile = "dict_org1.zstd"
inputFile = "dict_org2.zstd"

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
with open('mergeDict1.zstd', 'wb') as file:
    file.write(finalData)



referenceFile = "mergeDict1.zstd"
inputFile = "dict_org3.zstd"

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
with open('mergeDict2.zstd', 'wb') as file:
    file.write(finalData)



