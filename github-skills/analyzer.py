import pandas as pd


def top_langague(df):
        top_Langauge = df["language"].value_counts().head(3).to_dict()
        return top_Langauge

def analysis_repo(df):
        old_repo =  df[df["created_at"]==df.created_at.min()]["name"].iloc[0]
        new_repo = df[df["created_at"]==df.created_at.max()]["name"].iloc[0]
        most_started_repo = df[df.stargazers_count == df.stargazers_count.max()].name.iloc[0]
        avg_star = df.stargazers_count.mean()
        total_star = df.stargazers_count.sum().astype(int)
        last_active_date = pd.to_datetime(df["updated_at"]).max().date()
        total_repo = df.shape[0]
        analysis = { "Total Stars":total_star , "Average Star":avg_star, "Oldest Repo" : old_repo , "Newest Repo": new_repo,"Most started repo" : most_started_repo,
                    "Total Repos": total_repo , "Last Active Date": last_active_date}
        return analysis