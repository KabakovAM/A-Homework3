class linked_list:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    
    def append(self, data):
        end = linked_list(data)
        n = self
        while (n.next):
            n = n.next
        n.next = end


def print_list(ll):
    while ll:
        print(ll.data, end=' -> ' if ll.next else '')
        ll = ll.next
    print('\n')


def reverse_list(ll, tail=None):
    while ll:
        ll.next, tail, ll = tail, ll, ll.next
    return tail

ll = linked_list(0)
for i in range(1, 10):
    ll.append(i)

print_list(ll)
print_list(reverse_list(ll))
