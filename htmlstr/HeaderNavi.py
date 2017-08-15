#!python3
#encoding: utf-8
import htmlstr.HtmlWrapper
import htmlstr.Breadcrumbs
import htmlstr.MetaNavi
#import htmlstr.NextPrevNavi
class HeaderNavi(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = htmlstr.HtmlWrapper.HtmlWrapper()
        
#    def CreateHtml(self, breadcrumbs_data, metanavi_data):
#        return self.__CreateHeaderNavi() + '\n\n' + self.__CreateNextPrevNavi()

    def CreateHtml(self, breadcrumbs_data, metanavi_data):
        b = self.__CreateBreadcrumbs(breadcrumbs_data)
        m = htmlstr.MetaNavi.MetaNavi()
        breadcrumbs = b.CreateHtml(breadcrumbs_data['datas'], breadcrumbs_data['is_child_first'])
        metaNavi = m.CreateHtml(metanavi_data['pydoc'], metanavi_data['env'], metanavi_data['github'])
        return self.__wrapper.Wrap(
            self.__wrapper.CreateElement('div', id_='HeaderNavi'),
            breadcrumbs + metaNavi)
    
    def __CreateBreadcrumbs(self, breadcrumbs_data):
        if 'directional_icon_type' in breadcrumbs_data:
            return htmlstr.Breadcrumbs.Breadcrumbs(breadcrumbs_data['directional_icon_type'])
        else:
            return htmlstr.Breadcrumbs.Breadcrumbs()
    
    """
    def __CreateHeaderNavi(self):
        b = Breadcrumbs.Breadcrumbs()
        m = MetaNavi.MetaNavi()
        
        breadcrumbs = b.CreateHtml([
            {'text': '孫', 'href': 'http://2'},
            {'text': '子', 'href': 'http://1'},
            {'text': '親', 'href': 'http://0'}], is_child_first=True)
        metaNavi = m.CreateHtml(
            {'text': 'Python文書の見出し', 'href': 'https://docs.python.jp/3/reference/introduction.html#alternate-implementations'},
            {'text': '学習環境', 'href': 'https://pylangstudy.github.io/'},
            {'text': 'GitHubリポジトリのタイトル名', 'href': 'http://github/repo'})
        headerNavi = self.__wrapper.Wrap(
            self.__wrapper.CreateElement('div', id_='HeaderNavi'),
            breadcrumbs + metaNavi)
#        headerNavi = self.__wrapper.Wrap(breadcrumbs + metaNavi, 'div', id_='HeaderNavi')
        return headerNavi
    """
    """        
    def __CreateNextPrevNavi(self):
        n = NextPrevNavi.NextPrevNavi()
        return n.CreateHtml(
            {'text': '前のページ', 'href': 'http://prev'},
            {'text': '次のページ', 'href': 'http://next'})
    """


if __name__ == '__main__':
    n = HeaderNavi()
    breadcrumbs_data = {
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
    html = n.CreateHtml(breadcrumbs_data, metanavi_data)
    print(html)

