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
    
def analysis_repo(df):
        top_Langauge = df["language"].value_counts().head(3).to_dict()
        old_repo =  df[df["created_at"]==df.created_at.min()]["name"].iloc[0]
        new_repo = df[df["created_at"]==df.created_at.max()]["name"].iloc[0]
        most_started_repo = df[df.stargazers_count == df.stargazers_count.max()].name.iloc[0]
        avg_star = df.stargazers_count.mean()
        total_star = df.stargazers_count.sum().astype(int)
        last_active_date = pd.to_datetime(df["updated_at"]).max().date()
        total_repo = df.shape[0]
        analysis = {"Top_Langauge":top_Langauge , "Oldest Repo" : old_repo , "Newest Repo": new_repo,"Most started repo" : most_started_repo,
                    "Total Repos": total_repo , "Total Stars":total_star, "Average Star":avg_star, "Last Active Date": last_active_date}
        return analysis
    
    


