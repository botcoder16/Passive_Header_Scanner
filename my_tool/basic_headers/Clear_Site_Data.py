def clear_site_data(header,i):
    value=header['clear-site-data']
    if i in [0,1,3]:
        required_values = {'cache', 'cookies', 'storage'}
        if required_values.issubset(value.split(',')):
            return [1,1,'Header set perfectly and secured']
        return [1,0,' Header value not set properly, should clear cookies, cache, storage all 3 for maximum security']
    elif i in [2,6]:
        required_values = {'cache', 'cookies'}
        if required_values.issubset(value.split(',')):
            return [1,1,'Header set perfectly and secured']
        return [1,0,' Header value not set properly, should clear cookies and cache for maximum security']
    elif i==4:
        required_values = {'cache', 'storage'}
        if required_values.issubset(value.split(',')):
            return [1,1,'Header set perfectly and secured']
        return [1,0,' Header value not set properly, should clear cache and storage for maximum security']
    elif i==5:
        required_values = {'cache', 'executionContexts'}
        if required_values.issubset(value.split(',')):
            return [1,1,'Header set perfectly and secured']
        return [1,0,' Header value not set properly, should clear cache and storage for maximum security']


def no_clear_site_data(value,i):
    return [0,0,'Header not used but should be used in scenarios like user sign outs to provide proper security']
