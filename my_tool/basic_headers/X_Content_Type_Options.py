def x_content_type_options(header):
    value=header['x-content-type-options']
    if value.lower() == 'nosniff':
        return [1, 'Header configured properly with the "nosniff" value for optimal security.']
    else:
        return [1, f'Header present but value is "{value}". The value should strictly be "nosniff" for security.']

def no_x_content_type_options(value):
    return [0, 0, 'Header missing. Highly recommended to enable X-Content-Type-Options with value "nosniff", to enhance security and protect against MIME type sniffing vulnerabilities.']
