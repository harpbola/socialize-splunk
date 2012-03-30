from developer_notify import argv_to_dict, handle_search, main

sample_local_argv = [
    '/opt/splunk/bin/scripts/notify.py', 
    '1', 
    'source="/mnt/logs/nginx-prod.log" | rex "\\:00 (?P<host_ip>[^\\s]+) " | rex field=UserAgent "^(?P<platform>[^-]+)-(?P<platform_version>[^\\/]+)\\/(?P<device_name>.+)\\sSocializeSDK" | stats avg(ResponseTime) AS "average_reponse_time", p80(ResponseTime) AS "p80_reponse_time", count AS "request_count", count(eval(ResponseCode<400)) AS "success_count", count(eval(ResponseCode>=400)) AS "failure_count", count(eval(ResponseCode>=500)) AS "error_count", count(eval(platform="Android")) AS "android_count", count(eval(platform="iOS")) AS "ios_count"', 'source="/mnt/logs/nginx-prod.log" | rex "\\:00 (?P<host_ip>[^\\s]+) " | rex field=UserAgent "^(?P<platform>[^-]+)-(?P<platform_version>[^\\/]+)\\/(?P<device_name>.+)\\sSocializeSDK" | stats avg(ResponseTime) AS "average_reponse_time", p80(ResponseTime) AS "p80_reponse_time", count AS "request_count", count(eval(ResponseCode<400)) AS "success_count", count(eval(ResponseCode>=400)) AS "failure_count", count(eval(ResponseCode>=500)) AS "error_count", count(eval(platform="Android")) AS "android_count", count(eval(platform="iOS")) AS "ios_count"', 
    'Summary -- HTTP by Hour', 
    'Saved Search [Summary -- HTTP by minute] always(1)', 
    'http://logs.getsocialize.com:8000/app/search/@go?sid=scheduler_c3BsdW5rX2JvdA__search_U3VtbWFyeSAtLSBIVFRQIGJ5IG1pbnV0ZQ_at_1333140960_0e62db912459d27b', '', 
    'sample_search_result/results.csv.gz'
]
 

#===============================================================================
# argv_to_dict
#===============================================================================
def test_argv_to_dict():
    print argv_to_dict(sample_local_argv)
    
#test_argv_to_dict()


#===============================================================================
# handle_search
#===============================================================================
def test_handle_search():
    argv = argv_to_dict(sample_local_argv)
    handle_search(argv)
    
test_handle_search()

#===============================================================================
# main
#===============================================================================
def test_main():
    main()
#test_main()    