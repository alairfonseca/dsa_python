from chain_hash_map import ChainHashMap

# cyclic-shift hash code
def hash_code(s):
    mask = (1 << 32) - 1
    h = 0

    for char in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(char)

    return h


if __name__ == "__main__":
    print(hash_code("test"))
    print(hash_code("test1"))
    print(hash_code("test11"))
    print("============================")
    
    chmap = ChainHashMap()

    chmap["name"] = "chain hash map"
    chmap["test"] = "test.."
    chmap["test1"] = "test..."
    chmap["test11"] = "test...."

    for i in chmap:
        print(chmap[i])

    print("============================")
    del chmap["test1"]

    for i in chmap:
        print(chmap[i])

