#coding:gbk
import os
def searchwb():
   
    path = "F:\\documents\\My Pictures\\weibo" # 地址根据需要修改（相对或绝对路径）
    sentence = raw_input("请输入查找的句子： ")
    while sentence == "":
        sentence = raw_input("\n请确认输入查找的句子： ")
    print
    n = len(sentence)

    allfile = os.walk(path)
    allcount = 0
    for root, dirs, files in allfile:
        for filename in files:
            singlefile = os.path.join(root, filename)
            if singlefile[-3:] == "txt":
                f = open(singlefile,"r")
                g = f.readlines()
                singlefilecount = 0
                for i in g:
                    if cmp(i[0:n], sentence) == 0:
                        print "file found in " + singlefile
                        print i
                        print
                        singlefilecount += 1
                        allcount += 1
                if singlefilecount > 0:
                    print "found %i times in this file." % singlefilecount
                    print
           
            
                f.close()
    if allcount == 0:
        print "not found.\n"
    else:
   
        print "found all %i matches, searching ended." % allcount
        print
   
 
while __name__=="__main__": # while True:
   
    searchwb()