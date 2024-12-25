from basic_passive_scan import basic_scan

def normal_scan(urls):
    basic_scan(urls)
    print(f"function performed for {urls}")
    
def category_scan(category,urls):
    if category in ['Shopping','Finance','Autos_and_Vehicles']:
        basic_scan(urls,1)
        print(f"function performed for E-Commerce and Transactions {urls}")
    elif category in ['News_and_Media','Books_and_Literature','Law_and_Government','Reference','Career_and_Education','Adult (Sensitive)','Gambling (Sensitive)']:
        basic_scan(urls,2)
        print(f"function performed for Static and Moderated Content {urls}")
    elif category in ['Internet_and_Telecom','Computer_and_Electronics','People_and_Society','Business_and_Industry','Home_and_Garden','Recreation_and_Hobbies','Pets_and_Animals']:
        basic_scan(urls,3)
        print(f"function performed for Dynamic and Utility Sites {urls}")
    elif category in ['Travel','Food_and_Drink','Beauty_and_Fitness']:
        basic_scan(urls,4)
        print(f"function performed for Hybrid or Mixed-Content Sites {urls}")
    elif category in ['Arts_and_Entertainment','Games','Sports']:
        basic_scan(urls,5)
        print(f"function performed for Media and Entertainment {urls}")
    elif category in ['Science']:
        basic_scan(urls,6)
        print(f"function performed for Technical or Specialized Services {urls}")