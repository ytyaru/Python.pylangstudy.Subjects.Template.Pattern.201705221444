#!python3
#encoding: utf-8
import urllib.parse
import htmlstr.HeaderNavi
import htmlstr.NextPrevNavi
import htmlstr.HtmlWrapper
import htmlstr.Code
class CodeCompare(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = htmlstr.HtmlWrapper.HtmlWrapper()
        self.__nav_head = htmlstr.HeaderNavi.HeaderNavi()
        self.__nav_next = htmlstr.NextPrevNavi.NextPrevNavi()
        self.__code = htmlstr.Code.Code()
    
    def CreateHtml(self, breadcrumbs_data, metanavi_data, nextprevnavi_data, code_data):
        nav_head_str = self.__nav_head.CreateHtml(breadcrumbs_data, metanavi_data)
        nav_next_str = self.__nav_next.CreateHtml(nextprevnavi_data['prev'], nextprevnavi_data['next'])
#        code_str = self.__code.CreateHtml(code_data['path'], code_data['lines'])
        return nav_head_str + '\n' + self.__CreateCodeTable(code_data) + '\n' + nav_next_str
    
    def __CreateCodeTable(self, code_data):
        table = self.__wrapper.CreateElement('table')
        tr1 = self.__wrapper.CreateElement('tr')
        thL = self.__wrapper.CreateElement('th', text_node_value=code_data['left']['title'])
        thR = self.__wrapper.CreateElement('th', text_node_value=code_data['right']['title'])
        tr2 = self.__wrapper.CreateElement('tr')
        tdL = self.__wrapper.CreateElement('td', text_node_value=self.__CreateCode(code_data['left']))
        tdR = self.__wrapper.CreateElement('td', text_node_value=self.__CreateCode(code_data['right']))
#        thL = self.__wrapper.CreateElement('th', self.__code.CreateHtml(code_data['left']['path'], code_data['left']['lines']))
#        thR = self.__wrapper.CreateElement('th', self.__code.CreateHtml(code_data['right']['path'], code_data['right']['lines']))
#        self.__wrapper.Wrap(tr1, thL + thR)
#        self.__wrapper.Wrap(tr2, tdL + tdR)
#        self.__wrapper.Wrap(table, tr1 + tr2)
#        code_str = self.__code.CreateHtml(code_data['path'], code_data['lines'])
        return self.__wrapper.Wrap(table, self.__wrapper.Wrap(tr1, thL + thR) + self.__wrapper.Wrap(tr2, tdL + tdR))
        
    def __CreateCode(self, data):
        if 'lines' in data:
            return self.__code.CreateHtml(data['path'], data['lines'])
        else:
            return self.__code.CreateHtml(data['path'])


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
    c = CodeCompare()
    html = c.CreateHtml(
        breadcrumbs_data, 
        metanavi_data,
        { 'directional_icon_type': 'FontAwesome',
          'prev': {'text': '前のページ', 'href': 'http://prev'},
          'next': {'text': '次のページ', 'href': 'http://next'} },
#        { 'path': '0.py', 'lines': [3, 7] })
        { 'left': { 'title': 'python2', 'path': 'left.py', 'lines': [3, 4] },
          'right': { 'title': 'python3', 'path': 'right.py', 'lines': [3, 4] }})
    print(html)
