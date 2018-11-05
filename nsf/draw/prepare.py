import re
for year in range(1959,2020):
    nodes = {}
    schools = {}
    number = 0
    for line in open('../'+str(year)+'.txt', 'r', encoding='utf-8').readlines():
        elements = line.strip().split('\t')
        try:
            money = int(elements[0])
            institute = elements[2]
        except:
            continue
        if institute not in schools: schools[institute] = []
        names = []
        for pos in range(3,len(elements),4):
            try:
                names.append(re.sub('[^A-Za-z]','',elements[pos])+' '+re.sub('[^A-Za-z]','',elements[pos+1])+'\t'+institute)
            except:
                pass
        for name in names:
            if name not in nodes:
                nodes[name] = [number,money,institute]
                number+=1
            else:
                nodes[name][1]+=money//len(names)
            if name not in schools[institute]:schools[institute].append(name)
    outfile = open(str(year)+'node.csv', 'w', encoding='utf-8')
    outfile.write('id,name,money,institute\n')
    barrier = 0
    while len([temp for temp in nodes if len(schools[nodes[temp][2]])>barrier])>len(nodes)*0.8: barrier+=1
    for node in nodes:
        info = nodes[node]
        if len(schools[info[2]])>=barrier:
            outfile.write(str(info[0])+','+node.split('\t')[0]+','+str(info[1])+','+info[2]+'\n')
    outfile.close()
    outfile = open(str(year)+'edge.csv', 'w', encoding='utf-8')
    outfile.write('source,target\n')
    for school in schools:
        if len(schools[school])>=barrier:
            allpeople = schools[school]
            for source in range(0,len(allpeople)-1):
                for target in range(source+1,len(allpeople)):
                    outfile.write(str(nodes[allpeople[source]][0])+','+str(nodes[allpeople[target]][0])+'\n')
    outfile.close()
