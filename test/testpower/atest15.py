#!user/bin/python
# encoding:utf-8
import re
import json
import HTMLParser

h
tml = """<p class="sceneheading" id="ljfe" data-input="12" data-id="1182">人物：包珺印（姜敏）托马斯、金刚、吴迪、飞行员甲乙、科考队员</p><p class="action"></p><p class="action">空中的<a id="effects-data-0-2708" data-id="2708" data-save="true" data-class="effects-cj" data-type="0" data-jd-id="0" data-other='{"txt":"浓云打在飞机","name":"场景","description":"","sceneDetails":"场景"}' data-old-class="effects-cj" data-old-type="0" class="effects-cj">浓云打在飞机</a>的前挡风玻璃上形成雨珠被雨刮器挂向一边，正副驾驶员紧张得驾驶着飞机，此时驾驶舱的门被打开。</p><p class="action">托马斯：还有多久才能到？病人快不行了。</p><p class="action">正驾驶：快了，再有十几分钟就能看见机场了。</p><p class="action">托马斯：我们需要帮手。</p><p class="action">正<a class="effects-js" data-class="effects-js" data-id="2722" data-jd-id="0" data-old-class="effects-js" data-old-type="1" data-other='{"qunzhong": "false", "name": "\u89d2\u82722", "yanyuan": "true", "teyue": "false", "txt": "\u9a7e\u9a76\u770b", "description": "\u63cf\u8ff0"}' data-save="true" data-type="1" id="effects-data-1-2722">驾驶看</a>驾驶看</a>向副驾驶，副驾驶旋即点了点头走向后舱。后舱是一群慌乱的人，只见人们分成两波分别压着狂躁的金刚和吴迪。忙乱的人中有的在试图给金刚打针，有的在向吴迪的嘴里灌着药水。机舱的尾部坐着面无表情的包珺印（姜敏），她看了看暴躁挣扎的金刚站起身向驾驶舱走去，在驾驶舱门口她拍了拍正在协助别人的托马斯，向他示意进入驾驶舱。托马斯跟着包珺印走进驾驶舱，在驾驶舱内包珺印反锁了舱门，托马斯不解的看着她，包珺印依旧面无表情，片刻后舱传来了凄厉的惨叫声和敲门声。</p><p class="action">驾驶员惊恐的回过头看着他两：出什么事了？</p><p class="action">包珺印：开好你的飞机！</p><p class="action">托马斯看着包珺印随即伸手去抓门把，却被包珺印按住了手。</p><p class="action"></p><p class="action"></p><p class="action"></p><p class="action">人物：包珺印（姜敏）托马斯、金刚、吴迪、飞行员甲乙、科考队员</p><p class="action"></p><p class="action">空中的浓云打在飞机的前挡风玻璃上形成雨珠被雨刮器挂向一边，正副驾驶员紧张得驾驶着飞机，此时驾驶舱的门被打开。</p><p class="action">托马斯：还有多久才能到？病人快不行了。</p><p class="action">正驾驶：快了，再有十几分钟就能看见机场了。</p><p class="action">托马斯：我们需要帮手。</p><p class="action">正驾驶看向副驾驶，副驾驶旋即点了点头走向后舱。后舱是一群慌乱的人，只见人们分成两波分别压着狂躁的金刚和吴迪。忙乱的人中有的在试图给金刚打针，有的在向吴迪的嘴里灌着药水。机舱的尾部坐着面无表情的包珺印（姜敏），她看了看暴躁挣扎的金刚站起身向驾驶舱走去，在驾驶舱门口她拍了拍正在协助别人的托马斯，向他示意进入驾驶舱。托马斯跟着包珺印走进驾驶舱，在驾驶舱内包珺印反锁了舱门，托马斯不解的看着她，包珺印依旧面无表情，片刻后舱传来了凄厉的惨叫声和敲门声。</p><p class="action">驾驶员惊恐的回过头看着他两：出什么事了？</p><p class="action">包珺印：开好你的飞机！</p><p class="action">托马斯看着包珺印随即伸手去抓门把，却被包珺印按住了手。</p><p class="action"></p><p class="action"></p><p class="action">人物：包珺印（姜敏）托马斯、金刚、吴迪、飞行员甲乙、科考队员</p><p class="action"></p><p class="action">空中的浓云打在飞机的前挡风玻璃上形成雨珠被雨刮器挂向一边，正副驾驶员紧张得驾驶着飞机，此时驾驶舱的门被打开。</p><p class="action">托马斯：还有多久才能到？病人快不行了。</p><p class="action">正驾驶：快了，再有十几分钟就能看见机场了。</p><p class="action">托马斯：我们需要帮手。</p><p class="action">正驾驶看向副驾驶，副驾驶旋即点了点头走向后舱。后舱是一群慌乱的人，只见人们分成两波分别压着狂躁的金刚和吴迪。忙乱的人中有的在试图给金刚打针，有的在向吴迪的嘴里灌着药水。机舱的尾部坐着面无表情的包珺印（姜敏），她看了看暴躁挣扎的金刚站起身向驾驶舱走去，在驾驶舱门口她拍了拍正在协助别人的托马斯，向他示意进入驾驶舱。托马斯跟着包珺印走进驾驶舱，在驾驶舱内包珺印反锁了舱门，托马斯不解的看着她，包珺印依旧面无表情，片刻后舱传来了凄厉的惨叫声和敲门声。</p><p class="action">驾驶员惊恐的回过头看着他两：出什么事了？</p><p class="action">包珺印：开好你的飞机！</p><p class="action">托马斯看着包珺印随即伸手去抓门把，却被包珺印按住了手。</p><p class="action"></p><p class="action"></p><p class="action">人物：包珺印（姜敏）托马斯、金刚、吴迪、飞行员甲乙、科考队员</p><p class="action"></p><i></i><span class="hh"></span><i></i><p class="action">空中的浓云打在飞机的前挡风玻璃上形成雨珠被雨刮器挂向一边，正副驾驶员紧张得驾驶着飞机，此时驾驶舱的门被打开。</p><p class="action">托马斯：还有多久才能到？病人快不行了。</p><p class="action">正驾驶：快了，再有十几分钟就能看见机场了。</p><p class="action">托马斯：我们需要帮手。</p><p class="action">正驾驶看向副驾驶，副驾驶旋即点了点头走向后舱。后舱是一群慌乱的人，只见人们分成两波分别压着狂躁的金刚和吴迪。忙乱的人中有的在试图给金刚打针，有的在向吴迪的嘴里灌着药水。机舱的尾部坐着面无表情的包珺印（姜敏），她看了看暴躁挣扎的金刚站起身向驾驶舱走去，在驾驶舱门口她拍了拍正在协助别人的托马斯，向他示意进入驾驶舱。托马斯跟着包珺印走进驾驶舱，在驾驶舱内包珺印反锁了舱门，托马斯不解的看着她，包珺印依旧面无表情，片刻后舱传来了凄厉的惨叫声和敲门声。</p><p class="action">驾驶员惊恐的回过头看着他两：出什么事了？</p><p class="action">包珺印：开好你的飞机！</p><p class="action">托马斯看着包珺印随即伸手去抓门把，却被包珺印按住了手。</p><p class="action"></p><p class="action"></p><p class="action">人物：包珺印（姜敏）托马斯、金刚、吴迪、飞行员甲乙、科考队员</p><p class="action"></p><p class="action">空中的浓云打在飞机的前挡风玻璃上形成雨珠被雨刮器挂向一边，正副驾驶员紧张得驾驶着飞机，此时驾驶舱的门被打开。</p><p class="action">托马斯：还有多久才能到？病人快不行了。</p><p class="action">正驾驶：快了，再有十几分钟就能看见机场了。</p><p class="action">托马斯：我们需要帮手。</p><p class="action">正驾驶看向副驾驶，副驾驶旋即点了点头走向后舱。后舱是一群慌乱的人，只见人们分成两波分别压着狂躁的金刚和吴迪。忙乱的人中有的在试图给金刚打针，有的在向吴迪的嘴里灌着药水。机舱的尾部坐着面无表情的包珺印（姜敏），她看了看暴躁挣扎的金刚站起身向驾驶舱走去，在驾驶舱门口她拍了拍正在协助别人的托马斯，向他示意进入驾驶舱。托马斯跟着包珺印走进驾驶舱，在驾驶舱内包珺印反锁了舱门，托马斯不解的看着她，包珺印依旧面无表情，片刻后舱传来了凄厉的惨叫声和敲门声。</p><p class="action">驾驶员惊恐的回过头看着他两：出什么事了？</p><p class="action">包珺印：开好你的飞机！</p><p class="action">托马斯看着包珺印随即伸手去抓门把，却被包珺印按住了手。</p><p class="action"></p><p class="action"></p><p class="action">Test</p><p class="action"></p><p class="action">Test</p><p class="action"></p><p class="action">Test</p><p class="action"></p><p class="action">Test</p><p class="action"></p>"""
recom = re.compile(r"<a(.*?)id=\"effects-data-1-%s\"(.*?)>" % "2722")
newhtml = recom.findall(html)
print newhtml