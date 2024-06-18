import os
#운영체제의 정보 하드웨어 정보

#for i,j in os.environ.items():
#    print(i,j,sep=" : ")

#print(os.getenv('PROGRAMFILES')+"\\Hello_World")


print(os.stat("teest.bat")[0])
os.chmod("teest.bat",0o00)
print(os.stat("teest.bat")[0])
