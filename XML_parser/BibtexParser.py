# -*- coding:utf-8 -*-

import bibtexparser
import re
import json
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bs4 import BeautifulSoup
import urllib2
import ssl
import requests
import sys
import string
class BibtexParser:
    def __init__(self, BibtexfilePath, BibtexContent):
        self.BibtexfilePath = BibtexfilePath
        self.BibtexContent = BibtexContent
        self.BibTeXtype={}
        self.show_properties=['author','editor','title','journal','publisher','booktitle','year','volume','number','pages','month']
        self.BibTeXtype['article']={'required':['author','title','journal','year'],
                                    'optional':['volume','number','pages','month','note']}
        self.BibTeXtype['book'] = {'required': ['author', 'title', 'publisher', 'year'],
                              'optional': ['volume', 'series', 'address', 'edition', 'month', 'note']}
        self.BibTeXtype['booklet'] = {'required': ['title'],
                                 'optional': ['author', 'howpublished', 'address', 'month', 'year', 'note']}
        self.BibTeXtype['inbook'] = {'required': ['author', 'title', 'chapter', 'publisher', 'year'],
                                'optional': ['volume', 'series', 'type', 'address', 'edition', 'month', 'note']}
        self.bibtex=''
        self.allbibtex=[]
        self.prep = ['in', 'on', 'and', 'by', 'with', 'at', 'after', 'of', 'before', 'as', 'for', 'and', 'or', 'nor', 'to']
        self.artie = ['a', 'the', 'an', 'via']
        self.tilte = ''

    def openfile(self):
        with open(self.BibtexfilePath) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            ENTRYTYPE = bib_database.entries[0]['ENTRYTYPE']# article
            self.bibtex = bib_database.entries[0]
            self.allbibtex = bib_database.entries
    def readcontent(self):
        bib_database = bibtexparser.loads(self.BibtexContent)
        self.allbibtex = bib_database.entries

    # 得到一个人名字的简写
    def getRealName(self, string):
        # print '删除空格之前长度',len(string)
        string = string.strip()  # 删除字符串收尾的空格
        # print string
        # print len(string)
        name = re.split('[, .]', string)  # 用','' ''.'将名字进行分割
        # print name
        num = len(name)
        namenew = []
        # 移除list里空白字符
        for i in range(0, num):
            # print name[i]
            if name[i] != '':
                # name.remove('')
                namenew.append(name[i])
        # print namenew
        # print len(namenew)
        name = ''
        for i in range(0, len(namenew)):
            if i == 0:
                name = namenew[i] + ' '
            elif i == len(namenew[i]) - 1:  # 第一个单词取全拼，其余选首字母并大写
                name = name + namenew[i][0].upper()
            else:
                name = name + namenew[i][0].upper() + ' '
        #print name
        return name.strip()

    def getTitle(self, string):
        return string

    def getJournal(self, string):
        return string


    def getTextTitle(self):
        with open(self.BibtexfilePath) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            allbibtex = bib_database.entries
            titles=[]
            for i in range(0, len(allbibtex)):
                bibtex = allbibtex[i]
                if bibtex.has_key('title'):
                    titles.append(bibtex['title'])
                else:
                    titles.append('')
        return titles


    def getkey(self):
        with open(self.BibtexfilePath) as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            allbibtex = bib_database.entries
            keys = []
            for i in range(0, len(allbibtex)):
                bibtex = allbibtex[i]
                if bibtex['ENTRYTYPE'] == 'proceedings':
                    continue
                if bibtex.has_key('ID'):
                    keys.append(bibtex['ID'])
                else:
                    keys.append('')
        return keys


    def gettextbykey(self):
        self.openfile()
        result = []
        keys = []
        titles = []
        years = []
        for i in range(0, len(self.allbibtex)):
            bibtex = self.allbibtex[i]
            #print(bibtex['ENTRYTYPE'])
            if bibtex['ENTRYTYPE'] == 'proceedings':
                continue
            keys.append(bibtex['ID'])
            text = ''
            for show_property in self.show_properties:
                if bibtex.has_key(show_property):
                    name = ''
                    if show_property == 'author' or show_property == 'editor':
                        # print(bibtex[show_property])
                        author = bibtex[show_property].replace("\n", " ")
                        # print(author)
                        names = author.split(' and ')
                        # getRealName(names[0])
                        for i in range(0, len(names)):
                            temp_name = self.getRealName(names[i])
                            print('temp_name', temp_name)
                            if i < 3:
                                name = name + temp_name + ', '
                            elif i >= 3:
                                name = name + 'et al.'
                                break
                    #     print type(name)
                        name = name.strip()
                    #     print type(name)
                        if name[-1] == ',':
                        # name=name.ToString().Substring(0,name.length-1)
                        # name_temp=list[name]
                        # name_temp.pop()
                        # name_temp.append('.')
                        # name=''.join(name_temp)
                            name = name.strip(',') + '. '
                        if name[-1] == '.':
                            name = name + ' '
                        text = text + name
                    #title = ''
                    if show_property == 'title':
                        title = self.getTitle(bibtex[show_property]) + '. '
                        title = title.replace('\n',' ')
                        titles.append(title)
                        text = text + title
                    if show_property == 'journal' or show_property == 'booktitle' or show_property == 'publisher':
                        journal = self.getJournal(bibtex[show_property]) + ', '
                        #print(journal)
                        journal = journal.replace('\n', ' ')
                        journal = journal.replace('{', '')
                        journal = journal.replace('}', '')
                        text = text + journal
                    if show_property == 'year':
                        year = bibtex[show_property] + ', '
                        years.append(bibtex[show_property])
                        text = text + year
                    if show_property == 'volume':
                        volume = bibtex[show_property]
                        text = text + volume
                    if show_property == 'number':
                        number = '(' + bibtex[show_property] + ')'
                        text = text + number
                    if show_property == 'pages':
                        pages = ':' + bibtex[show_property]
                        text = text + pages
            text = text.strip()
            text = text.strip(',')
            result.append(text+'.')
        print('result', result)
        print('keys', keys)
        print('titles', titles)
        print('years', years)

        return result, keys, titles, years
    def getMap(self):
        url = 'https://www.ccf.org.cn/xspj/jsjwl/'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'lxml', from_encoding="gb18030")
        # print soup
        # print soup.prettify()

        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')
        # 序号 刊物名称
        # body > div.main.m-b-md > div > div.focusList.row > div.col-md-10 > div > ul:nth-of-type(4) > li:nth-of-type(1)

        #rate = soup.select('body > div.main.m-b-md > div > div.focusList.row > div.col-md-10 > div > ul:nth-of-type(5)')
        # body > div.main.m-b-md > div > div.focusList.row > div.col-md-10 > div > ul:nth-child(6)
        # body > div.main.m-b-md > div > div.focusList.row > div.col-md-10 > div > ul:nth-child(8)
        st = ['', '', '']
        st[0] = 'body > div.main.m-b-md > div > div.focusList.row > div.col-md-10 > div > ul:nth-of-type(4)'
        st[1] = 'body > div.main.m-b-md > div > div.focusList.row > div.col-md-10 > div > ul:nth-of-type(5)'
        st[2] = 'body > div.main.m-b-md > div > div.focusList.row > div.col-md-10 > div > ul:nth-of-type(6)'
        rate = [soup.select(i)[0] for i in st]

        for i in rate:
            s = str(i.get_text())
        ss = s.strip().split('\n')
        m = {}
        for i in range(len(ss)):
            if i < 5:
                continue
            elif ss[i] == '':
                continue
            if (i - 5) % 7 == 3: #
                value = ss[i]
            elif (i - 5) % 7 == 4:
                key = ss[i]
            elif (i - 5) % 7 == 5:  # 出版社
                publish = ss[i]
                m[key] = [value, publish]
        return m

    def formatText(self):
        if self.BibtexfilePath != '':
            self.openfile()
        else:
            self.readcontent()

        m = self.getMap()
        m['IEEE Global Communications Conference'] = m['IEEE Global Communications Conference, incorporating the Global Internet Symposium']
        del m['IEEE Global Communications Conference, incorporating the Global Internet Symposium']
        print m

        length = 0
        nb = {}
        for bibtex in self.allbibtex:
            for key in bibtex.keys():
                if len(key) > length and key != 'ENTRYTYPE':
                    length = len(key)
            for k, v in bibtex.items():
                if k == 'ENTRYTYPE' or k == 'ID':
                    nb[k] = v
                    continue
                elif k == 'ID':
                    nb[k] = v
                    continue
                elif k == 'doi' or k == 'ISSN' or k == 'keywords':
                    continue
                elif v == '':
                    continue
                elif 'url' in k:
                    continue

                nk = k + (length - len(k)) * ' '

                if 'booktitle' in nk:
                    if '(' in v:
                        v1 = v.split('(')[1].split(')')[0]
                        nb[nk] = 'Proc. of ' + v1
                        continue
                    flag = 0 # 未更改booktitle

                    to_remove = "~`!@#$%^&*(){}[];':<>|-=_+"
                    table = {ord(char): None for char in to_remove}
                    clean_v = v.translate(table)

                    #clean_v = v.translate(string.punctuation)
                    #print clean_v
                    for kk, vv in m.items():
                        if kk in clean_v:
                            nb[nk] = 'Proc. of ' + vv[0]
                            publish = 'publish' + (length - 7) * ' '
                            nb[publish] = vv[1]
                            flag = 1
                            break
                    if flag == 0:
                        nb[nk] = v
                        print v
                    continue

                elif nk.strip() == 'title' and 'booktitle' not in nk:
                    self.tilte = v
                    nv = v.split(' ')
                    for i in range(len(nv)):
                        # 标题除介词和冠词外，首字母大写
                        if nv[i] in self.prep or nv[i] in self.artie:
                            continue
                        # 首字母大写
                        else:
                            if 97 <= ord(nv[i][0]) <= 122:
                                nv[i] = chr(ord(nv[i][0])-32)+nv[i][1:]

                    v = ' '.join(nv)
                    nb[nk] = '{' + v + '}'
                    continue

                elif 'pages' in nk:
                    if '--' in v:
                        nb[nk] = v
                        continue
                    nb[nk] = v.replace('-', '--')
                    continue
                elif 'author' in nk:
                    if '\n' in v:
                        nb[nk] = v.replace('\n', ' ')
                        continue

                # 其他不做改变
                nb[nk] = v

            db = BibDatabase()
            db.entries = [nb]
            writer = BibTexWriter()
            writer.indent = '\t'  # indent entries with 4 spaces instead of one
            writer.comma_first = False  # place the comma at the beginning of the line
            with open(self.tilte+'.bib', 'wb') as bibfile:
                bibfile.write(writer.write(db))



# if __name__ == '__main__':
#     test()
#     # path = "/Users/beddingearly/studio/Web-Based-Personal-Research-Assistant-System/test.bib"
#     # b = BibtexParser(path)
#     # b.formatText()
#     # print b.getTextTitle()
#     # #print b.gettextbykey()

