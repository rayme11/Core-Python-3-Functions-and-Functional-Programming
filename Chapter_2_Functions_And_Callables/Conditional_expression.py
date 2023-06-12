def sequence_class(immutable):
    return tuple if immutable else list


seq = sequence_class(immutable=False)

s = seq("Raymundo")
print(type(s))
