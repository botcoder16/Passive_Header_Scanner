from fetching_2 import fetch_messages
from basic_headers.Cache_Control import cache_control,no_cache_control
from basic_headers.X_Frame_Options import x_frame_options,no_x_frame_options
from basic_headers.Content_Security_Policy import content_security_policy, no_content_security_policy
from basic_headers.Strict_Transport_Security import strict_transport_security, no_strict_transport_security
from basic_headers.Access_Control_Allow_Origin import access_control_allow_origin ,no_access_control_allow_origin
from basic_headers.Cross_Origin_Embedder_Policy import cross_origin_embedder_policy, no_cross_origin_embedder_policy
from basic_headers.Cross_Origin_Opener_Policy import cross_origin_opener_policy, no_cross_origin_opener_policy
from basic_headers.Cross_Origin_Resource_Policy import cross_origin_resource_policy, no_cross_origin_resource_policy
from basic_headers.Clear_Site_Data import clear_site_data, no_clear_site_data
from basic_headers.Permissions_Policy import permissions_policy, no_permissions_policy 
from basic_headers.Referrer_Policy import referrer_policy, no_referrer_policy
from basic_headers.X_Permitted_Cross_Domain_Policies import x_permitted_cross_domain_policies, no_x_permitted_cross_domain_policies
from basic_headers.X_Content_Type_Options import x_content_type_options, no_x_content_type_options
import pprint


def basic_scan(url,i):

    request_test_headers, response_test_headers = fetch_messages(url)
    header_functions = {
        'cache-control': cache_control,
        'x-frame-options': x_frame_options,
        'x-content-type-options': x_content_type_options,
        'content-security-policy': content_security_policy,
        'strict-transport-security':  strict_transport_security,
        'access-control-allow-origin':  access_control_allow_origin,
        'cross-origin-embedder-policy': cross_origin_embedder_policy,
        'cross-origin-opener-policy': cross_origin_opener_policy,
        'cross-origin-resource-policy': cross_origin_resource_policy,
        'clear-site-data': clear_site_data,
        'permissions-policy':permissions_policy,
        'referrer-policy': referrer_policy,
        'x-permitted-cross-domain-policies': x_permitted_cross_domain_policies,
    }
    
    header_missing_function ={
        'cache-control': no_cache_control,
        'x-frame-options': no_x_frame_options,
        'x-content-type-options': no_x_content_type_options,
        'content-security-policy': no_content_security_policy,
        'strict-transport-security': no_strict_transport_security,
        'access-control-allow-origin':  no_access_control_allow_origin,
        'cross-origin-embedder-policy': no_cross_origin_embedder_policy,
        'cross-origin-opener-policy': no_cross_origin_opener_policy,
        'cross-origin-resource-policy': no_cross_origin_resource_policy,
        'clear-site-data': no_clear_site_data,
        'permissions-policy':no_permissions_policy,
        'referrer-policy': no_referrer_policy,
        'x-permitted-cross-domain-policies': no_x_permitted_cross_domain_policies,    
    }
    header_check={
        'cache-control': [0,0,''],
        'x-frame-options': [0,0,''],
        'x-content-type-options': [0,0,''],
        'content-security-policy': [0,0,''],
        'strict-transport-security': [0,0,''],
        'access-control-allow-origin': [0,0,''],
        'cross-origin-embedder-policy': [0,0,''],
        'cross-origin-opener-policy': [0,0,''],
        'cross-origin-resource-policy': [0,0,''],
        'clear-site-data': [0,0,''],
        'permissions-policy':[0,0,''],
        'referrer-policy': [0,0,''],
        'x-permitted-cross-domain-policies': [0,0,''],
    }

    unique_response_headers=[]
    for headers in response_test_headers:
        if headers in unique_response_headers:
            continue
        else:
            unique_response_headers.append(headers)
    
    print(len(unique_response_headers))
    
    for dict_temp in unique_response_headers:
        normalized_headers = {key.lower(): value for key, value in dict_temp.items()}

        # Check each predefined header and call the corresponding function if present
        for header, func in header_functions.items():
            if header_check[header][0] != 1:
                if header in normalized_headers:
                        output=func(normalized_headers,i)
                        header_check[header] = output
                else:
                    output = header_missing_function[header](normalized_headers,i)
                    header_check[header] = output
            else :
                continue
    #pprint.pprint(unique_response_headers ) 
    pprint.pprint(header_check)
    print()