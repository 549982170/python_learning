#coding:utf-8
import sys
import json
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
a='[{"id":"243","value":"1","cc":"<span id=\"data-comm-cc-243\" class=\"cc\"><b data-id=\"243\">场次：</b><input type=\"text\" value=\"1\" class=\"form-control ccinput\">场次1</span><span id=\"data-comm-jt-117\" class=\"jt\"><b data-id=\"117\">镜头</b>镜头1</span><span id=\"data-comm-dh-131\" class=\"dh\"><b data-id=\"131\">对话</b>对话1</span><span id=\"data-comm-db-132\" class=\"db\"><b data-id=\"132\">独白</b>独白1</span>","jt":[{"id":117,"content":"<span id=\"data-comm-jt-117\" class=\"jt\"><b data-id=\"117\">镜头</b>镜头1</span>"}],"dh":[{"id":131,"content":"<span id=\"data-comm-dh-131\" class=\"dh\"><b data-id=\"131\">对话</b>对话1</span>"}],"db":[{"id":132,"content":"<span id=\"data-comm-db-132\" class=\"db\"><b data-id=\"132\">独白</b>独白1</span>"}]},{"id":"244","value":"undefined","cc":"<span id=\"data-comm-cc-244\" class=\"cc\"><b data-id=\"244\">场次：</b><input type=\"text\" value=\"1\" class=\"form-control ccinput\">场次2</span><span id=\"data-comm-jt-118\" class=\"jt\"><b data-id=\"118\">镜头</b>镜头2</span><span id=\"data-comm-dh-133\" class=\"dh\"><b data-id=\"133\">对话</b>对话2</span><span id=\"data-comm-db-134\" class=\"db\"><b data-id=\"134\">独白</b>独白2 </span>","jt":[{"id":118,"content":"<span id=\"data-comm-jt-118\" class=\"jt\"><b data-id=\"118\">镜头</b>镜头2</span>"}],"dh":[{"id":133,"content":"<span id=\"data-comm-dh-133\" class=\"dh\"><b data-id=\"133\">对话</b>对话2</span>"}],"db":[{"id":134,"content":"<span id=\"data-comm-db-134\" class=\"db\"><b data-id=\"134\">独白</b>独白2 </span>"}]}]'

a = str(a)


print a