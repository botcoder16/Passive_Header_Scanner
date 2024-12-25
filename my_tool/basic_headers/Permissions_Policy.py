def permissions_policy(headers):
    # Define recommended values for the Permission-Policy directives
    recommended_values = {
        'accelerometer': '()',
        'autoplay': '()',
        'camera': '()',
        'cross-origin-isolated': '()',
        'display-capture': '()',
        'encrypted-media': '()',
        'fullscreen': '()',
        'geolocation': '()',
        'gyroscope': '()',
        'keyboard-map': '()',
        'magnetometer': '()',
        'microphone': '()',
        'midi': '()',
        'payment': '()',
        'picture-in-picture': '()',
        'publickey-credentials-get': '()',
        'screen-wake-lock': '()',
        'sync-xhr': '(self)',
        'usb': '()',
        'web-share': '()',
        'xr-spatial-tracking': '()',
        'clipboard-read': '()',
        'clipboard-write': '()',
        'gamepad': '()',
        'hid': '()',
        'idle-detection': '()',
        'interest-cohort': '()',
        'serial': '()',
        'unload': '()'
    }

    result = ""

    # Check if the Permission-Policy header is present
    current_policy = headers.get('Permission-Policy', None)

    if current_policy:
        result += f"Permission-Policy header found: {current_policy}\n"
        
        # Split current policy into individual directives
        current_directives = dict(
            map(lambda x: tuple(x.strip().split('=')), current_policy.split(','))
        )

        # Check for missing or incorrect directives
        missing_directives = []
        incorrect_directives = []

        for directive, recommended_value in recommended_values.items():
            if directive not in current_directives:
                missing_directives.append(directive)
            elif current_directives[directive] != recommended_value:
                incorrect_directives.append(directive)
        
        # Handle missing directives
        if missing_directives:
            result += f"⚠ Missing directives: {', '.join(missing_directives)}\n"
            result += "Recommendation:\n"
            result += f"- Add the missing directives with recommended values: {', '.join(missing_directives)} = ()\n"

        # Handle incorrect directives
        if incorrect_directives:
            result += f"⚠ Incorrect directives or values found: {', '.join(incorrect_directives)}\n"
            result += "Recommendation:\n"
            result += f"- Update the incorrect directives to use recommended values: {', '.join(incorrect_directives)} = ()\n"

    else:
        result += "⚠ Permission-Policy header is missing.\n"
        result += "Recommendation:\n"
        result += f"- Add 'Permission-Policy' header with recommended directives and values: {', '.join(recommended_values.keys())} = ()\n"

    # Explanation of recommended values
    result += "\nExplanation of recommended values:\n"
    result += "- The 'Permission-Policy' header controls which features and APIs can be accessed by the page.\n"
    result += "- The recommended values help restrict access to sensitive resources for privacy and security reasons.\n"
    result += "- Using `()` means no origin is allowed access to the feature, and using `(self)` means only the same origin can access it.\n"
    result += "- It's important to restrict permissions to only what is necessary for functionality.\n"

    return [1,result]

def no_permissions_policy(value):
    message = (
        "Header not present. It is strongly recommended to add the Permissions-Policy header "
        "to restrict access to browser features like geolocation, camera, or microphone. ")
    return [0, message]
