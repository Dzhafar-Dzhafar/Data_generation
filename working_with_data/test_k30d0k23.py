from itertools import groupby

a = 'abc'
b = 'abc'
c = 'zzz'
d = 'ooo'
x = [a, b, c, d]

new_x = [el for el, _ in groupby(x)]
mod = '\n'.join(new_x)
print(mod)
