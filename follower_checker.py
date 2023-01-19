import json 

with open('followers.json','r') as f:
    followers = json.load(f)
with open('following.json','r') as f:
    following = json.load(f)
    
    
followers_set = set(follower['username'] for follower in followers['followers'])

not_following_back = [user['username'] for user in following['following'] if user['username'] not in followers_set]

for username in not_following_back:
    print(username)
    
    
    """
    creating a followers set to check if the user is in the followers list
    
    the psuedo code is for followers_set:
        for each follower in the list of followers
            add the value of the username key of the follower to the followers set
    
    """