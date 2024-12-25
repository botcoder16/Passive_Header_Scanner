def cache_control(headers):
    recommended_values = {"no-store", "max-age=0", "no-cache"}
    result = ""

    # Check for Cache-Control header
    current_policy = headers.get('cache-control', None)

    result += f"Cache-Control header found: {current_policy}\n"
    
    # Split existing values into a set
    current_values = set(map(str.strip, current_policy.split(',')))
    
    # Check if recommended values are included
    missing_values = recommended_values - current_values
    if not missing_values:
        result += f"✔ The recommended values ({', '.join(recommended_values)}) are already included.\n\n"
    else:
        result += f"⚠ The following recommended values are missing: {', '.join(missing_values)}\n"
        result += "Recommendation:\n"
        result += f"- Add the missing values ({', '.join(missing_values)}) to the Cache-Control header.\n\n"

    # Explanation of recommended values
    result += "Why 'no-store, max-age=0' is recommended:\n"
    result += "- `no-store`: Prevents browsers and intermediate caches from storing any version of the resource.\n"
    result += "- `max-age=0`: Ensures the resource is always revalidated before use, avoiding stale data.\n"
    result += "- These settings are critical for sensitive data like authentication responses or personal information.\n\n"

    return [1,result]

    
def no_cache_control(value):
    recommended_values = {"no-store", "max-age=0", "no-cache"}
    result = ''
    result += "⚠ Cache-Control header is missing.\n"
    result += "Recommendation:\n"
    result += f"- Add 'Cache-Control: {', '.join(recommended_values)}' along with any other necessary directives.\n\n"
    return [0, result]
