def main():
    f = open("newfile.txt","w+")
    #f = open("newfile.txt","a+")
    for i in range(10):
        f.write("This is line %d\r\n"%(i+1))
    f.close()
   
    #Open the file back and read the contents
    #f = open("newfile.txt","r")
    #    if f.mode == 'r':
    #        contents=f.read()
    #        print contents
    #or, readlines reads the individual line into a list
    #fl = f.readlines()
    #for x in fl:
    #print x
main()      #a newfile.txt is created