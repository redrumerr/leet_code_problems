class MyHashSet(object):

    def __init__(self):
        self.lst = []
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.lst:
            self.lst.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.lst:
            self.lst.remove(key)

        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key in self.lst:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)