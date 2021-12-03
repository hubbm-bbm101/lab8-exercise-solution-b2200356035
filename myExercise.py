import sys
f = open(sys.argv[1], "r")
dictionary = dict()
check = sys.argv[2]
for i in f:
    i = i.rstrip("\n")
    i = i.split(":")
    dictionary[i[0]] = i[1]
check = check.split(",")
for i in check:
    try:
        print("Name: {}, University: {}".format(i, dictionary[i]), end=" ")
    except KeyError:
        print("No record of {} was found".format(i))
