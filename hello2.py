def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, unicode) else 2

    for i in xrange(0, len(src), length):
        s = src[i:i+length]
        hexa = b' '.join(["{0:0{1}X}".format(ord(x), digits) for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.'  for x in s])
        result.append( b"{0:04X}   {1:<{2}s}   {3}".format(i, hexa, length*(digits + 1), text) )

    print b'\n'.join(result)


hexdump("hello,world!hello,world!")