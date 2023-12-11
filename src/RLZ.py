# this is to factorize using RLZ algo
def factorise(T, S):
    factors = []
    i = 0
    while i < len(T):
        longest_factor = ""
        factor_position = -1

        for j in range(1, len(T) - i + 1):
            candidate_factor = T[i:i + j]

            if candidate_factor in S:
                factor_position = S.index(candidate_factor)
                longest_factor = candidate_factor
            else:
                break
        
        if longest_factor:
            factors.append((factor_position, len(longest_factor)))
            i += len(longest_factor)
            # print(len(longest_factor))
        else:
            # No factor found in S, treat it as a letter
            print("\n\n=====================================")
            print(type(T[i].encode('utf-8')))
            print("=======================================\n\n")
            factors.append((T[i].encode('utf-8'), 0))
            i += 1
        print(i)
    return factors


# add to reference dictionary where the lenght is less than threshold
def addToRefDict(T, S, factors, th_length):
    len = 0
    for factor in factors:
        if(factor[1]<th_length):
            if(type(factor[0]) != int):
                S = S + factor[0]
            else:
                S = S + S[factor[0]: factor[0]+factor[1]]
    # print(S)
    return S

