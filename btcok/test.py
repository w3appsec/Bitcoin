import re

with open('pub') as f:
    l = '0x'+f.readline()
l = re.sub('[L]', '', l)
pub = int(l, 0)
#print(str(hex(pub)))

keycode = pub >> (64 * 8)
#print(keycode)

ff32 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

x = (pub >> (32 * 8)) & ff32 
#print(str(hex(x)))

y = pub & ff32
#print(str(hex(y)))

compcode = 0x02
compress = '0x02'
if y & 1:
    #print ('odd')
    compcode = 0x03
    compress = '0x03'
#else:
    #print ('even')
compkey = compcode << (32 * 8)
xstr = str(hex(x))
#print(str(hex(compkey | x)))
#print(len(xstr))
#print(compress+xstr)

if len(xstr) == 66:
    #print('ok')
    ok = 1
elif len(xstr) == 65: 
    print('low')
    compress = compress + '0'
else:
    print('wtf')

print(compress+xstr[2:])
