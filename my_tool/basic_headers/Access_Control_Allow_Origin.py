def access_control_allow_origin(header,i):
    value = header['access-control-allow-origin']
    if i in [0,1,2,4,5,6] :
        if value == '*':
            return [1,0,'Dont use star for CDN on public network']
        return [1,1,'No issues, header present']
    else:
        if value == '*':
            return [1,1,'Header value perfect for dynamic and utility sites but will recommend using trusted domains']
    
def no_access_control_allow_origin(header,i):
    text='Header not present and vulnerable if using APIs'
    if 'content-security-policy' in header and 'x-frame-options' in header:
        value1 = header['content-security-policy']
        value2 = header['x-frame-options']
        if 'SAMEORIGIN' in value2 and "frame-ancestors 'self'" in value1:
            text='Header not present but compensated by other headers x-frame-options and csp'
    if 'referrer-policy' in header:
        value=header['referrer-policy']
        if 'strict-origin' in value:
            text='Header not present but compensated by other header referrer-policy'
    if 'access-control-allow-methods' in header or 'access-control-allow-credentials' in header:
        text=text+'Header not present and should be included as access-control-allow-method and access-control-allow-credential rely on it'
    return [0,0,text]