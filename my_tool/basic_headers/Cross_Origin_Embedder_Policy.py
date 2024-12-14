def cross_origin_embedder_policy(header,i):
    value=header['cross-origin-embedder-policy']
    if i in [0,1,2,3,4,5,6]:
        if value == 'require-corp':
            return [1,1,'Header configured properly']
        return [1,0,'Header set but value not set properly']
    
def no_cross_origin_embedder_policy(value,i):
    if i in [3,5]:
        return [0,1,'Header not present but not very much required for this website.']
    return [0,0,'Should use this header to prevent untrusted resources from being loaded, especially if they might contain sensitive data.']