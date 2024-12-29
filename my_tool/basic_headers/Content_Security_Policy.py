import requests
from urllib.parse import urlparse
from prettytable import PrettyTable

def categorize_csp(csp_header):
    """
    Categorize CSP header values into Safe and Unsafe based on the cheatsheet.
    """
    safe_values = {'self', 'none', 'strict-dynamic', 'https:'}
    unsafe_values = {'unsafe-inline', 'unsafe-eval', '*', 'data:'}

    categorized = []

    # Split CSP directives and process each
    directives = csp_header.split(';')
    for directive in directives:
        if not directive.strip():
            continue
        name, *sources = directive.strip().split()
        sources_set = set(sources)

        # Determine if the directive is safe or unsafe
        status = "Safe" if not sources_set & unsafe_values else "Unsafe"
        risks = []
        if "unsafe-inline" in sources_set:
            risks.append("Allows inline scripts/styles, prone to XSS attacks.")
        if "unsafe-eval" in sources_set:
            risks.append("Allows eval(), increasing XSS risks.")
        if "*" in sources_set:
            risks.append("Wildcard allows any origin, reducing security.")
        if "data:" in sources_set:
            risks.append("Data URIs can be exploited for malicious payloads.")

        categorized.append({
            "directive": name,
            "sources": ' '.join(sources),
            "status": status,
            "risks": ' | '.join(risks) if risks else "None"
        })

    return categorized

def content_security_policy(header):
    """
    Evaluate the CSP header of the given URL and categorize its directives.
    """
    try:
        csp_header = header.get('content-security-policy')

        if not csp_header:
            print("No CSP header found for the target URL.")
            return

        categorized = categorize_csp(csp_header)

        table = PrettyTable()
        table.field_names = ["Directive", "Sources", "Status", "Potential Risks"]

        for entry in categorized:
            table.add_row([entry['directive'], entry['sources'], entry['status'], entry['risks']])

        print("\n==== CSP Header Evaluation ====")
        print(table)

        return [1,'Present']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    


def no_content_security_policy(value):
    return [0,'Content-security-policy header should be present']