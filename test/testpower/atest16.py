#encoding: utf-8
import re
import json
str = u'<p class="sceneheading" data-input="1243" id="7rji" data-id="1187">1243标题</p><p class="action"><a id="effects-data-1-2732" data-id="2732" data-save="true" data-class="effects-js" data-type="1" data-jd-id="0" data-other="{&quot;txt&quot;:&quot;小林&quot;,&quot;name&quot;:&quot;单价&quot;,&quot;description&quot;:&quot;&quot;,&quot;teyue&quot;:false,&quot;qunzhong&quot;:true,&quot;yanyuan&quot;:false}" data-old-class="effects-js" data-old-type="1" class="effects-js">小林</a>1：<a id="effects-data-1-2730" data-id="2730" data-save="true" data-class="effects-js" data-type="1" data-jd-id="0" data-other="{&quot;txt&quot;:&quot;人物&quot;,&quot;name&quot;:&quot;小林22&quot;,&quot;description&quot;:&quot;&quot;,&quot;teyue&quot;:true,&quot;qunzhong&quot;:false,&quot;yanyuan&quot;:false}" data-old-class="effects-js" data-old-type="1" class="effects-js">人物</a></p><p class="action">其他</p>'

ids=[2732,2730]
for k in ids:
    pattern = u"<a id=\"effects-data-1-%s\".*?data-other=\"(.*?)\".*?>" % k
    out = re.search(pattern, str)
    oldStr = out.group(1)
    m = json.loads(oldStr.replace("&quot;","\""))
    str = re.sub(u"<a id=\"effects-data-1-%s\".*?data-other=\"(.*?)\".*?>" % k, u'<a id="effects-data-1-%s" data-id="%s" data-save="true" data-class="effects-js" data-type="1" data-jd-id="0" data-other="{&quot;txt&quot;:&quot;%s&quot;,&quot;name&quot;:&quot;%s&quot;,&quot;description&quot;:&quot;%s&quot;,&quot;teyue&quot;:%s,&quot;qunzhong&quot;:%s,&quot;yanyuan&quot;:%s}" data-old-class="effects-js" data-old-type="1" class="effects-js">' % (k,k,m['txt'],u'被窝改了',m['description'],'true','false','false'), str)
print str
