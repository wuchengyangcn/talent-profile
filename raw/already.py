import os
# files = [temp for temp in os.listdir(os.getcwd()) if 'txt' in temp]
files = ['jieqing_all.txt']
for file in files:
    if 'all' not in file: continue
    all = open(file,'r',encoding='utf-8').readlines()
    numbers = {}
    for line in open(file.replace('all','already'),'r',encoding='utf-8').readlines():
        elements = line.strip().split('\t')
        numbers[int(elements[0])-1] = elements[1]
    outfile = open(file.replace('all','todo'),'w',encoding='utf-8')
    for line in range(len(all)):
        # if line in numbers and numbers[line] == all[line].split('\t')[0]:continue
        if all[line].split('\t')[0] in numbers.values():continue
        outfile.write(all[line])
    outfile.close()