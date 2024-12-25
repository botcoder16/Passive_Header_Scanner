def strict_transport_security(header):
    value = header.get('strict-transport-security', '')
    directives = value.split(';')

    # Initialize flags
    max_age_present = False
    include_subdomains_present = False
    preload_present = False

    # Single iteration to check all conditions
    for directive in directives:
        directive_lower = directive.strip().lower()
        if 'max-age' in directive_lower:
            max_age_present = True
            try:
                # Extract max-age value
                max_age_value = int(directive_lower.split('=')[1])
                if max_age_value <= 31536000:  # Check max-age validity
                    max_age_valid = True
            except (IndexError, ValueError):
                pass  # Handle cases where max-age is malformed
        if 'includesubdomains' in directive_lower:
            include_subdomains_present = True
        if 'preload' in directive_lower:
            preload_present = True

    max_age_result = (
    "Present and Value valid" if max_age_valid else
    "Present but Value invalid" if max_age_present else
    "Not Present"
    )
    result = (
        f"IncludeSubDomains: {'Present' if include_subdomains_present else 'Not Present'}, "
        f"Max-Age <= 31536000: {max_age_result}, "
        f"Preload: {'Present' if preload_present else 'Not Present'}"
    )
    return [1, result]

def no_strict_transport_security(value):
    return [0,f'Header missing']