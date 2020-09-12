from itertools import combinations 

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    if len(weights) > 1:
        # find the pair that adds to weight limit using python combinations
        test = [pair for pair in combinations(weights, 2) if sum(pair) == limit]
        list_pair = list(test[0])

        # store the list as key's, and indexes as values
        hashtable = {}
        for index, value in enumerate(weights):
            hashtable[value] = index
        
        # getting the indices for weight combinations

        zero_index = hashtable[list_pair[0]]

        one_index = hashtable[list_pair[1]]

        # the index combination sorted

        indices = sorted((zero_index, one_index), reverse = True)

        return hashtable
    else:
        return None


weights = [4, 4]
print(get_indices_of_item_weights(weights, 5, 8))