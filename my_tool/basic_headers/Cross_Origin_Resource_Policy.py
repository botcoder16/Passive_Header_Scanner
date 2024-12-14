def cross_origin_resource_policy(header,i):
    value=header['cross-origin-opener-policy']
    if i in [0,1,3,4,6]:
        if value == 'same-origin':
            return [1,1,'Header configured properly']
        elif value == 'same-site':
            return [1,0,'Header present but the security can be improved by using value same-origin only']
    elif i in [2,5]:
        if value == 'same-origin' or value == 'same-site':
            return [1,1,'Header configured properly'] 
    return [1,0,'Header set but value not set properly']
    
def no_cross_origin_resource_policy(value,i):
    return [0,0,'Header missing and should be added to ensure that certain files (e.g., images, scripts) are only usable within a controlled environment..']