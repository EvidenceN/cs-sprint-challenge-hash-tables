def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict_list = []

    #for i in range(len(arrays)):
    for index, values in enumerate(arrays):
        dict_list.append((index, values))

    hashtable = dict(dict_list)

    values = list(hashtable.values())

    a = []
    result = []

    for c in values:
        for i in c:
            if i not in a:
                a.append(i)
            else:
                if i not in result:
                    result.append(i)

    #for i in range(len(values)):
     #   if 

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))

    arrays = [
            list(range(10, 20)) + [1,2,3],
            list(range(20, 30)) + [1,2,3],
            list(range(30, 40)) + [1,2,3],
            list(range(40, 50)) + [1,2,3],
            list(range(50, 60)) + [1,2,3],
            list(range(60, 70)) + [1,2,3],
            list(range(70, 80)) + [1,2,3],
            list(range(80, 90)) + [1,2,3],
            list(range(90, 100)) + [1,2,3],
            list(range(100, 110)) + [1,2,3]
        ]

    print(intersection(arrays))