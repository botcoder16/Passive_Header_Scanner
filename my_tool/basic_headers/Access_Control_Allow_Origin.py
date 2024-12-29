# def access_control_allow_origin(header,i):
#     value = header.get('access-control-allow-origin', '').strip()
#     # Validate Access-Control-Allow-Origin values
#     if value == '*':
#         result= "Access-Control-Allow-Origin present: * (Not Recommended; Consider restricting origins to specific domains for better security)"
#     elif value == 'null':
#         result= "Access-Control-Allow-Origin present: NULL (Not Recommended; Avoid this value for security reasons)"
#     else:
#         result= f"Access-Control-Allow-Origin present: {value} (Valid; Ensure only trusted domains are listed)"
#     return [0, result]
    
from prettytable import PrettyTable

def access_control_allow_origin(header):
    """
    Print a table evaluating Access-Control-Allow-Origin headers.
    """
    def print_table(value, i):
        """
        Validate Access-Control-Allow-Origin header values.
        """
        # Validate Access-Control-Allow-Origin values
        if value == '*':
            result = "Not Recommended; Consider restricting origins to specific domains for better security"
            status = "Unsafe"
        elif value == 'null':
            result = "Not Recommended; Avoid this value for security reasons"
            status = "Unsafe"
        elif value:
            result = f"Valid; Ensure only trusted domains are listed"
            status = "Safe"
        else:
            result = "Access-Control-Allow-Origin header is missing (Potential Issue; Add this header for CORS protection)"
            status = "Missing"

        return [i, value if value else "None", status, result]

    value = header.get('access-control-allow-origin', '').strip()
    # Create a PrettyTable object
    table = PrettyTable()
    table.field_names = ["Index", "Header Value", "Status", "Evaluation"]

    # Process each header and add to the table
    for i, header in enumerate(value):
        result = print_table(value, i + 1)
        table.add_row(result)

    # Print the table
    print("\n==== Access-Control-Allow-Origin Header Evaluation ====\n")
    print(table)
    return[1,'present']

def no_access_control_allow_origin(header):
    text='Header not present and vulnerable if using APIs'
    if 'content-security-policy' in header and 'x-frame-options' in header:
        value1 = header['content-security-policy']
        value2 = header['x-frame-options']
        if 'SAMEORIGIN' in value2 and "frame-ancestors 'self'" in value1:
            text='Header not present but compensated by other headers x-frame-options and csp'
    if 'referrer-policy' in header:
        value=header['referrer-policy']
        if 'strict-origin' in value:
            text='Header not present but compensated by other header referrer-policy'
    if 'access-control-allow-methods' in header or 'access-control-allow-credentials' in header:
        text=text+'Header not present and should be included as access-control-allow-method and access-control-allow-credential rely on it'
    return [0, text]