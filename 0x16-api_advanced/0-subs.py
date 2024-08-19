        
        # If the status code indicates a redirect or other failure, return 0
        else:
            return 0
    
    except requests.RequestException as e:
        # Handle any request exceptions
        return 0

# Example usage:
print(number_of_subscribers('python'))

