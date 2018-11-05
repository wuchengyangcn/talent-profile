import os
files = [temp for temp in os.listdir(os.getcwd()) if 'txt' in temp]
name2id = {}
id2name = {}
name2count = {}
id2paper = {}
paper2id = {}
name2field = {}
name2year = {}
for file in files:
    if 'tag' not in file: continue
    flush = open(file.replace('tag','co'),'w',encoding='utf-8')
    flush.close()
    for line in open(file,'r',encoding='utf-8').readlines():
        elements = line.strip().split('\t')
        name = elements[0] + file.split('_')[0]
        field = elements[1]
        year = int(elements[2])
        if name not in name2field: name2field[name] = field
        if name not in name2year: name2year[name] = [year, 0]
for file in files:
    if 'list' not in file: continue
    count = 1
    for line in open(file,'r',encoding='utf-8').readlines():
        elements = line.strip().split('\t')
        name = elements[1]+'\t'+elements[3]
        if name not in name2id: name2id[name] = []
        if elements[4] not in name2id[name]:name2id[name].append(elements[4])
        id2name[elements[4]] = name
        if elements[4] not in id2paper: id2paper[elements[4]] = []
        if name not in name2count:
            name2count[name] = file.split('_')[0]+'_'+str(count)
            count+=1
for file in files:
    if 'data' not in file: continue
    for line in open(file,'r',encoding='utf-8').readlines():
        elements = line.strip().split('\t')
        if elements[0] not in id2name:continue
        if len(elements)<3: continue
        for paper in elements[2].split(' '):
            if paper not in id2paper[elements[0]]:id2paper[elements[0]].append(paper)
            if paper not in paper2id:paper2id[paper] = []
            if elements[0] not in paper2id[paper]:paper2id[paper].append(elements[0])
        name = id2name[elements[0]].split('\t')[0]+file.split('_')[0]
        try: name2year[name][1]+=int(elements[1].split(' ')[name2year[name][0]-2019])
        except: pass
for name in name2count:
    outfile = open(name2count[name].split('_')[0]+'_co.txt','a',encoding='utf-8')
    short = name.split('\t')[0]+name2count[name].split('_')[0]
    if short in name2field: field = name2field[short]
    else: field = 'none'
    if short in name2year:
        year = str(name2year[short][0])
        cite = str(name2year[short][1])
    else:
        year = 'none'
        cite = 'none'
    outfile.write(name2count[name]+'\t'+name+'\t'+field+'\t'+year+'\t'+cite)
    for source in name2id[name]:
        for paper in id2paper[source]:
            for target in paper2id[paper]:
                try:
                    if id2name[target] != name: outfile.write('\t'+name2count[id2name[target]])
                except:print('error')
    outfile.write('\n')
    outfile.close()
