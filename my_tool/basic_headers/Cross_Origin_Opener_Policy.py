def cross_origin_opener_policy(headers):
    recommended_value = "same-origin"
    result = ""

    # Check for Cross-Origin-Opener-Policy header
    current_policy = headers.get('Cross-Origin-Opener-Policy', None)

    if current_policy:
        result += f"Cross-Origin-Opener-Policy header found: {current_policy}\n"
        
        # Compare current value with recommended one
        if current_policy == recommended_value:
            result += f"✔ Recommended value ('{recommended_value}') is correctly set.\n\n"
        else:
            result += f"⚠ Current value ('{current_policy}') differs from the recommended value ('{recommended_value}').\n"
            result += "Recommendation:\n- Update the header to use the recommended value: 'same-origin'.\n\n"
    else:
        result += "⚠ Cross-Origin-Opener-Policy header is missing.\n"
        result += "Recommendation:\n- Add 'Cross-Origin-Opener-Policy: same-origin' to prevent security issues.\n\n"

    # Explanation of recommended value
    result += "Why 'same-origin' is recommended:\n"
    result += "- Ensures that a top-level document can only interact with documents from the same origin.\n"
    result += "- Mitigates cross-origin attacks like Spectre and other shared memory attacks.\n\n"

    return result


def no_cross_origin_opener_policy(value):
    return [0, 'Header missing and should be added to secure sensitive applications that open external links in new tabs or windows.']