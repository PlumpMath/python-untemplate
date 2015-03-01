import sys
from untemplate.node import Element


class elements(object):
    """This module allows the user to import arbitrary elements by tag name

    example:

        >>> from untemplate.elements import Html, Head, Body
        >>> print(Html)
        <html />
        >>> print(Html(Body))
        <html><body /></html>
    """
    def __init__(self, cls):
        self.cls = cls

    def __getattr__(self, tag):
        return self.cls(tag)


sys.modules[__name__] = elements(Element)
