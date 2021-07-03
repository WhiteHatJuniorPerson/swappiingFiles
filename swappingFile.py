def swappingFile():
    f1=open("sample1.txt")
    f2=open("sample2.txt")
    r1=f1.read()
    r2=f2.read()
    fw1=open("sample1.txt","w")
    fw2=open("sample2.txt","w")
    fw2.write(r1)
    fw1.write(r2) 

swappingFile()
