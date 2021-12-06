class newNode: 
    def __init__(self, item): 
        self.key=item
        self.left = None
        self.right = None
    
def preorder(root) :
    if (root != None) :
        print(root.key, end = " " )
        preorder(root.left) 
        preorder(root.right) 

     
def constructTrees(start, end): 
    list = [] 

    if (start > end) :
        list.append(None) 
        return list

    for i in range(start, end + 1): 
        leftSubtree = constructTrees(start, i - 1) 
        rightSubtree = constructTrees(i + 1, end) 

        for j in range(len(leftSubtree)) :
            left = leftSubtree[j] 

            for k in range(len(rightSubtree)): 
                right = rightSubtree[k] 
                node = newNode(i)   # El valor de i se vuelve el valor del nodo
                node.left = left    # El valor de left se vuelve el valor del nodo izquierdo
                node.right = right  # El valor de right se vuelve el valor del nodo derecho
                list.append(node)   # Se agrega el nodo a la lista

    return list
 
if __name__ == '__main__':
    totalTreesFrom1toN = constructTrees(1, 4) 

    print("Distinct binary trees de 1 a 4 son:\n") 
    for i in range(len(totalTreesFrom1toN)): 
        preorder(totalTreesFrom1toN[i])
        print()