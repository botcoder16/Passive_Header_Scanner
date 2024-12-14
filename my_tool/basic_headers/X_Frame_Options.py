def x_frame_options(header, category):
    value = header.get('x-frame-options', '').upper()
    
    # Define recommendations for each category
    if category in [1, 3, 5, 6]:  # E-Commerce, Dynamic and Utility, Media, Technical
        recommended_value = "DENY"
        message = 'Recommended to use "DENY" for maximum protection against clickjacking.'
    elif category in [2, 4]:  # Static, Hybrid
        recommended_value = "SAMEORIGIN"
        message = 'Recommended to use "SAMEORIGIN" to allow framing within the same origin when necessary.'

    # Validate the header value against recommendations
    if value == recommended_value:
        return [1, 1, f'Header configured properly with "{value}" for category {category}. {message}']
    elif value == "DENY" and recommended_value != "DENY":
        return [1, 0, f'Header configured with "DENY". While secure, "{recommended_value}" is more suitable for category {category}.']
    elif value == "SAMEORIGIN" and recommended_value != "SAMEORIGIN":
        return [1, 0, f'Header configured with "SAMEORIGIN". Consider using "{recommended_value}" for better alignment with category {category}.']
    elif value == "ALLOW-FROM":
        return [1, 0, f'Header configured with "ALLOW-FROM", which is deprecated. Use "{recommended_value}" for category {category}.']
    elif value == "":
        return [0, 0, f'Header missing. {message}']
    else:
        return [1, 0, f'Header configured with unknown value "{value}". Recommended to use "{recommended_value}" for category {category}.']

def no_x_frame_options(value, category):
    if category in [1, 3, 5, 6]:  # E-Commerce, Dynamic and Utility, Media, Technical
        message = 'Recommended to set X-Frame-Options to "DENY" for security against clickjacking.'
    elif category in [2, 4]:  # Static, Hybrid
        message = 'Recommended to set X-Frame-Options to "SAMEORIGIN" for security against clickjacking.'
    
    return [0, 0, f'Header missing. {message}']
