def cross_origin_embedder_policy(headers):
    recommended_value = "require-corp"
    result = ""

    # Check for Cross-Origin-Embedder-Policy header
    current_policy = headers.get('Cross-Origin-Embedder-Policy', None)

    if current_policy:
        result += f"Cross-Origin-Embedder-Policy header found: {current_policy}\n"
        
        # Compare current value with recommended one
        if current_policy == recommended_value:
            result += f"✔ Recommended value ('{recommended_value}') is correctly set.\n\n"
        else:
            result += f"⚠ Current value ('{current_policy}') differs from the recommended value ('{recommended_value}').\n"
            result += "Recommendation:\n- Update the header to use the recommended value: 'require-corp'.\n\n"
    else:
        result += "⚠ Cross-Origin-Embedder-Policy header is missing.\n"
        result += "Recommendation:\n- Add 'Cross-Origin-Embedder-Policy: require-corp' to enhance security.\n\n"

    # Explanation of recommended value
    result += "Why 'require-corp' is recommended:\n"
    result += "- Ensures that cross-origin resources can only be loaded if they explicitly allow it using CORS headers.\n"
    result += "- Protects against certain types of cross-origin attacks, including data leaks.\n\n"

    return [1,result]
    
def no_cross_origin_embedder_policy(value):
    return [0, 'Should use this header to prevent untrusted resources from being loaded, especially if they might contain sensitive data.']