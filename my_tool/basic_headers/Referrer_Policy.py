def referrer_policy(headers):
    # Referrer-Policy header analysis
    recommended_policy = 'no-referrer'
    result = ""

    # Check for the existence of the Referrer-Policy header
    current_policy = headers.get('Referrer-Policy', None)

    if current_policy:
        result += f"Referrer-Policy found: {current_policy}\n"

        # Compare current policy with the recommended one
        if current_policy == recommended_policy:
            result += f"✔ Recommended policy ('{recommended_policy}') is correctly set.\n\n"
        else:
            result += f"⚠ Current policy ('{current_policy}') does not match the recommended policy ('{recommended_policy}').\n"
            result += "Recommendation:\n- Update to 'no-referrer' for maximum privacy and security.\n"
    else:
        result += "⚠ Referrer-Policy header is missing.\n"
        result += f"Recommendation:\n- Add 'Referrer-Policy: {recommended_policy}' to ensure privacy protection.\n\n"

    # Explanation of 'no-referrer'
    result += "Why 'no-referrer' is recommended:\n"
    result += "- Prevents sending the `Referer` header, avoiding leaks of sensitive information.\n"
    result += "- Ensures user privacy when navigating between pages or domains.\n"
    result += "- Reduces risk in scenarios involving confidential data or restricted resources.\n\n"

    return [1,result]
    
def no_referrer_policy(value):
    message = (
        "Header not present. The Referrer-Policy header is critical for protecting sensitive data in referrer URLs. "
        "Set this header to 'no-referrer' or 'strict-origin-when-cross-origin' to prevent leaking user data or transaction information to third-party sites."
    )

    return [0, 0, message]