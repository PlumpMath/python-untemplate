"""Convienence module for quick-access to html elements.

The point of this module is to help you avoid having to do::

    from untemplate.elements import Html, Head, Body, ... <*everything else*>

Instead, you can do::

    from html import *

Which will make almost all of the html5 conformant elements available by
their names, with the first letter of the word capitalized. Ommited elements
fall into the following categories:

    * Things which introduce whole new xml namespaces (e.g. math, svg).
    * Things which are technically conforming, but which should probably
      be avoided: <b> & <i> are the main ones.
    * Things which are only there to be abused: <embed>, <object>
    * The <base> tag, because it's name is nightnmare-enducingly generic,
      and I can't condone an unqualified import of it.

It is *strongly* recommended that this is the *first* import statement in
your module; many html elements have collision-prone names (e.g. <output>),
and it would be easy to have one shadow another binding that you meant to use.
Care has been taken to ensure that none of these conflict with the standard
python namespace, but there will be conflicts with other libraries.
"""


from untemplate.elements import (
    # From http://www.w3.org/community/webed/wiki/HTML/Elements,
    # With some exclusions whose reasonings are detailed inline.
    Html,

    Head,
    Title,
    # Base, # Likely to cause trouble given how generic a name it is, and the
    #       # fact that it's marginally obscure.
    # Isindex,  # Obsolete, see [1].
    Link,
    Meta,
    Style,

    Script,
    Noscript,

    Body,
    Section,
    Nav,
    Article,
    Aside,
    H1, H2, H3, H4, H5, H6,
    Hgroup,
    Header,
    Footer,
    Address,

    P,
    Hr,
    Pre,
    Blockquote,
    Ol,
    Ul,
    Li,
    Dl,
    Dt,
    Dd,
    Figure,
    Figcaption,
    Div,
    Center,

    A,
    Abbr,
    # Acryonm,  # Non-conforming
    # B,        # HTML5 technically gives this new semantics, but it really
                # shouldn't exist, and it's taking up prime one-letter-name
                # realestate.
    # Basefont, # Non-conforming
    Bdo,
    # Big,      # Non-conforming
    # Blink,    # Oh dear god. Also, non-conforming.
    Br,
    Cite,
    Code,
    Dfn,
    Em,
    # Font,     # Non-conforming.
    # I,        # See the comments for B.
    Kbd,
    # Listing,  # Non-conforming.
    Mark,
    # Marquee,  # Oh dear god. Also, non-conforming.
    # Nextid,   # Non-conforming.
    # Nobr,     # Non-conforming.
    Q,
    Rp,
    Rt,
    Ruby,
    S,
    Samp,
    Small,      # Amusingly enough, small is semantically meaningful,
                # though big is not.
    # Spacer,   # Non-conforming.
    Span,
    # Strike,   # Non-conforming.
    Strong,
    Sub, Sup,
    Time,
    # Tt,       # Non-conforming.
    # U,        # Non-conforming.
    Var,
    Wbr,
    # Xmp,      # Non-conforming. I don't even know what this one was.

    Ins,
    Del,

    Img,
    Iframe,
    # Embed,    # If you want to use this, fine, but I refuse to make it easier
                # for you; import it yourself.
    # Object,   # See Embed.
    # Param,    # Only for use with Object.
    Video,
    Audio,
    Source,
    Track,
    Canvas,
    Map,
    Area,
    # Math,     # This represents an entire namespace of xml elements, and I'm
                # not putting them all in this module. In the future, a module
                # "untemplate.mathml" would not be unreasonable.
    # Svg,      # See Math.
    # Applet,   # See Embed, Object. Just let it die.
    # Frame,    # Non-conforming.
    # Frameset, # Non-conforming.
    # Noframes, # Non-conforming.
    # Bgsound,  # Non-conforming.
    # Noembed,  # Non-conforming.
    # Plaintext,# Non-conforming.

    Table,
    Caption,
    Colgroup,
    Col,
    Tbody,
    Thead,
    Tfoot,
    Tr,
    Td,
    Th,

    Form,
    Fieldset,
    Legend,
    Label,
    Input,
    Button,
    Select,
    Datalist,
    Optgroup,
    Option,
    Textarea,
    Keygen,
    Output,
    Progress,
    Meter,

    Details,
    Summary,
    Menu
)

# [1]: http://www.w3.org/TR/html5/obsolete.html#obsolete,
