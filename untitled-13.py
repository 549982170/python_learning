<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">  
<html xmlns="http://www.w3.org/1999/xhtml">  
    <head>  
        <title>�ӿڲ���</title>  
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>  
        <style type="text/css">  
            body {font-size:12px; font-family:Tahoma;}  
            .tit0 {  
                    background-color: #DAEAF9;  
                    padding-left: 5px;  
                    font-size:15px;  
                 }  
            .tit1 {  
                    background-color: #FFF2AA;  
                    padding-left: 5px;  
                    font-size:15px;  
                 }  
            .tit2 {  
                    background-color: #DAEAF9;  
                    font-size:12px;  
                 }  
        </style>  
        <script type="text/javascript">  
            var $ = document.getElementById;  
            // ҳ���ʼ����ȡ���ļ�·������������Ҫ������޸�  
            var filePath = "E:\\�ӿڲ���\\������.xml";  
              
            function sendxml() {  
                var xmlhttp = new ActiveXObject("MICROSOFT.XMLHTTP");  
                xmlhttp.open("POST", $("servleturl").value, false);  
                xmlhttp.send($("RSXML").value);  
                $("RQXML").value = xmlhttp.responseText;  
                if ($("RQXML").value.indexOf("�ɹ�����") > 0) {  
                    alert("����ɹ���");  
                    // ��ָ�����ݸ��Ƶ����а��У���������Ҫ������޸�  
                    window.clipboardData.setData("text", "���Ƶ����а��е����ݡ�");   
                    $("resultword").style.display = "";  
                } else {  
                    alert("����ʧ�ܣ�");  
                }  
            }  
            function readFile(inFilePath) {  
                var fso = new ActiveXObject("Scripting.FileSystemObject");  
                var textFile = fso.GetFile(inFilePath);  
                var ts = fso.OpenTextFile(inFilePath, 1);   
                $("RSXML").value = ts.ReadAll();  
            }  
            function init() {  
                $('file1').value = filePath;  
                readFile(filePath);  
            }  
        </script>  
    </head>   
<body onload="init()">  
        <table width="100%" border="1" align="center" cellpadding="0" cellspacing="0" bordercolor="#CACA00" style="border-collapse: collapse;">  
            <caption align="center"> <font size="5px"><b>�ӿڲ��ԣ�HTTP + XML��</b></font><p/></caption>  
            <tr>  
                <td colspan=2>  
                    <div class="tit1">�����ַ��  
                        <select name="userid" id="servleturl" style="width:50%;" class="tit0" >  
                            <!-- ��Ҫ�޸Ľӿڵ�ַ -->  
                            <option value="http://ip:port/xx/AServlet" selected>1��1 A �ӿڣ�http://ip:port/xx/AServlet</option>  
                            <option value="http://ip:port/xx/BServlet" >1��2 B �ӿڣ�http://ip:port/xx/BServlet</option>  
                            <option value="http://ip:port/xx/CServlet" >1��3 C �ӿڣ�http://ip:port/xx/CServlet</option>  
                            <option value="http://ip:port/xx/DServlet" >1��4 D �ӿڣ�http://ip:port/xx/DServlet</option>  
                            <option value="http://ip:port/xx/EServlet" >1��5 E �ӿڣ�http://ip:port/xx/EServlet</option>  
                            <option value="http://ip:port/xx/FServlet" >2��1 F �ӿڣ�http://ip:port/xx/FServlet</option>  
                            <option value="http://ip:port/xx/GServlet" >2��2 G �ӿڣ�http://ip:port/xx/GServlet</option>  
                        </select>  
                        <input type="button" style="height:30px;"  id="send" value="    ��    ��    " onclick="sendxml()"/><p/>  
                    </div>  
                </td>  
            </tr>  
            <tr>  
                <td colspan=2>  
                    <div class="tit1">XML�ļ���  
                    <input type="text" id="file1" value="" style="width:50%;"  class="tit0" readonly>   
                    <input type="button" id="file2" style="height:30px;"   value="    �    ��    " onclick="file3.click();file1.value=file3.value;readFile(file1.value);">  
                    <input type="file" id="file3" style="display:none" style="width:50%;"  class="tit0">  
                    </div>  
                </td>  
            </tr>  
            <tr>  
                <td class="tit1"><b>���ͱ���</b>   
                    <input type="button" style="height:30px;"  value="�� ��" onclick="document.getElementById('RSXML').value='';">  
                    <input type="button" style="height:30px;"  value="�� ��" onclick="window.clipboardData.setData('text', document.getElementById('RSXML').value);">  
                </td>   
                <td class="tit1"><b>���ձ���</b>   
                    <input type="button" style="height:30px;"  value="�� ��" onclick="document.getElementById('RQXML').value='';">  
                    <input type="button" style="height:30px;"  value="�� ��" onclick="window.clipboardData.setData('text', document.getElementById('RQXML').value);">  
                </td>  
            </tr>   
            <tr>  
                <td><textarea id="RSXML" style="width:100%;height:400px;" class="tit2"></textarea></td>  
                <td><textarea id="RQXML" style="width:100%;height:400px;" class="tit2"></textarea></td>  
            </tr>  
        </table>  
        <div id="resultword"  align="center" style="display:none;color:red;font-size:25px;">  
            �ѽ��ı������Ƶ����а��е����ݡ������Ƶ����а壡��  
        </div>  
</body>   
</html>  