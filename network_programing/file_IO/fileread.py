# filein = open("./test.txt", "r", encoding="utf-8")

# read = filein.readline().rstrip()
# while read != "" :
#     print(read)
#     read = filein.readline()
# filein.close()

with open("./test.txt", "r", encoding="utf-8") as file :
    str = file.read().strip()
    print(str)