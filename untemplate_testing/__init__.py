from lxml import etree as et


def same_doc(elt, text):
    """True if elt and text are the same xml document, False otherwise.

    ``elt`` should be an ``untemplate.Element``, and ``text`` should be a
    string.
    """
    elt_doc = et.XML(str(elt))
    elt_doc = et.tostring(elt_doc)
    text_doc = et.XML(text)
    text_doc = et.tostring(text_doc)
    return elt_doc == text_doc
