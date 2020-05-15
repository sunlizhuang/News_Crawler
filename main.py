import sys
import os
import newspaper
import pymysql

db = pymysql.connect(host="localhost", user="root", password="sunlizhuang97", port=3306)
cursor = db.cursor()
sql = "SELECT DISTINCT C58,C35 from testDemo.`20200119.export` where C6='CHN' "
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

results = cursor.fetchall()


def text_save(content, filename, mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i]))
    file.close()

count=0
for index in range(len(results)):
    count=count+1
    article = newspaper.Article(results[index][0], language='en')
    article.download()
    article.parse()
    text_save(article.text,str(results[index][1])+"--"+str(count)+'.txt')
    print(results[index][0])
    print(results[index][1])
