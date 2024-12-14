def x_permitted_cross_domain_policies(header, category):
    value = header.get('x-permitted-cross-domain-policies', '').lower()

    # Define category-specific recommendations
    if category in [1, 3, 5, 6]:  # E-Commerce, Dynamic, Media, Technical
        recommended_value = "none"
        message = 'Recommended to use "none" to prevent cross-domain data sharing for sensitive or dynamic content.'
    elif category in [2, 4]:  # Static, Hybrid
        recommended_value = "none"
        message = 'Recommended to use "none" to restrict cross-domain data sharing for static or hybrid sites.'

    # Validate the header value against recommendations
    if value == recommended_value:
        return [1, 1, f'Header configured properly with "{value}" for category {category}. {message}']
    elif value in ['master-only', 'all', 'by-content-type', 'by-ftp-filename']:
        return [1, 0, f'Header configured with "{value}", which is less secure. Use "{recommended_value}" for category {category}.']
    elif value == "":
        return [0, 0, f'Header missing. {message}']
    else:
        return [1, 0, f'Header configured with unknown value "{value}". Recommended to use "{recommended_value}" for category {category}.']

def no_x_permitted_cross_domain_policies(value, category):
    if category in [1, 3, 5, 6]:  # E-Commerce, Dynamic, Media, Technical
        message = 'Recommended to set X-Permitted-Cross-Domain-Policies to "none" to enhance security for sensitive or dynamic content.'
    elif category in [2, 4]:  # Static, Hybrid
        message = 'Recommended to set X-Permitted-Cross-Domain-Policies to "none" to enhance security for static or hybrid content.'

    return [0, 0, f'Header missing. {message}']
