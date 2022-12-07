class MyHashSet(object):

    def __init__(self):
        self.capacity= 1000001;
        self.set = [None]*self.capacity;

    def hash(self, key): 
       return key % self.capacity;

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        address = hash(key);
        if self.set[address] is None :
            self.set[address] = [];
            self.set[address]=key;
        
        #else:
        #  self.set[address].append(key);

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        address = hash(key);
        if self.set[address] is not None:
            #if key in self.set[address]:
                self.set[address] = None;

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        address = hash(key);
        if self.set[address] is not None:
            #if key in self.set[address]:
                return True;
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)