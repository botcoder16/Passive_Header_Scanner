def referrer_policy(header,i):
    value=header['referrer-policy']
    if value == 'no-referrer':
        return [1, 1, 'Header configured properly with the highest security.']
    elif value == 'strict-origin-when-cross-origin':
        return [1, 1, 'Header configured securely for general use.']
    elif value == 'same-origin':
        return [1, 0, 'Header configured securely for restricting referrer data to same-origin requests only.']
    elif value == 'strict-origin':
        return [1, 1, 'Header set securely, prevents referrer leakage to HTTP origins.']
    elif value == 'origin':
        return [1, 0, 'Header present, but less secure. Reveals the origin cross-origin.']
    elif value == 'origin-when-cross-origin':
        return [1, 0, 'Header present, but could be stricter. Sends full referrer for same-origin, origin only cross-origin.']
    elif value == 'no-referrer-when-downgrade':
        return [1, 0, 'Header present, but this is the default behavior and could be improved with stricter values.']
    elif value == 'unsafe-url':
        return [1, 0, 'Header present, but least secure. Full referrer including path and query is sent.']
    elif value == '':
        return [0, 0, 'Header error. Highly recommended to configure Referrer-Policy.']
    
def no_referrer_policy(value,category):
    if category in [1, 3, 5]:  # E-Commerce, Dynamic, Media
        message = (
            "Header not present. The Referrer-Policy header is critical for protecting sensitive data in referrer URLs. "
            "Set this header to 'no-referrer' or 'strict-origin-when-cross-origin' to prevent leaking user data or transaction information to third-party sites."
        )
    elif category in [2, 4, 6]:  # Static, Hybrid, Technical
        message = (
            "Header not present. Adding the Referrer-Policy header is recommended to improve privacy. "
            "Use 'no-referrer' or 'strict-origin' to minimize data exposure when users navigate away from your site."
        )
    else:
        message = (
            "Header not set. The Referrer-Policy header should be configured to ensure referrer data is shared only as needed, "
            "based on your site's privacy and security requirements."
        )

    return [0, 0, message]