
class baseClass(object):
    def sub(self):
        print("1")


class parentClass(baseClass):
    def parent(self):
        # in python3
        # super().sub()
        # in python2
        super(parentClass, self).sub()
        print("2")


a = parentClass().parent()
