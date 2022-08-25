# python3

def build_trie(patterns):
    tree = {}
    new_node = 0
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            if tree.__contains__(current_node) and tree[current_node].__contains__(current_symbol):
                current_node = tree[current_node].get(current_symbol)
            else:
                new_node = new_node + 1
                if not tree.__contains__(current_node):
                    tree[current_node] = {}
                    tree[current_node][current_symbol] = new_node
                else:
                    tree[current_node][current_symbol] = new_node
                current_node = new_node
    return tree


if __name__ == '__main__':
    n_patterns = int(input())
    patterns = list(input() for _ in range(n_patterns))
    tree = build_trie(patterns)
    for node in tree:
        for char in tree[node]:
            print("{}->{}:{}".format(node, tree[node][char], char))
