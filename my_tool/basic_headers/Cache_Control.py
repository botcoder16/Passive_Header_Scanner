def cache_control(header,i):
    value=header['cache-control']
    
    if i == 1:
        elements=['no-store','no-cache','maz-age=0','must-revalidate']
        if all(element in value for element in elements):
            return [1,1,'All required header values present']
        else:
            return [1,0,'All values no-store,no-cache,maz-age=0,must-revalidate should be present']
    elif i == 2:
        elements=['public','immutable','max-age=604800']
        if all(element in value for element in elements):
            return [1,1,'All required header values present']
        else:
            return [1,0,'All values public, immutable, max-age=604800 should be present']
    elif i == 3:
        elements=['no-cache','private','max-age=0']
        if all(element in value for element in elements):
            return [1,1,'All required header values present']
        else:
            return [1,0,'All values no-cache, private, max-age=0 should be present']
    elif i == 4:
        elements=['private','no-transform','max-age=3600','stale-while-revalidate=600']
        if all(element in value for element in elements):
            return [1,1,'All required header values present']
        else:
            return [1,0,'All values private, no-transform, max-age=3600, stale-while-revalidate=600 should be present']
    elif i == 5:
        elements=['public','immutable','stale-if-error=120']
        if all(element in value for element in elements):
            return [1,1,'All required header values present']
        else:
            return [1,0,'All values public, immutable, stale-if-error=120 should be present']
    elif i == 6:
        elements=['no-store','no-cache','s-maxage=0']
        if all(element in value for element in elements):
            return [1,1,'All required header values present']
        else:
            return [1,0,'All values no-store, no-cache, s-maxage=0 should be present']
    else:
        max_age = 0
        if 'max-age' in value:
            max_age = int(value.split('=')[1])
        else:
            if 'no-cache' in value:
                text=''
            else:
                text='Most essential value not set in the header.'

        # Default message for max-age
        if max_age != 0:
            text = 'Recommended value of max-age is 0 for security.'
        elif max_age <= 31536000:
            text = 'Recommended value of max-age is 31536000 for performance but compromises security.'

        # Check if 'public' or 'private' is set
        if 'public' in value:
            if 'must-revalidate' in value:
                return [1, 1, text + ' Properly configured for publicly available content but needs changes for sensitive data.']
            else:
                return [1, 0, text + ' Properly configured for publicly available content, but very less secure']
        elif 'private' in value:
            if 'no-cache' in value and 'must-revalidate' in value:
                return [1, 1, 'Header is properly configured']
            else:
                return [1, 0, 'All the three values max-age=0, no-cache, must-revalidate should be present']
        
        # If neither 'public' nor 'private' is present
        return [1, 0, 'Header present but missing major values like public or private']
    
def no_cache_control(value,i):
    return [0,1,'Header missing and should be added']
