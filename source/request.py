import requests
import json
import warnings
from urllib3.exceptions import InsecureRequestWarning
import pandas as pd


warnings.filterwarnings("ignore", category=InsecureRequestWarning)



def inspect_response(url):
    r = requests.get(url, verify=False)
    print()
    print()
    print()

    data = r.json()

    print(json.dumps(data,indent=4))


def stackoverflow():
    r = requests.get("https://api.stackexchange.com/2.3/questions/10667960;78191954?order=desc&sort=activity&site=stackoverflow", verify=False)

    data = r.json()
    print(r.status_code)
    pretty = json.dumps(data,indent=2)

    for item in data["items"]:
        print(item["tags"][0])
        print(item["owner"]["display_name"])
        print(item["link"])
        print(item["title"])
        print()
        print("----------------------------------------")
        print()



def person_info():
    r = requests.get("https://swapi.dev/api/people/",verify=False)
    print()
    print()
    print()
    data = r.json()["results"]

    chosen_data = [{k:v for k,v in obj.items()if k in ["name","birth_year","gender"]} for obj in data]

    for person in chosen_data:
        for key, info in person.items():
            print(f"{key}: {info}")
        print("-------------------------------------------")



def resource_info(base_url, *args,pages = 1, to_df = False, display = False):

   

    if base_url.endswith("/"):
    
        for page in range(pages):

            url = base_url+f"?page={page+1}"

            r = requests.get(url,verify=False)

            data = r.json()

            if "results" in data:

                data = data["results"]

                chosen_data = [{k:v for k,v in obj.items()if k in args} for obj in data]
                if display:
                    for obj in chosen_data:
                        for key, info in obj.items():
                            print(f"{key}: {info}")
                        print("-------------------------------------------")
                
            else:
                print("exceeded ammount of pages")
                break
        
    else:
        r = requests.get(base_url,verify=False)

        data = r.json()

        chosen_data = {k:v for k,v in data.items() if k in args}

        if display:
            for key, info in chosen_data.items():
                print(f"{key}: {info}")
            print("-------------------------------------------")
        print("XDDDDDD43434366666666666664DDDD")

    if to_df:
        if isinstance(chosen_data,list):
            return pd.DataFrame(chosen_data)
        return pd.DataFrame([chosen_data])
        


if __name__ == "__main__":
    result = resource_info("https://swapi.dev/api/people/1","name","birth_year","gender",to_df=True)

