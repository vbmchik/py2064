def get_formatted_name(first, last):
    f = ''.join([ x for x in first if x.isalpha() ])
    l = ''.join([ x for x in last if x.isalpha() ])
    return f"{f} {l}".title()
