class Base():
    def __init__(self):
        self.a = 'a'

    def amethod(self):
        print 'amethod from base'

class Derived(Base):
    def amethod(self):
        Base.amethod(self)
        print 'amethod from derived'
