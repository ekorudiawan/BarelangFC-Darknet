jumlah_file = 1000
f = open("train.txt","w") #opens file with name of "test.txt"
for x in range(1, jumlah_file+1):
    f.write("/home/master/robot/data_images/bola/bola%d.jpg\n"%x)
for x in range(1, jumlah_file+1):
    f.write("/home/master/robot/data_images/gawang/gawang%d.jpg\n"%x)
for x in range(1, jumlah_file+1):
    f.write("/home/master/robot/data_images/acak/acak%d.jpg\n"%x)
f.close()
