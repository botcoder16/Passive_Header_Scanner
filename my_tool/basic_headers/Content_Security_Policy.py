import re
def content_security_policy(header):
    recommendations = {
        'default-src': "Notes:\n- Sets fallback for other directives.\n"
                       "- Affects scripts, stylesheets, images, etc.\n"
                       "- Recommended values: 'self', 'none', specific URLs.\n\n",

        'script-src': "Notes:\n- Controls executable script sources.\n"
                      "- Crucial for preventing XSS attacks.\n"
                      "- Recommended: 'self', specific trusted domains.\n\n",

        'style-src': "Notes:\n- Controls stylesheet sources.\n"
                     "- Avoid 'unsafe-inline' to prevent XSS vulnerabilities.\n"
                     "- Recommended: 'self', specific trusted domains.\n\n",

        'connect-src': "Notes:\n- Restricts origins for connections.\n"
                       "- Affects XMLHttpRequest, WebSocket, fetch(), etc.\n"
                       "- Ensure it covers necessary domains and protocols.\n\n",

        'object-src': "Notes:\n- Controls embedded objects (e.g., Flash).\n"
                      "- Recommended: Avoid unless necessary.\n\n",

        'media-src': "Notes:\n- Controls sources of audio and video.\n"
                     "- Recommended: Restrict to trusted sources.\n\n",

        'frame-src': "Notes:\n- Controls sources that can embed the page.\n"
                     "- Crucial for preventing clickjacking attacks.\n"
                     "- Recommended: Restrict to trusted sources.\n\n",

        'worker-src': "Notes:\n- Controls scripts used as workers.\n"
                      "- Affects Web Workers, SharedWorkers, ServiceWorkers.\n"
                      "- Recommended: 'self', specific trusted domains.\n\n",

        'font-src': "Notes:\n- Controls font sources.\n"
                    "- Recommended: Restrict to trusted sources to avoid exploits.\n\n",

        'img-src': "Notes:\n- Controls image sources.\n"
                   "- Important for preventing image-based XSS attacks.\n\n",

        'manifest-src': "Notes:\n- Controls application manifests.\n"
                        "- Important for offline functionality and PWAs.\n\n",

        'prefetch-src': "Notes:\n- Controls resources allowed to be prefetched.\n"
                        "- Affects performance optimization for preloading.\n\n",

        'child-src': "Notes:\n- Controls sources for iframe, embed, object, frameset.\n"
                     "- Important for preventing XSS in third-party iframes.\n\n",

        'form-action': "Notes:\n- Restricts URLs for form submissions.\n\n",

        'frame-ancestors': "Notes:\n- Specifies valid parents for embedding the page.\n\n",

        'base-uri': "Notes:\n- Restricts URLs in the document's <base> element.\n\n",

        'report-uri': "Notes:\n- Provides a URL for CSP violation reports.\n\n",

        'report-to': "Notes:\n- Specifies endpoint token for CSP violation reports.\n\n",

        'upgrade-insecure-requests': "Notes:\n- Instructs user agents to upgrade insecure HTTP URLs to HTTPS.\n\n",

        'block-all-mixed-content': "Notes:\n- Prevents loading mixed content (HTTP over HTTPS).\n\n",

        'sandbox': "Notes:\n- Enables a sandbox for the page.\n"
                   "- Restricts functionality like script execution.\n\n",
    }

    # Parse CSP directives
    directives = {}
    value = header.get('content-security-policy','')
    for directive in value.split(';'):
        directive = directive.strip()
        if directive:
            match = re.match(r'(\w+)\s*(.*)', directive)
            if match:
                name, value = match.group(1).strip(), match.group(2).strip()
                directives[name] = value

    # Start analyzing directives
    result = ""
    for name, value in directives.items():
        result += f"\nAnalyzing directive: {name}\nCurrent Value: {value or 'Not Set'}\n"
        result += recommendations.get(name, "Unknown directive. Review manually.\n")

    # Add missing OWASP recommended directives
    owasp_recommendations = {
        'default-src': "'self'",
        'form-action': "'self'",
        'object-src': "'none'",
        'frame-ancestors': "'none'",
        'upgrade-insecure-requests': "",
        'block-all-mixed-content': "",
    }
    for name, value in owasp_recommendations.items():
        if name not in directives:
            result += f"\nAnalyzing directive: {name}\nCurrent Value: Not Set\n"
            result += f"Recommendation: Set to {value or 'an appropriate value'}\n"
            result += recommendations.get(name, "")

    return [1,result]

def no_content_security_policy(value):
    return [0,'Content-security-policy header should be present']