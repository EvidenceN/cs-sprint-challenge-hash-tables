# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict_list = []

    if len(queries) > 1:
        for index, value in enumerate(files):
            query = queries[index]
            file = files[index]
            pair = (query, file)
            dict_list.append(pair)
    
    hashtable = dict(dict_list)

    result = []
    for key, value in hashtable.items():
        if value.endswith(key):
            result.append(value)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

    files = []

    for i in range(50):
        files.append(f"/dir{i}/file{i}")

    for i in range(50):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(100):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]

    print(finder(files, queries))

