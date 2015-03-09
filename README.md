`python-untemplate` is an alternative to xml/html templating libraries.  
It provides facilities for quickly and easily constructing documents in 
python itself, unlocking access to the full power of the python 
programming language in your untemplates.

`python-untemplate` works, but is still very new, and probably has a few 
rough edges.

# Appetizer

Code:

```python

from untemplate.html import *

def base(title, *content):
    return Html(
        Head(
            Title(title),
        ),
        Body(
            H1(title),
            Div(id="content")(*content),
        ),
    )

github = "//github.com/zenhack/python-untemplate"
doc = base("Hello, Untemplate")(
    P(
        Code("python-untemplate"), ''' is an alternative to xml/html 
        templating libraries.  It provides facilities for quickly and
        easily constructing documents in python itself, unlocking access 
        to the full power of the python programming language in your
        untemplates.
        '''
    ),
    P(
        "Fork us on ", A(href=github)("Github"), "!",
    ),
)

print(doc)
     

```

Output:

```html
<html>
    <head>
        <title>Hello, Untemplate</title>
    </head>
    <body>
        <h1>Hello, Untemplate</h1>
        <p>
            <code>python-untemplate</code> is an alternative to xml/html 
            templating libraries.  It provides facilities for quickly and
            easily constructing documents in python itself, unlocking access 
            to the full power of the python programming language in your
            untemplates.
        </p>
        <p>
        Fork us on <a href="//github.com/zenhack/python-untemplate">Github</a>!
        </p>
    </body>
</html>
        
```
