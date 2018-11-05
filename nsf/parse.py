from xml.dom.minidom import parse as p
import os
for year in range(1959, 2020):
    folder = str(year)
    path = os.getcwd()+'/'+folder
    outfile = open(folder+'.txt', 'w', encoding='utf-8')
    for infile in os.listdir(path):
        if 'xml' not in infile: continue
        try:page = p(path+'/'+infile).documentElement
        except:continue
        try:amount = page.getElementsByTagName('AwardAmount')[0].childNodes[0].data
        except:amount = 'none'
        try:field = page.getElementsByTagName('Directorate')[0].getElementsByTagName('LongName')[0].childNodes[0].data
        except:field = 'none'
        try:institute = page.getElementsByTagName('Institution')[0].getElementsByTagName('Name')[0].childNodes[0].data
        except:institute = 'none'
        outfile.write(amount+'\t'+field+'\t'+institute)
        try:
            people = page.getElementsByTagName('Investigator')
        except:
            outfile.write('\n')
            continue
        for person in people:
            try:firstname = person.getElementsByTagName('FirstName')[0].childNodes[0].data
            except:firstname = 'none'
            try:lastname = person.getElementsByTagName('LastName')[0].childNodes[0].data
            except:lastname = 'none'
            try:emailaddress = person.getElementsByTagName('EmailAddress')[0].childNodes[0].data
            except:emailaddress = 'none'
            try:rolecode = person.getElementsByTagName('RoleCode')[0].childNodes[0].data
            except:rolecode = 'none'
            outfile.write('\t'+firstname+'\t'+lastname+'\t'+emailaddress+'\t'+rolecode)
        outfile.write('\n')
    outfile.close()
