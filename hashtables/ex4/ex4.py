def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = []
    for index, number in enumerate(a):
        key = index
        value = number
        pair = (key, value)
        numbers.append(pair)

    hashtable = dict(numbers)

    
    values = hashtable.values()

    negative = [i for i in values if i < 0]
    positive = [i for i in values if i >= 0]
    
    # get the positive versions of the negative value
    neg_to_pos = [abs(i) for i in negative]

    result = [i for i in neg_to_pos if i in positive]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
