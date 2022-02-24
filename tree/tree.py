from node import Node


if __name__ == "__main__":
    tree = Node('drinks', [])
    cold = Node('cold', [])
    hot = Node('hot', [])
    
    tree.add_child(cold)
    tree.add_child(hot)
    
    tea = Node('tea', [])
    coffee = Node('coffee', [])

    cola = Node('cola', [])
    fanta = Node('fanta', [])

    cold.add_child(cola)
    cold.add_child(fanta)

    hot.add_child(tea)
    hot.add_child(coffee)

    print(tree)
