def convert(s):
    combo=zip(reversed(signs(s)), reversed(terms(s)) )
    return ''.join([''.join(_) for _ in combo])
def terms(poly: str):
    return poly.replace('+',' ').replace('-',' ').split()
