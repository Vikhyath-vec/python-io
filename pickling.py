import pickle

# imelda = ("more mayhem",
#           "imelda may",
#           "2011",
#           ((1, "pulling the rug"),
#            (2, "psycho"),
#            (3, "mayhem"),
#            (4, "kentish town waltz")))
#
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open("imelda.pickle", "rb") as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
#
# print(imelda2)
# album, artist, year, track_list = imelda2
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_number, track_title = track
#     print(track_number, track_title)

imelda = ("more mayhem",
          "imelda may",
          "2011",
          ((1, "pulling the rug"),
           (2, "psycho"),
           (3, "mayhem"),
           (4, "kentish town waltz")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=0)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=0)
    pickle.dump(2998302, pickle_file, protocol=0)

with open("imelda.pickle", "rb") as imelda_pickle:
    imelda2 = pickle.load(imelda_pickle)
    even_list = pickle.load(imelda_pickle)
    odd_list = pickle.load(imelda_pickle)
    x = pickle.load(imelda_pickle)

print(imelda2)
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)
print()
for i in even_list:
    print(i)
for i in odd_list:
    print(i)
print(x)
print()
# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")
# to delete a file
