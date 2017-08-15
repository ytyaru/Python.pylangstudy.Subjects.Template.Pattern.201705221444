#!python3
#encoding: utf-8
import urllib.parse
import htmlstr.HeaderNavi
import htmlstr.NextPrevNavi
import htmlstr.HtmlWrapper
import htmlstr.Code
class CodeList(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = htmlstr.HtmlWrapper.HtmlWrapper()
        self.__nav_head = htmlstr.HeaderNavi.HeaderNavi()
        self.__nav_next = htmlstr.NextPrevNavi.NextPrevNavi()
        self.__code = htmlstr.Code.Code()
    
    def CreateHtml(self, breadcrumbs_data, metanavi_data, nextprevnavi_data, code_data):
        nav_head_str = self.__nav_head.CreateHtml(breadcrumbs_data, metanavi_data)
        nav_next_str = self.__nav_next.CreateHtml(nextprevnavi_data['prev'], nextprevnavi_data['next'])
        return nav_head_str + '\n' + self.__CreateCodeStr(code_data) + '\n' + nav_next_str
    
    def __CreateCodeStr(self, code_data):
        code_str = ''
        for data in code_data:
            if 'lines' in data:
                code_str += self.__code.CreateHtml(data['path'], data['lines'])
            else:
                code_str += self.__code.CreateHtml(data['path'])
        return code_str


if __name__ == '__main__':
    breadcrumbs_data = {
        'directional_icon_type': 'FontAwesome',
        'datas': [
            {'text': '孫', 'href': 'http://2'},
            {'text': '子', 'href': 'http://1'},
            {'text': '親', 'href': 'http://0'}],
        'is_child_first': True
    }
    metanavi_data = {
        'pydoc': {'text': 'Python文書の見出し', 'href': 'https://docs.python.jp/3/reference/introduction.html#alternate-implementations'},
        'env': {'text': '学習環境', 'href': 'https://pylangstudy.github.io/'},
        'github': {'text': 'GitHubリポジトリのタイトル名', 'href': 'http://github/repo'}
    }
    c = CodeList()
    html = c.CreateHtml(
        breadcrumbs_data, 
        metanavi_data,
        { 'directional_icon_type': 'FontAwesome',
          'prev': {'text': '前のページ', 'href': 'http://prev'},
          'next': {'text': '次のページ', 'href': 'http://next'} },
        [
            { 'path': '0.py', 'lines': [3, 7] },
            { 'path': '1.py', 'lines': [3, 7] },
            { 'path': '1.py', 'lines': [3, 7] }
        ])
    print(html)
