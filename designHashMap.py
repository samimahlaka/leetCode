class MyHashMap(object):

    def __init__(self):
        self.capacity = 10000001;
        self.set = [None]*self.capacity;
    
    def hash(self, key):
        return key % self.capacity;

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        address = hash(key);
        if self.set[address] is None:
            self.set[address] = [key, value];
        else:
            self.set[address][1] = value;
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        address = hash(key);
        if self.set[address] is not None:
            return self.set[address][1];
        else:
            return -1;

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        address = hash(key);
        if self.set[address] is not None:
            self.set[address] = None;
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key