def cross_origin_opener_policy(header,i):
    value=header['cross-origin-opener-policy']
    if i in [1,2,3,4,6]:
        if value == 'same-origin':
            return [1,1,'Header configured properly']
        elif value == 'same-origin-allow-popups':
            return [1,0,'Header present but the security can be improved by using value same-origin only']
    if i ==5:
        if 'same-origin' in value or 'same-origin-allow-popups' in value:
            return [1,1,'Header configured properly']
    return [1,0,'Header present but value not set properly.']
def no_cross_origin_opener_policy(value,i):
    return [0,0,'Header missing and should be added to secure sensitive applications that open external links in new tabs or windows.']