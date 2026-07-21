from api import get_user
from api import get_basic_info
from api import get_user_repo
from api import get_repo_data
from analyzer import analysis_repo
from analyzer import top_langague
from reports import get_report
from reports import identify_skills
from reports import check_skills
import pandas as pd

username = "karthickrajja"

repo_data = get_repo_data(username)

df = pd.DataFrame(repo_data)

basic_info = get_basic_info(username)
top_langagues = top_langague(df)
analyz = analysis_repo(df)

print(check_skills(identify_skills(repo_data)))

