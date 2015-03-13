class SuperStr(str):

    def is_repeatance(self, s=''):
        if type(s) is not str or self == '':
            return False
        return s*self.count(s) == self

    def is_palindrom(self):
        return self.lower() == ''.join(reversed(self.lower()))


s2 = SuperStr('')
print s2.is_repeatance('')
print s2.is_repeatance('a')



