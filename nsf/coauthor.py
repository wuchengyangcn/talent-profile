import re
people = {}
for year in range(1959,2020):
    for line in open(str(year)+'.txt','r',encoding='utf-8').readlines():
        elements = line.strip().split('\t')
        try:
            money = int(elements[0])
            institute = elements[2]
        except:
            continue
        if len(elements)%4!=3:continue
        if len(elements)<=7:continue
        names = []
        leader = None
        for pos in range(3,len(elements),4):
            if elements[pos+3] == 'Principal Investigator':leader = re.sub('[^A-Za-z]','',elements[pos])+' '+re.sub('[^A-Za-z]','',elements[pos+1])+'\t'+institute
            else:names.append(re.sub('[^A-Za-z]','',elements[pos])+' '+re.sub('[^A-Za-z]','',elements[pos+1])+'\t'+institute)
        if not leader:
            leader = names[0]
            del names[0]
        if leader not in people: people[leader] = []
        for name in names:
            info = str(year)+'\t'+str(money)+'\t'+name
            if info not in people[leader]:people[leader].append(info)
outfile = open('coauthor.txt', 'w', encoding='utf-8')
for leader in people:
    if 'none' not in leader: outfile.write(leader+'\t'+'\t'.join(people[leader])+'\n')