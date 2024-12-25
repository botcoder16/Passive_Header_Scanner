def cross_origin_resource_policy(headers):
    recommended_value = "same-origin"
    result = ""

    # Check for Cross-Origin-Resource-Policy header
    current_policy = headers.get('Cross-Origin-Resource-Policy', None)

    if current_policy:
        result += f"Cross-Origin-Resource-Policy header found: {current_policy}\n"
        
        # Compare current value with recommended one
        if current_policy == recommended_value:
            result += f"✔ Recommended value ('{recommended_value}') is correctly set.\n\n"
        else:
            result += f"⚠ Current value ('{current_policy}') differs from the recommended value ('{recommended_value}').\n"
            result += "Recommendation:\n- Update the header to use the recommended value: 'same-origin'.\n\n"
    else:
        result += "⚠ Cross-Origin-Resource-Policy header is missing.\n"
        result += "Recommendation:\n- Add 'Cross-Origin-Resource-Policy: same-origin' to secure your resources.\n\n"

    # Explanation of recommended value
    result += "Why 'same-origin' is recommended:\n"
    result += "- Ensures that resources can only be requested from the same origin.\n"
    result += "- Prevents unauthorized access to resources by cross-origin scripts or attackers.\n\n"

    return [1,result]
    
def no_cross_origin_resource_policy(value):
    return [0,'Header missing and should be added to ensure that certain files (e.g., images, scripts) are only usable within a controlled environment..']