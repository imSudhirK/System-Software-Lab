import inc
f=open(sys.argv[1], 'r')
g=open(sys.argv[2],'w')
lines=f.readlines()
read=[]
for line in lines:
    read.append([line])
if (sys.argv[3])=0:
    k=ang_to_vec(read)
elif (sys.argv[3])=1:
    k=vec_to_arg(read)
else:
     print "1"
     exit
fieldnames=['output']
writer=csv.DictWriter(g,fielfnames=fieldnames)
writer.writeheader()
for i in range(1,len(k)+1):
    writer.writerow({'output':k[i]})
g.close()
f.close()
