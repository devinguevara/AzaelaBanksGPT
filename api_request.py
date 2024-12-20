import requests
import os
import json

# all of this is straight from twitter developer platform. This basically gets a JSON from my request. 
# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '(from:azealiaslacewig -is:retweet) OR #azealiaslacewig','tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# Here I will be saving the request into a json file, this is my code
def make_response_file(response, filename): 
    with open(filename, 'w') as json_file: 
        json.dump(respone, json_file, indent= 4, sort_keys= True)
    print(f"Response Saved as {filename}")

def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print("OMG did we actually do it?")
    #print(bearer_token)

if __name__ == "__main__":
    main()