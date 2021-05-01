# jabber = open("D:/Python/test.txt", 'r')
#
# for line in jabber:
#     if "a" in line.lower():
#         print(line, end=' ')
#
# jabber.close()

# no need to close the file when opening using with
# if there's an error in opening the file, then with will close the file automatically
# with open("D:/Python/test.txt", 'r') as jabber:
#     for line in jabber:
#         if "a" in line.lower():
#             print(line, end=" ")
# with open("D:/Python/test.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end=" ")
#         line = jabber.readline()

# with open("D:/Python/test.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines:
#     print(line, end=" ")

# with open("D:/Python/test.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line, end=" ")

with open("D:/Python/test.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end="")