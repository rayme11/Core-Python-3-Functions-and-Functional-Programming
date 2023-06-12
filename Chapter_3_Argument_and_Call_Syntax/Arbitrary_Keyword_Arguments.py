def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

tag('img', src="Ray.jpg", alt="Ray Maldonado", border=1)

def tab_combined_positional_arguments(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result

tag(tab_combined_positional_arguments('img', src="Ray.jpg", alt="Ray Maldonado", border=1))
