def access_control_allow_origin(header,i):
    value = header.get('access-control-allow-origin', '').strip()
    # Validate Access-Control-Allow-Origin values
    if value == '*':
        result= "Access-Control-Allow-Origin present: * (Not Recommended; Consider restricting origins to specific domains for better security)"
    elif value == 'null':
        result= "Access-Control-Allow-Origin present: NULL (Not Recommended; Avoid this value for security reasons)"
    else:
        result= f"Access-Control-Allow-Origin present: {value} (Valid; Ensure only trusted domains are listed)"
    return [0, result]
    
def no_access_control_allow_origin(header):
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
    return [0, text]