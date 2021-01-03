#!/usr/bin/env python3

'''
# CGI script for routing remote requests for processing through to marsden
# Uses socket-server methods
#
# Does/will support ...
# (i) socket_testing
# (ii) orbit-fitting (orbit extension)
# (iii) initial orbit determination
# () ...
#
# While this is pretty primitive, I'm not sure whether there is much value in
# creating anything more sophisticated, given that we probably don't want
# to use this approach for very long ...
'''

# Dict to map allowed calling script to ...
allowed_calling_scripts = {
    'remote_test.py'    : True ,
    'remote_iod.py'     : True ,
    'remote_orbfit.py'  : True ,
}


def process_cgi_string(input_str, calling_file):
    
    
    try:

        # Convert the string to a dictionary
        input_dict = json.loads(input_str)
    
        # Depending on the content of the input, route to the appropriate destination
        assert calling_file in allowed_calling_scripts,
            f'{calling_file} not in allowed_calling_scripts'
        
        # wrapping the input dict in a higher dict to pass in the type of request being made
        request_type = allowed_calling_scripts[calling_file]
        request_dict = {request_type:input_dict}
        
        # instantiate
        C = sc.Client(port=destination_port)

        # Call client-connect func with the content from the input dict
        result_dict = C.connect(request_dict)
    
  except Exception as e :
    result_dict = { 'exception':f'{e}' ,
                    'file':'remote.cgi'}

else:
  result_dict = {   'exception':'Empty input:This API needs to be supplied with json-input that is valid for orbit-fitting',
                    'file':'remote.cgi'}

except Exception as e :
result_dict = {   'exception':f'{e}' ,
                'file':'remote.cgi' }

# This should cause the result to be returned to the submitter ...
print( json.dumps( result_dict ) )