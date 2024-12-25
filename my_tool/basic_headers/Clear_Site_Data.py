def clear_site_data(headers):
    # Recommended values for the Clear-Site-Data header
    recommended_values = {"cache", "cookies", "storage"}
    result = ""

    # Check if the Clear-Site-Data header is present
    current_header = headers.get('Clear-Site-Data', None)

    if current_header:
        result += f"Clear-Site-Data header found: {current_header}\n"
        
        # Parse the current values into a set for comparison
        current_values = set(value.strip('"').strip() for value in current_header.split(','))

        # Compare current values with recommended values
        missing_values = recommended_values - current_values
        unexpected_values = current_values - recommended_values

        if not missing_values and not unexpected_values:
            result += "✔ Recommended values ('cache', 'cookies', 'storage') are correctly set.\n\n"
        else:
            if missing_values:
                result += f"⚠ Missing recommended values: {', '.join(missing_values)}.\n"
            if unexpected_values:
                result += f"⚠ Unexpected values detected: {', '.join(unexpected_values)}.\n"
            
            result += "Recommendation:\n"
            result += "- Update the header to include all recommended values: 'cache', 'cookies', 'storage'.\n"
            result += "- Avoid including unnecessary or incorrect values to ensure optimal behavior.\n\n"
    else:
        result += "⚠ Clear-Site-Data header is missing.\n"
        result += "Recommendation:\n"
        result += "- Add 'Clear-Site-Data: \"cache\", \"cookies\", \"storage\"' to enhance security and privacy.\n\n"

    # Explanation of recommended values
    result += "Why these values are recommended:\n"
    result += "- `cache`: Ensures cached resources (e.g., CSS, JS, images) are cleared, preventing outdated or malicious content.\n"
    result += "- `cookies`: Deletes cookies, reducing tracking risks and ensuring session invalidation.\n"
    result += "- `storage`: Clears client-side storage (e.g., localStorage, sessionStorage), protecting sensitive data.\n\n"

    return result

def no_clear_site_data(value):
    return [0, 'Header not used but should be used in scenarios like user sign outs to provide proper security']
