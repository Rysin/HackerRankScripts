# Write a method to count number of times a Desired string appeared in a Given string.
# e.g. GivenString: MFJGIUTITICHGDH , DesiredString: "TI" Output: 2
# e.g. GivenString: IUOLYOYHHLKHUYOYOYTYTYYTYT, DesiredString: "YOY" Output: 2

def CountDesiredString(GivenString, DesiredString):
    Count = 0

    substring_len = len(DesiredString)

    # for i in range(len(GivenString)):
    #     if GivenString[i:i + substring_len] == DesiredString:
    #         Count += 1
    #         i = i + substring_len + 1
    i = 0
    while i <= len(GivenString):
        if GivenString[i:i + substring_len] == DesiredString:
            Count += 1
            i = i + substring_len
        i += 1


    return Count


print(CountDesiredString("IUOLYOYHHLKHUYOYOYTYTYYTYT", "YOY"))
