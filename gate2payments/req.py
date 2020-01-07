import requests

url = "https://test.oppwa.com/v1/checkouts/"
params = {
    'entityId': '8a8294174ed9c2b5014ede67e92406ef',
    'amount': "92.00",
    'currency': "EUR",
    'paymentType': "DB",
    'createRegistration': "true"
}

headers = {"Authorization": "Bearer OGE4Mjk0MTc0ZWQ5YzJiNTAxNGVkZTY3ZTkzMjA2ZjN8SjR5SnhUYkNncw==",
            "Content-Type": "application/x-www-form-urlencoded"}

r = requests.get(url, params=params, headers=headers)
print(r.json())
print("REEEEE")