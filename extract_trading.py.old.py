#!/usr/bin/python
import urllib2,re,html2text
import sqlite3
from datetime import datetime

def getIndex():
    mse_index = " ".join(urllib2.urlopen('http://www.borzamalta.com.mt').read().decode('utf8').split())
    global mse_clean 
    mse_clean = html2text.html2text(mse_index)

def extractTables():
    global mse_table
    global mse_equities_table
    global mse_mgs_table
    global mse_bonds_table
    def cleanTable(table):
        x = table
        x = re.sub(r'\(.+?\)', '', x)
        x = re.sub(r'\|[\n]','|', x)
        return x
    mse_table_re = re.search('Regular Market(.+?)Treasury', mse_clean, re.DOTALL)
    mse_table = mse_table_re.group(1)
    mse_equities_re = re.search('(\(Equities.+?)\(Stocks', mse_table, re.DOTALL)
    mse_equities_table = cleanTable(mse_equities_re.group(1))
    mse_mgs_re = re.search('(\(Stocks.+?)\(Corporate', mse_table, re.DOTALL)
    mse_mgs_table = cleanTable(mse_mgs_re.group(1))
    mse_bonds_re = re.search('(\(Corporate.*$)', mse_table, re.DOTALL)
    mse_bonds_table = cleanTable(mse_bonds_re.group(1))

def formatEqTable(table):
    x = table.replace("| ","",1)
    return formatTable(x)

def formatTable(table):
    x = table.replace(" | ","|")
    x = x.replace(" |","|")
    x = x.replace("| ","|")
    x = x.replace("|","#")
    x = x.replace("  "," ")
    x = x.replace("Open\nPrice","Open Price")
    x = x.replace(",","")
    x = x.replace("[", "")
    x = x.replace("]", "").strip()
    return x
    
def printTable(data):   # ----- METHOD NOT CURRENTLY IN USE
    x_width = max(len(word) for row in data.split("\n") for word in row.split("#")) + 5

    for row in data.split("\n"):
        for word in row.split("#"):
            print "".join(word.strip().rjust(x_width)),
        print

def behead(table):
    table = table.replace("\n","#")
    behead_re = re.search('- #(.*)', table, re.DOTALL)
    return behead_re.group(1).strip()

getIndex()
extractTables()

mse_equities = formatEqTable(mse_equities_table)

dbconnection = sqlite3.connect('/home/django/investments/db.investments')
dbdo = dbconnection.cursor()
dbdo.execute('CREATE TABLE IF NOT EXISTS mse_trades (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, DATE datetime NOT NULL, TICKER varchar(6) NOT NULL, VOLUME integer NOT NULL, VALUE real NOT NULL, TRADES integer NOT NULL, HIGH real NOT NULL, LOW real NOT NULL, OPEN real NOT NULL, CLOSE real NOT NULL, CHANGE real NOT NULL)')

curr_time=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
y=0
execute = list()
execute.append(curr_time)
execute.append(curr_time)
execute.append(curr_time)
for x in behead(mse_equities).split("#"):
      if x != None:
           y+=1
           if (y == 9):
              execute.append(x.strip())
              dbdo.execute('INSERT INTO mse_trades (DATE, CREATED, MODIFIED, TICKER, VOLUME, VALUE, TRADES, HIGH, LOW, OPEN, CLOSE, CHANGE) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', execute)
              y=0
              del execute[:]
              execute.append(curr_time)
              execute.append(curr_time)
              execute.append(curr_time)

           else:
              execute.append(x.strip())
              
dbconnection.commit()
dbconnection.close() 

#print behead(mse_equities)

#print(mse_equities)
#print
#mse_mgs = formatTable(mse_mgs_table)
#print(mse_mgs)
#print
#mse_bonds = formatTable(mse_bonds_table)
#print(mse_bonds)
