def x_permitted_cross_domain_policies(header):
    value = header.get('x-permitted-cross-domain-policies', '').strip().lower()
    
    # Determine the result based on the value
    if value == 'none':
        result= "NONE (Recommended for better security)"
    elif value == 'master-only':
        result= "MASTER-ONLY (Consider using NONE for stricter security)"
    elif value == 'by-content-type':
        result= "BY-CONTENT-TYPE (Consider using NONE for stricter security)"
    elif value == 'all':
        result= "ALL (Not Recommended; Use NONE for better security)"
    elif value == 'by-ftp-filename':
        result= "BY-FTP-FILENAME (Not Recommended; Use NONE for better security)"
    else:
        result= "Not Present or Invalid (Add header with value NONE for stricter security)"        
    return[1,result]

def no_x_permitted_cross_domain_policies(header):
    if 'access-control-allow-origin' in header:
        value = header.get('access-control-allow-origin', '').strip()
        # Validate Access-Control-Allow-Origin values
        if value == '*':
            result= "Access-Control-Allow-Origin present: * (Not Recommended; Consider restricting origins to specific domains for better security)"
        elif value == 'null':
            result= "Access-Control-Allow-Origin present: NULL (Not Recommended; Avoid this value for security reasons)"
        else:
            result= f"Access-Control-Allow-Origin present: {value} (Valid; Ensure only trusted domains are listed)"
    else:
        result= "Access-Control-Allow-Origin: Missing (Add any of these header if CORS support is required)"
    return [0, 'Header not present, '+result]
