import sys

length =len(sys.argv)

if length > 5 or length < 3:
    print("parameter error")
    exit(-1)

if sys.argv[0] == "file_L":
    print("file_L")
elif sys.argv[0] == "file_H":
    print("file_H")
elif sys.argv[0] == "":
    print("filesystem")
elif sys.argv[0] == "":
    print("network")
elif sys.argv[0] == "storage":
    print("storage")
elif sys.argv[0] == "olt_pre":
    print("olt_pre")
elif sys.argv[0] == "olt_run":
    print("olt_run")
