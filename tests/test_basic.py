import doctest

from untemplate.node import Element, Markup
from untemplate_testing import same_doc

assert same_doc(Element('p'), "<p/>")

assert same_doc(Element('p')("Hello, <world/>"),
                "<p>Hello, &lt;world/&gt;</p>")

from untemplate.elements import P

assert same_doc(Element('p'), str(P))

assert same_doc(P(Markup('<span>Hello</span>')),
                '<p><span>Hello</span></p>')
