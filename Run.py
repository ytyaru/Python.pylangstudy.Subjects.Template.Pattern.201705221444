#!python3
#encoding: utf-8
from subjects.CodeOnly import CodeOnly
from subjects.CodeCompare import CodeCompare
from subjects.CodeList import CodeList

class Run(object):
    def __init__(self):
        pass
        
    def CreateHtmlCodeList(self):
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
                { 'path': 'left.py', 'lines': [3, 7] },
                { 'path': 'right.py', 'lines': [3, 7] }
            ])
        print(html)
    def CreateHtmlCodeCompare(self):
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
            { 'left': { 'title': 'python2', 'path': 'left.py', 'lines': [3, 7] },
              'right': { 'title': 'python3', 'path': 'right.py', 'lines': [3, 7] }})
        print(html)
    def CreateHtmlCodeOnly(self):
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
        c = CodeOnly()
        html = c.CreateHtml(
            breadcrumbs_data, 
            metanavi_data,
            { 'directional_icon_type': 'FontAwesome',
              'prev': {'text': '前のページ', 'href': 'http://prev'},
              'next': {'text': '次のページ', 'href': 'http://next'} },
            { 'path': '0.py', 'lines': [3, 7] })
        print(html)


if __name__ == '__main__':
    r = Run()
    r.CreateHtmlCodeOnly()
    r.CreateHtmlCodeCompare()
    r.CreateHtmlCodeList()
