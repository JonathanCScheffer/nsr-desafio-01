import requests

if __name__ == '__main__':

    # Replace 'YOUR_API_KEY' with your NASA API key (if you have one).
    api_key = 'bnvTjBtcQw3qpbgQbTCo9aFl9dGvPIaf9YALJGw4'
    base_url = 'https://api.nasa.gov/planetary/apod'

    params = {
        'api_key': api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Now, you can access the APOD data from the 'data' dictionary.
        print(data)
    else:
        print(f"Failed to retrieve APOD data. Status code: {response.status_code}")