import xlrd
from pypinyin import lazy_pinyin as pinyin
institutes = {}
for line in open('institute.txt','r',encoding='utf-8').readlines():
    try:elements = line.strip().split('\t')
    except:continue
    if len(elements)!=2:continue
    if elements[1].lower() not in institutes: institutes[elements[1]] = elements[0].lower()

infile = xlrd.open_workbook('kexue.xlsx').sheets()[0]
outfile = open('kexue.txt','w',encoding='utf-8')
for line in range(1,infile.nrows):
    if infile.row_values(line)[1] == '':continue
    name = infile.row_values(line)[1].replace(' ','').replace('　','').replace('（女）','')
    field = infile.row_values(line)[5]
    year = str(infile.row_values(line)[6])[:4]
    if year == '':continue
    institute = infile.row_values(line)[4]
    if '科学院' in institute:institute = 'chinese academy of sciences'
    elif institute in institutes:institute = institutes[institute]
    en = pinyin(name)
    if len(en)==2:
        q = en[1]+' '+en[0]
    elif len(en)==3:
        q = en[1]+en[2]+' '+en[0]
    elif len(en)==4:
        q = en[2]+en[3]+' '+en[0]+en[1]
    else:
        q = ' '.join(en)
    outfile.write(name+'\t'+field+'\t'+year+'\t'+q+'\t'+institute+'\n')
outfile.close()

infile = xlrd.open_workbook('gongcheng.xlsx').sheets()[0]
outfile = open('gongcheng.txt','w',encoding='utf-8')
for line in range(1,infile.nrows):
    if infile.row_values(line)[0] == '':continue
    name = infile.row_values(line)[0].replace(' ','').replace('　','').replace('（女）','')
    field = infile.row_values(line)[4]
    year = str(infile.row_values(line)[3])[:4]
    if year == '':continue
    institute = infile.row_values(line)[2]
    if '科学院' in institute:institute = 'chinese academy of sciences'
    elif institute in institutes:institute = institutes[institute]
    en = pinyin(name)
    if len(en)==2:
        q = en[1]+' '+en[0]
    elif len(en)==3:
        q = en[1]+en[2]+' '+en[0]
    elif len(en)==4:
        q = en[2]+en[3]+' '+en[0]+en[1]
    else:
        q = ' '.join(en)
    outfile.write(name+'\t'+field+'\t'+year+'\t'+q+'\t'+institute+'\n')
outfile.close()

infile = xlrd.open_workbook('changjiang.xlsx').sheets()[0]
outfile = open('changjiang.txt','w',encoding='utf-8')
for line in range(1,infile.nrows):
    if infile.row_values(line)[1] == '':continue
    name = infile.row_values(line)[1].replace(' ','').replace('　','').replace('（女）','')
    field = infile.row_values(line)[2].replace(' ','')
    if len(field)==0:field = 'none'
    year = str(infile.row_values(line)[3])[:4]
    if year == '':continue
    institute = infile.row_values(line)[0]
    if '科学院' in institute:institute = 'chinese academy of sciences'
    elif institute in institutes:institute = institutes[institute]
    en = pinyin(name)
    if len(en)==2:
        q = en[1]+' '+en[0]
    elif len(en)==3:
        q = en[1]+en[2]+' '+en[0]
    elif len(en)==4:
        q = en[2]+en[3]+' '+en[0]+en[1]
    else:
        q = ' '.join(en)
    outfile.write(name+'\t'+field+'\t'+year+'\t'+q+'\t'+institute+'\n')
outfile.close()

infile = xlrd.open_workbook('youqing.xls').sheets()[0]
outfile = open('youqing.txt','w',encoding='utf-8')
for line in range(1,infile.nrows):
    if infile.row_values(line)[0] == '':continue
    name = infile.row_values(line)[0].replace(' ','').replace('　','').replace('（女）','')
    field = infile.row_values(line)[4]
    year = str(infile.row_values(line)[5])[:4]
    if year == '':continue
    institute = infile.row_values(line)[1]
    if '科学院' in institute:institute = 'chinese academy of sciences'
    elif institute in institutes:institute = institutes[institute]
    en = pinyin(name)
    if len(en)==2:
        q = en[1]+' '+en[0]
    elif len(en)==3:
        q = en[1]+en[2]+' '+en[0]
    elif len(en)==4:
        q = en[2]+en[3]+' '+en[0]+en[1]
    else:
        q = ' '.join(en)
    outfile.write(name+'\t'+field+'\t'+year+'\t'+q+'\t'+institute+'\n')
outfile.close()

infile = xlrd.open_workbook('chuangxin.xls').sheets()[0]
outfile = open('chuangxin.txt','w',encoding='utf-8')
for line in range(1,infile.nrows):
    if infile.row_values(line)[0] == '':continue
    name = infile.row_values(line)[0].replace(' ','').replace('　','').replace('（女）','')
    field = infile.row_values(line)[4]
    year = str(infile.row_values(line)[5])[:4]
    if year == '':continue
    institute = infile.row_values(line)[1]
    if '科学院' in institute:institute = 'chinese academy of sciences'
    elif institute in institutes:institute = institutes[institute]
    en = pinyin(name)
    if len(en)==2:
        q = en[1]+' '+en[0]
    elif len(en)==3:
        q = en[1]+en[2]+' '+en[0]
    elif len(en)==4:
        q = en[2]+en[3]+' '+en[0]+en[1]
    else:
        q = ' '.join(en)
    outfile.write(name+'\t'+field+'\t'+year+'\t'+q+'\t'+institute+'\n')
outfile.close()

infile = xlrd.open_workbook('lingjun.xlsx').sheets()[0]
outfile = open('lingjun.txt','w',encoding='utf-8')
for line in range(1,infile.nrows):
    if infile.row_values(line)[1] == '':continue
    name = infile.row_values(line)[1].replace(' ','').replace('　','').replace('（女）','')
    field = infile.row_values(line)[3]
    year = str(infile.row_values(line)[4])[:4]
    if year == '':continue
    institute = infile.row_values(line)[2]
    if '科学院' in institute:institute = 'chinese academy of sciences'
    elif institute in institutes:institute = institutes[institute]
    en = pinyin(name)
    if len(en)==2:
        q = en[1]+' '+en[0]
    elif len(en)==3:
        q = en[1]+en[2]+' '+en[0]
    elif len(en)==4:
        q = en[2]+en[3]+' '+en[0]+en[1]
    else:
        q = ' '.join(en)
    outfile.write(name+'\t'+field+'\t'+year+'\t'+q+'\t'+institute+'\n')
outfile.close()

infile = xlrd.open_workbook('bajian.xlsx').sheets()[0]
outfile = open('bajian.txt','w',encoding='utf-8')
for line in range(1,infile.nrows):
    if infile.row_values(line)[1] == '':continue
    name = infile.row_values(line)[1].replace(' ','').replace('　','').replace('（女）','')
    field = infile.row_values(line)[3].replace('青年拔尖人才','')
    year = str(infile.row_values(line)[4])[:4]
    if year == '':continue
    institute = infile.row_values(line)[2]
    if '科学院' in institute:institute = 'chinese academy of sciences'
    elif institute in institutes:institute = institutes[institute]
    en = pinyin(name)
    if len(en)==2:
        q = en[1]+' '+en[0]
    elif len(en)==3:
        q = en[1]+en[2]+' '+en[0]
    elif len(en)==4:
        q = en[2]+en[3]+' '+en[0]+en[1]
    else:
        q = ' '.join(en)
    outfile.write(name+'\t'+field+'\t'+year+'\t'+q+'\t'+institute+'\n')
outfile.close()

infile = xlrd.open_workbook('jieqing.xls')
outfile = open('jieqing.txt','w',encoding='utf-8')
for sheet in range(len(infile.sheets())):
    table = infile.sheets()[sheet]
    for line in range(1,table.nrows):
        if table.row_values(line)[0] == '':continue
        name = table.row_values(line)[0].replace(' ','').replace('　','').replace('（女）','')
        field = table.row_values(line)[1]
        if field == '':field = 'none'
        year = str(1994+sheet)
        institute = table.row_values(line)[2]
        if '科学院' in institute:institute = 'chinese academy of sciences'
        elif institute in institutes:institute = institutes[institute]
        en = pinyin(name)
        if len(en)==2:
            q = en[1]+' '+en[0]
        elif len(en)==3:
            q = en[1]+en[2]+' '+en[0]
        elif len(en)==4:
            q = en[2]+en[3]+' '+en[0]+en[1]
        else:
            q = ' '.join(en)
        outfile.write(name+'\t'+field+'\t'+year+'\t'+q+'\t'+institute+'\n')
outfile.close()
