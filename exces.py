class A():
    def __len__(self):
        return 0

class B():
    def __nonzero__(self):
        return 0

a = A()
bool        