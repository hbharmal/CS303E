class Link (object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularList(object):
    def __init__ (self): 
        self.first = None
        self.num_links = 0

    def insert (self, item):
        if self.num_links == 0:
          self.first = Link(item)
        elif self.num_links == 1:
            current = self.first
            current.next = Link(item)
            current.next.next = self.first
            current.prev = self.first.next
            current.prev.prev = self.first
        else:
            first = self.first
            current = self.first
            while (current.next != first):
                current = current.next
            current.next = Link(item)
            current.next.prev = current
            current.next.next = self.first
            current.next.next.prev = current.next
        self.num_links += 1

    def find (self, key):
        if(self.first.data == key):
            return self.first
        current = self.first.next
        first = self.first
        while current != first:
            if (current.data == key):
                return current
            current = current.next
        return None

    def delete (self, key):
        pros = Link(key)
        current = self.first
        first = self.first
        while current != first:
            if (current == pros):
                current.prev.next = current.next
                self.num_links -=1
            current = current.next
        return None

    def delete_after (self, start, n):
        i = 1
        n = n
        current = self.find(start)
        while i < (n):
            current = current.next
            i = i + 1
        if current == self.first:
            self.first = current.next
        current.next.prev = current.prev
        current.prev.next = current.next
        self.num_links -=1
        return current.prev.next, current

    def __str__ (self):
        string = ""
        current = self.first
        for i in range(self.num_links):
            if current and current.data != None:
                string += str(current.data) + "  "
                current = current.next
        return string

def main():
    
    in_file = open("testcase3.txt", "r")
    num_soldiers = int(in_file.readline().strip())
    num_start = int(in_file.readline().strip())
    elim_num = int(in_file.readline().strip())
    in_file.close()

    group = CircularList()
    for i in range(1, num_soldiers + 1):
      group.insert(i)
    new_start = num_start
    for i in range(num_soldiers - 1):
      new_start, last = group.delete_after(new_start, elim_num)
      last = last.data
      new_start = new_start.data
      print(last)
    print(group)

main()  