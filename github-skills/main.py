from api import get_user
from api import get_basic_info
from api import get_user_repo
from api import get_repo_data
from api import analysis_repo
import pandas as pd

username = "karthickrajja"

repo_data = get_repo_data(username)

df = pd.DataFrame(repo_data)

print(analysis_repo(df))
