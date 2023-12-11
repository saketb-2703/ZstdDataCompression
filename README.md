# Privacy-Aware Data Compression

### Repository structure
1. `myDictionaries` contain the respective individual dictionaries and the merged global dictionary
2. `orgs` contain the different organization's data contents
3. `src` contains the source codes used, mainly the RLZ factorization algorithms.

### How to train Dictionary as well as compress and decompress data with it
1. Create the dictionary

   `zstd --train FullPathToTrainingSet/* -o dictionaryName`

2. Compress with dictionary

   `zstd -D dictionaryName FILE`

3. Decompress with dictionary

   `zstd -D dictionaryName --decompress FILE.zst`

### Working
1. Create the individual dictionaries for each organization as mentioned above using Zstd and place them in `myDictionaries` directory. This can be done by executing the command `zstd --train <PathToOrganizationData>/* -o myDictionaries/<dict_name>`
2. Merge the dictionaries of any two organizations using `python3 src/main.py <reference_dict> <input_dict> <merged_dict>`
3. Use the newly created merged global dictionary along with the individual dictionaries to do the analysis by compressing the organizations' data.