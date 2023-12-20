def simplify(func, *args, **kwargs):
    def simplified(*s_args, **s_kwargs):
        return func(*args, *s_args, **kwargs, **s_kwargs)
    return simplified


def foo(prefix, a, b):
    print("fooness:", prefix, a, b)


def bar(prefix, a, b, sufix=None):
    print("barness:", prefix, a, b)
    print("barness: +", sufix)


foo("baseline:", 0, 0)
f = simplify(foo, "MEGA:")
f(1, 2)

print('-'*20)

bar("baselne:", 0,0)
bar("baselne:", 0,0, sufix="EOF")
b = simplify(bar, "This is the end", sufix="my only friend")
b(1, 2)

