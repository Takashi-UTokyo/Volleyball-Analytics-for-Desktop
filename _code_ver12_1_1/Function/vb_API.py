import http.client

conn = http.client.HTTPSConnection("v1.volleyball.api-sports.io")

headers = {
    'x-rapidapi-host': "v1.volleyball.api-sports.io",
    'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    }

conn.request("GET", "/teams?country=Japan", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))