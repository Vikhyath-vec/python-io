import shelve

with shelve.open("bike") as bikey:
    bikey["make"] = "Honda"
    bikey["model"] = "250 dream"
    bikey["colour"] = "red"
    bikey["engine_size"] = 250

    print(bikey["engine_size"])
    print(bikey["colour"])
