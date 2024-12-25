def x_frame_options(header):
    value = header.get('x-frame-options', '').strip().lower()
    
    # Determine the result based on the value
    if value == 'deny':
        result = "Value: DENY (Recommended)"
    elif value == 'sameorigin':
        result = "Value: SAMEORIGIN (Consider using DENY for stricter security)"
    elif value.startswith('allow-from'):
        result = f"Value: {value.upper()} (Not Recommended; Consider using DENY)"
    else:
        result = "Value: Not Present or Invalid (DENY is Recommended)"
    
    return [1, result]

def no_x_frame_options(headers):
    if 'content-security-policy' in headers:
        csp_value = headers.get('content-security-policy', '')
        csp_directives = csp_value.split(';')
        for directive in csp_directives:
            directive = directive.strip().lower()
            if directive.startswith('frame-ancestors'):
                result= f"Content-Security-Policy: {directive} (Can replace X-Frame-Options)"
        result= "Content-Security-Policy: Present but no frame-ancestors directive found (Add frame-ancestors for framing protection)"
    else:
        result= "X-Frame-Options: Missing and no Content-Security-Policy with frame-ancestors found (Add X-Frame-Options: DENY or equivalent CSP directive)"
    
    return [0, result]
