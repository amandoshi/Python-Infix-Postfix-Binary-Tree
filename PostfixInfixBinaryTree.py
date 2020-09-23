import re

# tree data structure
class Tree:
    def __init__(self, pf):
        self._root = Node(pf[-1])

        # initialise tree
        self.setTree(pf[:-1])

    # initialise tree
    def setTree(self, pf):
        for val in pf[::-1]:
            self._root.addNode(val)

    def infix(self):
        return self._root.inOrderTraversal()[1:-1]

    def postfix(self):
        return self._root.postOrderTraversal()

# node data structure
class Node:
    def __init__(self, value):
        self._left = None
        self._value = value
        self._right = None

    def addNode(self, val):
        # check if rightChild is numeric value
        if self._value.isdigit():
            return False
        # add value to right child if rightChild empty
        elif self._right == None:
            self._right = Node(val)
            return True

        # recursively add value to rightChild
        check = self._right.addNode(val)

        # check if value successfully added to right child
        if check:
            return check

        # check if leftChild empty
        if self._left == None:
            self._left = Node(val)
            return True

        # add value to leftChild
        return self._left.addNode(val)

    def inOrderTraversal(self):
        # add '(' if leftChild or rightChild
        tree = '' if not any([self._left, self._right]) else '('

        # inOrderTraversal - leftChild, self._value, rightChild
        if self._left:
            tree += self._left.inOrderTraversal()

        tree += self._value

        if self._right:
            tree += self._right.inOrderTraversal()

        #add ')' if leftChild or rightChild
        return tree if not any([self._left, self._right]) else tree + ')'

    def postOrderTraversal(self):
        tree = []

        # postOrderTraversal - leftChild, rightChild, self._value
        if self._left:
            tree += self._left.postOrderTraversal()

        if self._right:
            tree += self._right.postOrderTraversal()

        tree += [self._value]

        return tree

def infix_to_postfix(exp):
    ops = ["*/", "+-"]

    # check if parentheses in equation
    if "(" in exp:
        start = None
        cnt = 0
        pos = 0

        # find parenthese - return that expression and solve recursively
        while pos < len(exp):
            if exp[pos] == '(':
                if start == None:
                    start = pos
                    cnt = 0
                cnt += 1

            elif exp[pos] == ')':
                cnt -= 1

                if cnt == 0:
                    exp[start:pos+1] = [infix_to_postfix(exp[start+1:pos])]
                    pos = start
                    start = None
                    cnt = None

            pos += 1

    # convert infix to postfix for expression with no parentheses
    for i in range(len(ops)):
        pos = 0
        while pos < len(exp):
            if exp[pos] in ops[i]:
                exp[pos-1:pos+2] = [exp[pos-1] + ' ' + exp[pos+1] + ' ' + exp[pos]]
            else:
                pos += 1

    return exp[0]

# format expression
def format(exp):
    exp = list(re.sub(r"\s+", "", exp))
    pos = 0
    found = False

    while pos < len(exp):
        if not found:
            if exp[pos] in "1234567890":
                found = True
            pos += 1
        else:
            if exp[pos] in "1234567890":
                exp[pos-1:pos+1] = [''.join(exp[pos-1:pos+1])]
            else:
                found = False
                pos += 1

    return exp

def main():
    #SIMPLE TEST
    test0 = "2+9123*23/43+35-15"
    print('test0:', test0)

    test0 = (format(test0))
    print("format:", test0)

    test0 = infix_to_postfix(test0)
    print("infix:", test0)

    #COMPLEX TEST
    #Solution: 100 23 4 * 11 - - 12 +
    test1 = '(100-(23*4-11))+12'
    print("\ntest1:", test1)

    test1 = format(test1)
    print("format:", test1)

    test1 = infix_to_postfix(test1)
    print("infix:", test1)

    #COMPLEX TEST 2
    #Solution: 100 7 3 1 - * 6 + - 10 +
    test2 = '(100-((7*(3-1))+6))+10'
    print('\ntest2:', test2)

    test2 = format(test2)
    print("format:", test2)

    test2 = infix_to_postfix(test2)
    print("postfix:", test2)

    # create binary tree
    binaryTree = Tree(test2.split(' '))
    print("\ninfix: {}".format(binaryTree.infix()))
    print("postfix: {}".format(' '.join(binaryTree.postfix())))


    # solution 100 30 4 3 2 * / - * 2 4 3 - * -
    test3 = '(100*(30-(4/(3*2)))) - 2*(4-3)'
    print('\ntest3:', test3)

    test3 = format(test3)
    print("format:", test3)

    test3 = infix_to_postfix(test3)
    print("postfix:", ''.join(test3))

    binaryTree2 = Tree(test3.split(' '))
    print("\ntree infix: {}".format(binaryTree2.infix()))
    print("tree postfix: {}".format(' '.join(binaryTree2.postfix())))


if __name__ == "__main__":
    main()
