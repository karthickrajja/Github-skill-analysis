import pandas as pd
import requests as rq

def get_user(username):
    url = f"https://api.github.com/users/{username}"
    response = rq.get(url = url , timeout= 10)
    if response.status_code == 200:
        return response.json()
    else: 
        return None
    
def get_basic_info(username):
    info = get_user(username)
    if info is not None:
        return {"Name":info["name"],
                "Username":info["login"],
                "Following":info["following"],
                "Public Repos": info["public_repos"]}
    else :
        return None

def get_user_repo(username):
    url = f"https://api.github.com/users/{username}/repos"
    responce = rq.get(url=url, timeout= 10)
    if responce.status_code == 200:
        return responce.json()
    else:
        return None
    
def get_repo_data(username):
    repo_data = get_user_repo(username)
    if repo_data is None:
        return None
    else :
        return repo_data
    
    


