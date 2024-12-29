from basic_passive_scan import basic_scan

def normal_scan(urls):
    result = basic_scan(urls)
    print("Header Check Details:\n")
    for header, values in result.items():
        print(f"Header ---> {header}")
        print(f"  Present: {values[0]}")
        print(f"  Feedback: {values[1]}\n")
        print('----------------------------------------------------------')
    print(f"function performed for {urls}")
