def strict_transport_security(header, category):
    
    value = header.get('strict-transport-security', '')
    directives = value.split(';')
    max_age_present = any('max-age' in directive.lower() for directive in directives)
    include_subdomains_present = any('includeSubDomains' in directive for directive in directives)
    preload_present = any('preload' in directive for directive in directives)

    # Extract max-age value for validation
    max_age_value = None
    for directive in directives:
        if 'max-age' in directive.lower():
            try:
                max_age_value = int(directive.split('=')[1].strip())
            except (IndexError, ValueError):
                pass

    # Define requirements for each category
    if category == 1:  # E-Commerce and Transactions
        required_max_age = 31536000
        require_include_subdomains = True
        require_preload = True
    elif category == 2:  # Static and Moderated Content
        required_max_age = 15768000
        require_include_subdomains = False
        require_preload = False
    elif category == 3:  # Dynamic and Utility Sites
        required_max_age = 31536000
        require_include_subdomains = True
        require_preload = False
    elif category == 4:  # Hybrid or Mixed-Content Sites
        required_max_age = 15768000
        require_include_subdomains = True
        require_preload = False
    elif category == 5:  # Media and Entertainment
        required_max_age = 31536000
        require_include_subdomains = True
        require_preload = True
    elif category == 6:  # Technical or Specialized
        required_max_age = 31536000
        require_include_subdomains = True
        require_preload = True
    else:
        return [0, 0, f'Invalid category {category}.']

    # Evaluate the header based on the category requirements
    if max_age_present and max_age_value <= required_max_age and \
       (not require_include_subdomains or include_subdomains_present) and \
       (not require_preload or preload_present):
        return [1, 1, f'Header configured correctly for category {category} with max-age={max_age_value}, '
                      f'{"includeSubDomains" if include_subdomains_present else "no includeSubDomains"}, '
                      f'{"preload" if preload_present else "no preload"}.']
    elif max_age_present and max_age_value <= required_max_age:
        missing_directives = []
        if require_include_subdomains and not include_subdomains_present:
            missing_directives.append('includeSubDomains')
        if require_preload and not preload_present:
            missing_directives.append('preload')
        return [1, 0, f'Header partially configured for category {category}. Missing directives: {", ".join(missing_directives)}.']
    elif max_age_present and max_age_value > required_max_age:
        return [1, 0, f'Header present but max-age is {max_age_value}. Recommended to set max-age={required_max_age} for category {category}.']
    else:
        return [1, 0, f'Strict-Transport-Security header present but improperly configured for category {category}.']


def no_strict_transport_security(value,i):
    return [0,0,f'Strict-Transport-Security header is missing or improperly configured for category {i}.']