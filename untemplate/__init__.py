_quote = repr


class Node(object):

    def __init__(self, name):
        self.tag = type(self).__name__.lower()
        self.attrs = {}
        self.contents = ()

    def __call__(self, *args, **attrs):
        if len(args) == 0:
            args = self.args
        if len(attrs) == 0:
            attrs = self.attrs

        ret = type(self)(self.tag)
        ret.contents = args
        ret.attrs = attrs
        return ret

    def write_to(self, fp):
        fp.write('<')
        fp.write(self.tag)
        for k, v in self.attrs.iteritems():
            fp.write(' ')
            fp.write(k),
            fp.write('=')
            fp.write(_quote(v))
        if len(self.contents) == 0:
            fp.write(' />')
        else:
            fp.write('>')
            for item in self.contents:
                if not hasattr(item, 'write_to'):
                    item = xml_escape(item)
                    fp.write(item)
                else:
                    item.write_to(fp)
            fp.write('</')
            fp.write(self.tag)
            fp.write('>')



class TextNode(object):

    def __init__(self, text):
        self.text = text

    def write_to(self, fp):
        fp.write(self.text)

class A(Tag): pass
class Body(Tag): pass
class Div(Tag): pass
class H1(Tag): pass
class Head(Tag): pass
class Html(Tag): pass
class P(Tag): pass
class Title(Tag): pass
