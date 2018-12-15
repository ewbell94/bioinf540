from math import ceil

f=open("all.list")
g=open("data.list","w")
for line in f:
    parts=line.split()
    protname=parts[0]
    parensplit=parts[3].split(")(")
    bounds=[float(parensplit[0].split("-")[0].replace("(","")),float(parensplit[0].split("-")[1]),float(parensplit[1].split("-")[0]),float(parensplit[1].split("-")[1].replace(")",""))]
    bounds.sort()
    boundary=ceil((bounds[1]+bounds[2])/2.)
    print("%d %d %d"%(bounds[1],bounds[2],boundary))
    g.write("%s,%d\n"%(protname,boundary))
f.close()
g.close()
