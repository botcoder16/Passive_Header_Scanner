def permissions_policy(header, i):
    # Define the expected values
    expected_values = {
        "accelerometer": "(none)",
        "autoplay": "(none)",
        "camera": "(none)",
        "cross-origin-isolated": "(none)",
        "display-capture": "(none)",
        "encrypted-media": "(none)",
        "fullscreen": "(self)",
        "geolocation": "(none)",
        "gyroscope": "(none)",
        "keyboard-map": "(none)",
        "magnetometer": "(none)",
        "microphone": "(none)",
        "midi": "(none)",
        "payment": "(none)",
        "picture-in-picture": "(none)",
        "publickey-credentials-get": "(self)",
        "screen-wake-lock": "(none)",
        "sync-xhr": "(self)",
        "usb": "(none)",
        "web-share": "(none)",
        "xr-spatial-tracking": "(none)",
        "clipboard-read": "(none)",
        "clipboard-write": "(none)",
        "gamepad": "(none)",
        "hid": "(none)",
        "idle-detection": "(none)",
        "interest-cohort": "(none)",
        "serial": "(none)",
        "unload": "(none)"
    }

    # Get the header value
    value = header.get("permissions-policy", "")

    # Parse the header value into directives
    directives = {}
    for item in value.split(", "):
        parts = item.split("=")
        if len(parts) == 2:  # Ensure valid key=value pairs
            k, v = parts
            directives[k.strip()] = v.strip()
        else:
            print(f"Invalid directive format: {item}")  # Log invalid directives

    # Initialize the result message
    message = ''
    
    # Check each directive
    for directive, expected in expected_values.items():
        if directive in directives:
            actual_value = directives[directive]
            if actual_value != expected:
                message += f"{directive} is not configured correctly. Expected: {expected}, Found: {actual_value}\n"
        else:
            message += f"{directive} is missing from Permissions-Policy header.\n"

    # If all checks pass
    if not message.strip():
        return [1, 1, "Permissions-Policy header is properly configured."]
    else:
        return [1, 0, message.strip()]


def no_permissions_policy(value,category):
    if category in [1, 3, 5, 6]:  # E-Commerce, Dynamic, Media, Technical
        message = (
            "Header not present. It is strongly recommended to add the Permissions-Policy header "
            "to restrict access to browser features like geolocation, camera, or microphone. "
            "This is especially important for sensitive or dynamic websites to prevent potential abuse."
        )
    elif category in [2, 4]:  # Static, Hybrid
        message = (
            "Header not present. The Permissions-Policy header should be added to control access to browser features. "
            "Even for static or hybrid content, restricting unnecessary permissions reduces potential attack vectors."
        )

    return [0, 0, message]
