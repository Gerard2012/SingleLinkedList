class SLLNode(object):

    # Singly linked list node class.

    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt

    def __repr__(self):
        nval = self.nxt and self.nxt.value or None
        return f'[{self.value}: {repr(nval)}]'


class SingleLinkedList(object):

    # Singly linked list class.

    def __init__(self):
        self.head = None
        self.end = None

    def __repr__(self):
        pass


    def push(self, obj):

        # Apends a new value to the end of the list.

        if self.head == None:
            new_elem = SLLNode(obj, None)
            self.head = new_elem

        elif self.head and self.head.nxt == None:
            new_elem = SLLNode(obj, None)
            self.head.nxt = new_elem

        else:
            n = self.head.nxt
            while n.nxt != None:
                n = n.nxt
            else:
                n.nxt = SLLNode(obj, None)


    def traverse_list(self):

        # Return the contents of the list.

        if self.head == None:
            print('List is empty []')

        else:
            n = self.head
            while n != None:
                print(n.value)
                n = n.nxt


    def count(self):

        # Returns the number of items in the list.

        if not self.head:
            return 0

        else:
            x = 1
            n = self.head
            while n.nxt != None:
                x += 1
                n = n.nxt
            else:
                return x


    def first(self):

        # Returns a reference for first item in list but does not remove it.

        if not self.head:
            return None

        else:
            return self.head.value

    def last(self):

        # Return last item in the list.

        if not self.head:
            return None

        else:
            n = self.head
            while n.nxt != None:
                n = n.nxt
            else:
                return n.value


    def pop(self):

        # Removes the last item and returns it.

        if not self.head:
            return None

        elif not self.head.nxt:
            nval = self.head.value
            self.head = None
            return nval

        else:
            n = self.head
            while n.nxt != None:
                prev = n
                n = n.nxt
            else:
                prev.nxt = None
                return n.value


    def popleft(self):

        # Removes the first item and returns it.
        
        if not self.head:
            return None

        elif not self.head.nxt:
            n = self.head
            self.head = None
            return n.value

        else:
            n = self.head
            self.head = n.nxt
            return n.value


    def remove(self, obj):

        # Finds a matching item and removes it from the list.

        if not self.head:
            print('List is empty[]')
            return False

        elif self.head.value == obj:
            self.head = self.head.nxt
            return True

        else:
            n = self.head
            while n.nxt != None:
                if n.nxt.value == obj:
                    n.nxt = n.nxt.nxt
                    return True
                else:
                    print('Element not found in list[]')
                    return False


    def get(self, index):

        # Returns reference of item at given index.

        if not self.head:
            print('List is empty[]')

        elif index == 0:
            return self.head.value

        else:
            n = self.head
            node_assigned_index = 0
            while node_assigned_index < index:
                if not n.nxt:
                    return None
                else:
                    node_assigned_index += 1
                    n = n.nxt
            else:
                return n.value


    def dump(self):

        # Debugging func that dumps content of the list.

        if not self.head:
            print('List is empty[]')

        elif self.head and not self.head.nxt:
            return f'[{self.head.value}]'

        else:
            dump = f'['
            n = self.head
            while n.nxt != None:
                dump += n.value + ', '
                n = n.nxt
            else:
                dump += n.value + ']'

            return dump


if __name__ == '__main__':

    pass