import sys
from untemplate.node import Element


class _MakeElement(object):

    def __init__(self, cls):
        self.cls = cls

    def __getattr__(self, tag):
        return self.cls(tag)

sys.modules[__name__] = _MakeElement(Element)
