"""Classes for constructing nodes in the xml tree."""
from untemplate._utils import xml_escape
from StringIO import StringIO


class Element(object):
    """An element in the xml document."""

    def __init__(self, tag):
        """Create a new element

        The element will have the tag ``tag``, and no attributes or child
        nodes.
        """
        self.tag = tag.lower()
        self.attrs = {}
        self.contents = ()

    def __call__(self, *contents, **attrs):
        """Return a new element, with changed contents and/or attributes.

        If the list of positional arguments is non-empty, the new element
        will have contents equal to it. Otherwise, it will have contents
        equal to those of the original element.

        Each element of contents should be either a string, which will be
        treated as a text node and escaped, or an instance of ``Markup``.

        If the set of keyword arguments is non empty, the new element will
        have attributes equal to it, otherwise it will have the same attributes
        as the original.
        """
        if len(contents) == 0:
            contents = self.contents
        if len(attrs) == 0:
            attrs = self.attrs

        ret = type(self)(self.tag)
        ret.contents = contents
        ret.attrs = attrs
        return ret

    def write_to(self, fp):
        """Write the element to the file-like object fp."""
        fp.write('<')
        fp.write(self.tag)
        for k, v in self.attrs.iteritems():
            fp.write(' ')
            fp.write(k),
            fp.write('="')
            fp.write(xml_escape(v))
            fp.write('"')
        if len(self.contents) == 0:
            fp.write(' />')
        else:
            fp.write('>')
            for item in self.contents:
                if isinstance(item, basestring):
                    item = xml_escape(item)
                    fp.write(item)
                elif isinstance(item, Markup) or isinstance(item, Element):
                    item.write_to(fp)
                else:
                    raise TypeError('Item %r must be either a string, '
                                    '``Element``, or ``Markup``' % item)
            fp.write('</')
            fp.write(self.tag)
            fp.write('>')

    def __str__(self):
        """Return the element as a string, formated as an xml document"""
        buf = StringIO()
        self.write_to(buf)
        return buf.getvalue()

    def __repr__(self):
        return '<Element(%r,%r,%r)' % (self.tag, self.attrs, self.contents)


class Markup(object):
    """Markup in a text literal, which should not be escaped.

    By default, strings are escaped to make them html/xml-safe. If the user
    wishes to insert markup as raw text, they must wrap it in a markup object.
    """

    def __init__(self, text):
        """Create a ``Markup`` object with textual representation ``text``."""
        self.text = text

    def write_to(self, fp):
        """Write the element to the file-like object fp."""
        fp.write(text)
