def content_security_policy(header,i):
    value=header['content-security-policy']

    if i in [0,1,2,3,4,5,6]:
# Suggested CSP values by OWASP
        OWASP_CSP_VALUES = {
            "default-src": "'self'",
            "form-action": "'self'",
            "object-src": "'none'",
            "frame-ancestors": "'none'",
            "upgrade-insecure-requests": None,
            "block-all-mixed-content": None,
        }
        message=''
        # Check each CSP directive
        for directive, expected_value in OWASP_CSP_VALUES.items():
            if directive in value:
                if expected_value and f"{directive} {expected_value}" not in value:
                    text=(f"Directive '{directive}' is present but the value does not match: Expected '{expected_value}'.")
                else:
                    text=(f"Directive '{directive}' with the correct value is present.")
            else:
                text=(f"Directive '{directive}' is missing.")
            message=message+text
        return [1,0,message]
    
def no_content_security_policy(value,i):
    return [0,0,'Content-security-policy header should be present']