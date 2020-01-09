import requests
import urllib


def prepare_the_checkout():

    url = "https://test.oppwa.com/v1/checkouts"

    payload = urllib.parse.urlencode(
                {
                "entityId": "8a8294174ed9c2b5014ede67e92406ef",
                "amount": "955.00",  # decimal part must be 2 digits
                "currency": "EUR",
                "paymentType": "DB"
                }
    )
    headers = {
        'Authorization': "Bearer OGE4Mjk0MTc0ZWQ5YzJiNTAxNGVkZTY3ZTkzMjA2ZjN8SjR5SnhUYkNncw==",
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response



if __name__ == "__main__":
    print(prepare_the_checkout().json()["id"])