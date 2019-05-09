input_file=open('a.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while(1>=1):
        s=s+line[1-1]
        l=l-1
    print(s)
input_file.close()