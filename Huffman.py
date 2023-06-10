class BinaryTree:
    def __init__(self, symbol=None, prob=0, level=0):
        # Initialize binary tree       
        self.left = None
        self.right = None
        self.symbol = symbol
        self.prob = prob
        self.level = level
        
    def dumpTree(self):
        # dump nodes in the tree
        if self.left:
            self.left.dumpTree()
        print(f"{self.symbol}: {self.prob}")
        if self.right:
            self.right.dumpTree()
        
    def buildTree(self, codeBook):
        """Build a code book
        Parameters:
            - codeBook (list): a list containing symbol and its code. 
                E.g.: [{"symbol": "a", "prob": 0.6}, # 1
                       {"symbol": "b", "prob": 0.3}, # 01
                       {"symbol": "c", "prob": 0.1}] # 00
        Return:
            - An instance of BinaryTree that contains all symbol in codeBook. 
            - If codeBook is not a Huffman code, then return None
        """
        nodes = []
        for symbol, prob in codeBook:
            nodes.append(BinaryTree(symbol, prob))
        
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.prob)
            left = nodes[0]
            right = nodes[1]
            parent = BinaryTree(None, left.prob + right.prob)
            parent.left = left
            parent.right = right
            nodes = nodes[2:]
            nodes.append(parent)
        
        if len(nodes) == 0:
            return None
        
        return nodes[0]
        
    def decode(self, binaryString):
        '''Decode binaryString into a sequence of source symbols. 
        Paramters:
            - binaryString: the input binary string. 
        Return:
            - None if the binary tree is not built. 
            - None if the input binaryString is not a binary string 
            - None if the input binaryString cannot decodable.
            - Otherwise return a list of source symbols in the codebook
        '''
        if not self:
            return None
        tmp_node = self
        solution = ''
        for i in binaryString:
            if tmp_node:
                if i == '1':
                    if not tmp_node.right:
                        return None
                    tmp_node = tmp_node.right
                elif i == '0':
                    if not tmp_node.left:
                        return None
                    tmp_node = tmp_node.left
                else:
                    return None
                if tmp_node.symbol:
                    solution += tmp_node.symbol
                    tmp_node = self
                    
        if not tmp_node.symbol:
            return None
        return solution

