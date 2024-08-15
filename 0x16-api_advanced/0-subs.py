import requests

def number_of_subscribers(subreddit):
    # Define the User-Agent to avoid being blocked by Reddit
    headers = {'User-Agent': 'Python/requests:number_of_subscribers:v1.0.0 (by /u/yourusername)'}
    
    # Construct the URL for the subreddit's about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for a successful response (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the number of subscribers
            subscribers = data.get('data', {}).get('subscribers', 0)
            
            return subscribers
        
        # If the status code indicates a redirect or other failure, return 0
        else:
            return 0
    
    except requests.RequestException as e:
        # Handle any request exceptions
        return 0

# Example usage:
print(number_of_subscribers('python'))  # Replace 'python' with any subreddit you want to check

