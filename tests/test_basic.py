from untemplate.node import Element
from untemplate_testing import same_doc

assert same_doc(Element('p'), "<p/>")

assert same_doc(Element('p')("Hello, <world/>"),
                "<p>Hello, &lt;world/&gt;</p>")
