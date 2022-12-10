class sdclass:
    mul = 2

    @classmethod
    def aclassmethod(cls, newMul):
        cls.mul = newMul
        print('Class Method')

    def ainstancemethod(self, number):
        return self.mul * number

    @staticmethod
    def astaticmethod():
        print('Hello')


if __name__ == '__main__':
    sd = sdclass()
    x = sd.ainstancemethod(2)
    print(x)
    assert x == 4, 'X should have been 4'
    sd.astaticmethod()
    sdclass.aclassmethod(3)
    y = sd.ainstancemethod(2)
    print(y)

