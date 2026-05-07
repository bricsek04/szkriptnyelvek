import json

def main():
    f = open("orai_anyagok/pearson.json")
    data = json.load(f)
    
    print(data)
    print(type(data))

    print(data["name"])

    print(data["daughter"]["age"])
    
    f.close()

    f = open("orai_anyagok/earthporn.json")
    earth_data = json.load(f)
    for post in earth_data["data"]["children"]:
        print(post['data']['url'])

    f.close()

if __name__ == "__main__":
    main()