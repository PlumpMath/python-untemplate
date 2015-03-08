from untemplate.html import *
from untemplate.node import Element, Markup
from untemplate_testing import same_doc
import pytest

assert repr(A(href="/")("Home")) == "<Element('a',{'href': '/'},('Home',))>"

assert same_doc(Element('p'), "<p/>")

assert same_doc(Element('p')("Hello, <world/>"),
                "<p>Hello, &lt;world/&gt;</p>")


assert same_doc(Element('p'), str(P))

assert same_doc(P(Markup('<span>Hello</span>')),
                '<p><span>Hello</span></p>')

assert same_doc(A(href="/index.html")("Home"),
                '<a href="/index.html">Home</a>')


class WriterToTestObj(object):
    """Utility class for exercising "type checking."

    The library is only supposed to accept objects which are instances
    of ``basestring``, ``Element``, or ``Markup``. The implementation
    just calls the ``write_to`` method on the latter, and I'll likely
    relax the type requirement in the future, but for now I'm enfocing
    this. This class is used for testing that.
    """
    def write_to(self, fp):
        fp.write('BROKEN')


with pytest.raises(TypeError):
    str(A(WriterToTestObj()))

with pytest.raises(TypeError):
    str(A(4))
