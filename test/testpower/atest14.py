#!user/bin/python
# encoding:utf-8
import re
import json
from bs4 import BeautifulSoup
import HTMLParser

html = """
<p class="sceneheading" id="tfkl" data-id="1322" data-input="1">1243标题</p><p class="character" id="s26k"><a id="effects-data-1-2723" data-id="2723" data-save="true" data-class="effects-js" data-type="1" data-jd-id="0" data-other="{&quot;txt&quot;:&quot;小林&quot;,&quot;name&quot;:&quot;角色名称&quot;,&quot;description&quot;:&quot;角色描述&quot;,&quot;teyue&quot;:false,&quot;qunzhong&quot;:false,&quot;yanyuan&quot;:true}" data-old-class="effects-js" data-old-type="1" class="effects-js">小林</a>1：人物</p><p class="dialog" id="z9vo" data-id="1330"><a id="effects-data-1-2725" data-id="2725" data-save="true" data-class="effects-js" data-type="1" data-jd-id="0" data-other="{&quot;txt&quot;:&quot;其他&quot;,&quot;name&quot;:&quot;角色名称&quot;,&quot;description&quot;:&quot;角色描述&quot;,&quot;teyue&quot;:true,&quot;qunzhong&quot;:false,&quot;yanyuan&quot;:false}" data-old-class="effects-js" data-old-type="1" class="effects-js">其他</a><br></p>
"""
soup = BeautifulSoup(html, 'lxml')
soup.prettify()  # 标准化

html_parser = HTMLParser.HTMLParser()
newhtml = str(html_parser.unescape(html))
print newhtml

idList = [2723, 2725]  # 特效
newMame = u"小易"
newEtype = "演员"

mappedDict = {"演员": "yanyuan", "特约": "teyue", "群众": "qunzhong"}

ETypeDict = {"teyue": "false", "qunzhong": "false", "yanyuan": "false"}
ETypeDict[mappedDict[newEtype]] = "true"
# print ETypeDict

mytype = "|".join("effects-data-1-" + str(ca) for ca in idList)
for ca in soup.find_all(name="a", attrs={"id": re.compile(mytype)}):
    dataOther = ca["data-other"]
    dataOtherJson = json.loads(dataOther)
    upDataOther = {"txt": str(dataOtherJson['txt']), "name": str(newMame), "description": str(dataOtherJson['description'])}
    upDataOther.update(ETypeDict)
    temple = str(ca).replace(str(dataOther), "%s")
    newtemple = temple % json.dumps(upDataOther)
    effectsId = ca['data-id']
    recom = re.compile("<a id=\"effects-data-1-%s\".*?data-other=\"(.*?)\".*?>" % effectsId)
    newhtml = recom.sub(newtemple, newhtml)
print newhtml
