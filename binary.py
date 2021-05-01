# with open("binary", 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))
#
# with open("binary", 'br') as binfile:
#     for b in binfile:
#         print(b)
a = 65534  # FF FE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
d = 2998302  # 02 2D C0 1E
with open("binary2", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'little'))

with open("binary2", 'br') as binfile:
    e = int.from_bytes(binfile.read(2), 'big')
    f = int.from_bytes(binfile.read(2), 'big')
    g = int.from_bytes(binfile.read(4), 'big')
    h = int.from_bytes(binfile.read(4), 'big')
    i = int.from_bytes(binfile.read(4), 'big')  # bytes were in reverse order
    print(e, f, g, h, i)
