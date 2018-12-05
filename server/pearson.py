from math import sqrt

def pearson(list1, list2):
    # Sum of values
    sum1 = sum(list1)
    sum2 = sum(list2)

    # Sum of squares
    sum1Sq = sum([pow(val, 2) for val in list1])
    sum2Sq = sum([pow(val, 2) for val in list2])

    # Sum of the products
    pSum = sum([list1[i] * list2[i] for i in range(len(list1))])

    # Calculate Pearson Score
    num = pSum - (sum1 * sum2 / len(list1))
    den = sqrt((sum1Sq - pow(sum1, 2) / len(list1)) * (sum2Sq - pow(sum2, 2) / len(list1)))

    # 1 minus score => smaller distances = higher similarity
    return 1.0 - num / den