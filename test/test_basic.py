from untemplate.html import *
from untemplate.node import Element, Markup
from untemplate.elements import ExampleElt
from untemplate_testing import same_doc
import pytest

# Let's not forget the trivial stuff; test Element.__repr__
assert repr(A(href="/")("Home")) == "<Element('a',{'href': '/'},('Home',))>"

# Checks for correct output

## Trivial case
assert same_doc(Element('p'), "<p/>")

## Check that text is escaped properly
assert same_doc(Element('p')("Hello, <world/>"),
                "<p>Hello, &lt;world/&gt;</p>")

## Make sure the element auto-import mechanism is working correctly.
assert same_doc(Element('exampleelt'), str(ExampleElt))


## Make sure `Markup` prevents
assert same_doc(P(Markup('<span>Hello</span>')),
                '<p><span>Hello</span></p>')

## Test something with attributes.
assert same_doc(A(href="/index.html")("Home"),
                '<a href="/index.html">Home</a>')

## This isn't something you'll see often because it looks awkward, but
## it should work: passing both contents and attributes in the same call.
assert same_doc(A("Home", href="/index.html"),
                '<a href="/index.html">Home</a>')


# Checks for invalid input from the user

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
