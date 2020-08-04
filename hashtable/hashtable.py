class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

#Linked Listed method
class LinkedList:
    def __init__(self):
        #first node in list
        self.head = None
        self.tail = None

    def add_to_end(self,value):
        new_node = Node(value)
        #if empty set it
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.set_next(new_node)
            self.tail = new_node


    def remove_from_end(self):
        #check if list is empty
         #Yes
        if not self.head and not self.tail:
            return None
        # No
        else:
             # which node to remove the last node from?
             cur = self.head
             prev = cur

        # if the head does NOT have a next node it is the only node. Remove it
        if cur.get_next() is None:
            self.head = None
            sefl.tail = None

        else:
             # traverse the list to get last and next to last elements
             while cur.get_next() is not None:
                  #assign current to previous
                  prev = cur
                  cur = cur.get_next()
                  # end of list - set previous next node to None to remove current from list
                  prev.set_next(None)

        #return current value
        return cur.value
            

    def add_to_head(self,key,value):
        new_node = HashTableEntry(key, value)
         #if not set, set head and tail to new node varialbe
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            #otherwise set  new node to head
            new_node.set_next(self.head)
            self.head = new_node
   
    

    def remove_from_head(self):
       #check if list is empty
    # Yes - return None
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # otherwise - return value at current head.remove the value and update self.head
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value
    
    

    def get_length(self):
         # if empty return 0 length
        if not self.head:
            return 0
        else:
            # otherwise current get next element and ad 1 to length
            current = self.head
            length = 1
            while current.get_next() is not None:
                current = current.get_next()
                length = length+1
                # return length
            return length
   
    
  


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        #storage buckets
        self.data = [None]*self.capacity
     
      


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        #self.storage will hold the hash
        #return len() for number of items
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
   # https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
     # algorithm fnv-1 is
        # hash := FNV_offset_basis do
        # for each byte_of_data to be hashed
            # hash := hash × FNV_prime
            # hash := hash XOR byte_of_data
        # return hash 
        FNV_offset_basis=14695981039346656037
        FNV_prime=1099511628211

        hash=FNV_offset_basis
        # encode strings into bytes with encode()
        for x in key.encode():
            hash = hash * FNV_prime
            hash=hash^ x
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        self.data[slot] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key,None)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        hash_entry = self.data[slot]

        if hash_entry is not None:
            return hash_entry.value

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
