def get_links (html):
    import re
    pattern = r'<a href=["\'\s]*(\\*/{0,1}[A-Za-z0-9\./]+)\"'
    links = re.findall(re.compile (pattern), html)
    return(links)