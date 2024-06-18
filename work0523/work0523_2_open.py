#C language: File f = fopen("path","mode")

#f = open("test.csv","w")
#f.write("Hello world")      #fprint, fputs
#f.close()       # fclose(f)

with open("../test.csv", "r") as f:
    for i in f:
        print(i.split(" "))
