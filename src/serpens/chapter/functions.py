import html


def make_element(name, content, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = "".join(keyvals)
    element = "<{name}{attrs}>{content}</{name}>".format(
        name=name, attrs=attr_str, content=html.escape(content)
    )

    return element
