from traits.api import *


class Child(HasTraits):
    name = Str
    age = Int
    doing = Str

    def __str__(self):
        return '%s<%x>' % (self.name, id(self))

    # 静态监听age属性变化
    def _age_changed(self, old, new):
        print('%s.age changed: from %s to %s' % (self, old, new))

    # 静态监听任何Trait属性的变化
    def _anytrait_changed(self, name, old, new):
        print('anytrait changed: %s.%s from %s to %s' % (self, name, old, new))

    @on_trait_change('age')
    def print_info(self):
        print('age', 'has changed')


def log_trait_changed(obj, name, old, new):
    print('log %s.%s changed from %s to %s' % (obj, name, old, new))
