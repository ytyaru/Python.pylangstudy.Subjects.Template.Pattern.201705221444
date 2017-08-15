#!python3
#encoding: utf-8
import htmlstr.HtmlWrapper
import htmlstr.Includer
import os.path
class Code(object):
    def __init__(self):
        self.__includer = htmlstr.Includer.Includer()
        self.__wrapper = htmlstr.HtmlWrapper.HtmlWrapper()

    def CreateHtml(self, path, lines=None):
        return '<pre class="highlightjs highlight"><code class="language-python" data-lang="python">{0}</code></pre>'.format(self.__includer.Include(path, lines=lines))


if __name__ == '__main__':
    c = Code()
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
    lines = [3, 6]
    print(c.CreateHtml(path, lines=lines))

