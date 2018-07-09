#!/usr/bin/python
# coding: UTF-8
import re
from bs4 import BeautifulSoup

html_doc = """
<div class="bzh-main" id="bzh-container">
<pre id="bzh-main" class="bzh-tag" contenteditable="true">
<i class="split"></i><span id="split-cc-600" data-id="600" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="1"></span><span class="cc-content">剧本主要由台词和舞台指示组成</span></span>。对话、<i></i><span id="split-jt-344" data-id="344" class="jt"><b>◆</b>独白</span><i></i>、旁白都采用代言体，在戏曲、歌剧中则<i></i><span id="split-dh-396" data-id="396" class="dh"><span class="dh-head"></span><span class="dh-content">常用唱词来表现。</span></span><i></i><i></i><span id="split-jt-342" data-id="342" class="jt"><b>◆</b>剧本中的</span><i></i><i></i><span id="split-jt-343" data-id="343" class="jt"><b>◆</b>舞台</span><i></i><i class="split"></i><span id="split-cc-661" data-id="661" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="3"></span><span class="cc-content">指示</span></span><i></i><i></i><span id="split-db-398" data-id="398" class="db"><span class="db-head">独白</span><span class="db-content">是以剧作</span></span><i></i>者的口气<i></i><span id="split-dh-397" data-id="397" class="dh"><span class="dh-head"></span><i></i><i></i><span class="dh-content"><span style="font-family: STHeiti, &quot;Microsoft YaHei&quot;, 微软雅黑, SimSun, 宋体, arial;">来写的叙述性的文字说明</span>。包括对剧情发生的时间、地点的交代，对剧中人物的形象特征、形体动作及内心活动的描述,对场景、气氛的说明，</span></span><i></i>以及对布景、灯光、音响效果等方面的要求。
<i class="split"></i><span id="split-cc-605" data-id="605" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="9"></span><span class="cc-content">在戏剧发展史上</span></span>，<i></i><span id="split-jt-347" data-id="347" class="jt"><b>◆</b>剧本的出现</span><i></i>，<i></i><span id="split-jt-348" data-id="348" class="jt"><b>◆</b>大致在戏剧正式形成并成熟之际</span><i></i>。<i></i><span id="split-jt-353" data-id="353" class="jt"><b>◆</b>古希腊</span><i></i><i></i><span id="split-jt-355" data-id="355" class="jt"><b>◆</b>悲剧从原始</span><i></i><i></i><div id="split-dh-579" data-id="579" class="dh"><div class="dh-head"></div><div class="dh-content"><div class="tag">的酒神祭礼发展为</div></div></div><i></i><i></i><div id="split-dh-580" data-id="580" class="dh"><div class="dh-head"></div><div class="dh-content"><div class="tag">一种</div></div></div><i></i>完整的表演艺术，就是以一批悲剧剧本的出现为根本标志的；中国的宋元戏文和杂剧剧本，是中国戏剧成熟的最确实的证据；印度和日本古典戏剧的成熟，也是以一批传世的剧本来标明的。但是，<i class="split"></i><span id="split-cc-604" data-id="604" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="6"></span><span class="cc-content">也有一些</span></span>比较成熟的戏剧形态是没有剧本的，例如古代希腊、罗马的某些滑稽剧，意大利的初期即兴喜剧，日本歌舞伎中的一些口头剧目，中国唐代的歌舞小戏和滑稽短剧，以及现代的哑剧等等。
<i class="split"></i><span id="split-cc-601" data-id="601" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="2"></span><span class="cc-content">剧本的写作</span></span>，最重要的是能够被搬上舞台表演，戏剧文本不算是艺术的完成，只能说完成了一半，直到舞台演出之后（即“演出文本”）才<i></i><span id="split-db-417" data-id="417" class="db"><span class="db-head">独白</span><span class="db-content">是最终</span></span><i></i>艺术的呈现。历代文人中，也有<i></i><span id="split-db-399" data-id="399" class="db"><span class="db-head">独白</span><span class="db-content">人创作过不适合舞台演出，甚至根本</span></span><i></i>不能演出的剧本。这类的戏剧文本则称为案头戏（也叫书斋剧）。比较著名的如王尔德的《莎乐美》等。而好的剧本，能够具备适合阅读，也可能创造杰出舞台表演的双重价值。
<i class="split"></i><span id="split-cc-603" data-id="603" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="4"></span><span class="cc-content">一部可以在舞台</span></span>上搬演的剧本原著，还是需要在每一次不同舞台、不同表演者的需求下，做适度的修改，以符合实际的需要，因此，舞台工作者<i></i><span id="split-dh-416" data-id="416" class="dh"><span class="dh-head"></span><span class="dh-content">会修改</span></span><i></i>出一份不同于原著，有著详细注记<i></i><span id="split-db-400" data-id="400" class="db"><span class="db-head">独白</span><span class="db-content">、标出在剧本中某</span></span><i></i><i></i><span id="split-jt-346" data-id="346" class="jt"><b>◆</b>个段落应</span><i></i>该如何演出的工作用的剧本，这样的剧本叫做“提词簿”或“演出本”、“台本” 。此外，剧本是完整的演出脚本，有另外一种简单的舞台演出脚本只有简短的剧情大纲，实际的对白与演出，多靠演员在场上临场发挥，而这一种脚本则称为是“幕表”。
<i class="split"></i><span id="split-cc-602" data-id="602" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="3"></span><span class="cc-content">剧本主要由人物对话</span></span>（或唱词）和舞台提示组成。舞台提示一般指出人物说话的语气、说话时的动作，或人物上下场、指出场景或其它效果变换等。<i></i><span id="split-jt-345" data-id="345" class="jt"><b>◆</b>一个典型</span><i></i>的剧本例子如下：
<i class="split"></i><span id="split-cc-664" data-id="664" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="5"></span><span class="cc-content">第一场 日小姐房里 内</span></span><i></i>
<i class="split"></i><span id="split-cc-665" data-id="665" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="10"></span><span class="cc-content">王妈（小心翼翼地） </span></span><i></i>小姐，您还是得注意身子，就吃点东西吧。
<i class="split"></i><span id="split-cc-663" data-id="663" class="cc"><span class="cc-head"><b>场：</b><input type="text" class="form-control" value="4"></span><span class="cc-content">小姐（把碗砸在地上） 我不想吃</span></span><i></i>。</pre>
</div>
"""

soup = BeautifulSoup(html_doc, 'lxml')
for ca in soup.find_all(name="span", attrs={"id":re.compile(r"split-(\s\w+)?")}):  # 未标准化的内容没有标签无法筛选出来,条件需要修改
    if ca["class"][0] == u"cc":  # 场次
        ccdetail = ca.find_all('span')
        ccsign = str(ccdetail[0].b.string)  # 场（红色）
        ccnum = str(ccdetail[0].input['value'])   # 场次数
        ccconnet = str(ccdetail[1].string)   # 场次内容（标题）
        
    if ca["class"][0] == u"jt":  # 镜头
        jtsign = ca.span.b.string  # 镜头符号
        jtconnet = ca.span.string  # 镜头内容
        
    if ca["class"][0] == u"dh":  # 对话
        dhdetail = ca.find_all('span')
        dhsign = str(dhdetail[0].string)  # 对话符号（空）
        dhconnet = str(dhdetail[1].string)   # 场次内容
        
    if ca["class"][0] == u"dd":  # 独白
        dhdetail = ca.find_all('span')
        dhsign = str(dhdetail[0].string)  # 独白符号
        dhconnet = str(dhdetail[1].string)   # 独白内容
        


