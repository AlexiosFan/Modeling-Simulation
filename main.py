# since S is a set, we are sure that all Si are distinct, thus we can store the input data in a hashmap.
# Here in python we just use the dictionary, thus we assume the input data is given by a dictionary

def find_banzhaf(hashmap, quorum):
    # An iteration is indeed necessary. Since quorum is greater equal 50%, a top down iteration saves time and memory.
    keys = list(hashmap.keys())
    index = 0
    subsets = [keys]
    while len(subsets) > 0:
        subset = subsets.pop()
        weights = sum([hashmap[k] for k in subset])
        if weights < quorum:
            continue
            # we stop here when the sum of the subset cannot reach the limit
        else:
            for k in subset:
                if weights - hashmap[k] < quorum:
                    index += 1
                    # if it is on the border, we increment index, and ignore the new subset
                else:
                    newset = subset
                    newset.remove(k)
                    subsets.append(newset)
                    # if the subset is not on the border, we add the new subset to the cache
    # all subsets can reach the limit using top down iteration, thus we end it when the cache is empty
    return index


print(find_banzhaf({1:10, 2:5, 3:4}, 10))
