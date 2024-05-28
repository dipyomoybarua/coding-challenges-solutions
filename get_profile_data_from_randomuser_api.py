import requests

url = "https://randomuser.me/api/?results=5"
response = requests.get(url)
data = response.json()

formatted_data = [
    {
        "profile": {
            "gender": user["gender"],
            "email": user["email"],
            "dob_date": user["dob"]["date"],
            "age": user["dob"].get("age", ""),
            "phone": user["phone"],
            "cell": user["cell"]
        },
        "name": f"{user['name']['title']} - {user['name']['first']} - {user['name']['last']}",
        "location": {
            "street": user["location"]["street"]["name"],
            "city": user["location"]["city"],
            "state": user["location"]["state"],
            "country": user["location"]["country"],
            "postcode": user["location"]["postcode"]
        },
        "version": user.get("version", "")
    }
    for user in data["results"]
]

print(formatted_data)
