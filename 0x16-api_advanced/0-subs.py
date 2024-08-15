import requests

def top_ten(subreddit):
    # Define the User-Agent to avoid being blocked by Reddit
    headers = {'User-Agent': 'Python/requests:top_ten:v1.0.0 (by /u/yourusername)'}
    
    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for a successful response (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of posts
            posts = data.get('data', {}).get('children', [])
            
            # Print the title of each post
            for post in posts:
                print(post['data']['title'])
        
        # If the status code indicates a redirect or other failure, print None
        else:
            print(None)
    
    except requests.RequestException as e:
        # Handle any request exceptions
        print(None)

# Example usage:
top_ten('python')  # Replace 'python' with any subreddit you want to check

