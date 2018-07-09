# -*- encoding: utf8 -*-
import os

def readDocx(docName, separated_rows=0, addStr=''):
    """获取docx的文档中的所有文字,不管格式,暂不支持doc格式每line行
    @param separated_rows: int 相隔行数
    @param addStr: str 追加的字符
    """
    TotalPage = 1  # 页数
    extension = os.path.splitext(docName)[1]  # 文件后缀名
    separated_rows = int(separated_rows)  # 需要隔separated_rows行追加字符
    if extension == ".txt":
        with open(docName) as f:
            if separated_rows != 0:  # 需要隔行追加字符
                docText = '<br>'.join(paragraph + addStr if index % separated_rows == 0 else paragraph for index, paragraph in enumerate(f))
                docText = docText.replace(addStr, "", 1)  # 第一行不需要分页符
                TotalPage = docText.count(addStr) + 1  # 页数统计
            else:
                docText = '<br>'.join(paragraph for paragraph in f)  # 生成迭代器,然后加入回车换行,比起生成列表需要更少内存,此情况迭代器的括号可省略
    return docText, TotalPage

docText, TotalPage = readDocx("test.txt")
print docText
