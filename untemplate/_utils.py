"""Various internal support routines."""
from StringIO import StringIO

_escape_blacklist = set('&<>\'"')

def _xml_escape_char(c):
    """Return an xml numeric escape code for the argument ``c``."""
    return '&#x%x;' % ord(c)


def _isprint(c):
    """Return True if c is an ascii printing char, False otherwise."""
    return c >= ' ' and c <= '~'


def xml_escape(s):
    """Escape the string ``s``, such that it may safely be used in xml."""
    buf = StringIO()
    for c in s:
        if not _isprint(c) or c in _escape_blacklist:
            c = _xml_escape_char(c)
        buf.write(c)
    return buf.getvalue()
