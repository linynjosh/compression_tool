#!/usr/bin/env python3

import argparse
from abc import ABC, abstractmethod
import heapq

class HuffBaseNode(ABC):
    @abstractmethod
    def isLeaf(self):
        pass

    @abstractmethod
    def weight(self):
        pass

class HuffLeafNode(HuffBaseNode):
    def __init__(self, element, weight):
        self.element = element
        self._weight = weight

    def value(self):
        return self.element

    def weight(self):
        return self._weight
    
    def isLeaf(self):
        return True
    

class HuffInternalNode(HuffBaseNode):
    def __init__(self, left, right, weight):
        self._left = left
        self._right = right
        self._weight = weight

    def left(self):
        return self._left
    
    def right(self):
        return self._right

    def weight(self):
        return self._weight
    
    def isLeaf(self):
        return True
    
class HuffTree:
    def __init__(self, el=None, wt=None, l=None, r=None):
        if el is not None and wt is not None:
            self._root = HuffLeafNode(el, wt)
        elif l is not None and r is not None and wt is not None:
            self._root = HuffInternalNode(l, r, wt)
        else:
            raise ValueError("Invalid arguments for creating HuffTree")

    def root(self):
        return self._root

    def __lt__(self, other):
        return self._root.weight() < other._root.weight()

def main():
    parser = argparse.ArgumentParser(
                    prog='Compression Tool',
                    description='This challenge is to build your own command like tool to compress text files.',
                    epilog='For more information check out the link to this challenge: https://codingchallenges.fyi/challenges/challenge-huffman')
    parser.add_argument('filename')  

    args = parser.parse_args()

    char_occurrence_freq = {}

    file = open(args.filename, "r")

    for line in file:
        for char in line:
            if char not in char_occurrence_freq:
                char_occurrence_freq[char] = 1
            else:
                char_occurrence_freq[char] += 1

    heap = []

    for char in char_occurrence_freq:
        element = char
        weight = char_occurrence_freq[char]
        tree = HuffTree(el=element, wt=weight)
        heap.append(tree)

    heapq.heapify(heap)

    while len(heap) > 1:
        tmp1 = heapq.heappop(heap)
        tmp2 = heapq.heappop(heap)
        new_weight = tmp1.root().weight() + tmp2.root().weight()
        tmp3 = HuffTree(l=tmp1.root(), r=tmp2.root(), wt=new_weight)
        heapq.heappush(heap, tmp3)

    print("YAY FINISHED STEP 2")
    
if __name__ == "__main__":
    main()


class HuffBaseNode(ABC):
    @abstractmethod
    def isLeaf(self):
        pass

    @abstractmethod
    def weight(self):
        pass

class HuffLeafNode(HuffBaseNode):
    def __init__(self, element, weight):
        self.element = element
        self.weight = weight

    def value(self):
        return self.element

    def weight(self):
        return self.weight
    
    def isLeaf():
        return True
    

class HuffInternalNode(HuffBaseNode):
    def __init__(self, weight, left, right):
        self.weight = weight
        self.left = left
        self.right = right

    def left(self):
        return self.left
    
    def right(self):
        return self.right

    def weight(self):
        return self.weight
    
    def isLeaf():
        return True
    
class HuffTree:
    def __init__(self, el=None, wt=None, l=None, r=None):
        if el is not None and wt is not None:
            self.root = HuffLeafNode(el, wt)
        elif l is not None and r is not None and wt is not None:
            self.root = HuffInternalNode(l, r, wt)
        else:
            raise ValueError("Invalid arguments for creating HuffTree")

    def root(self):
        return self.root

    def weight(self):
        return self.root.weight()

    def __lt__(self, other):
        if self.root.weight() < other.weight():
            return True
        elif self.root.weight() == other.weight():
            return False
        else:
            return False