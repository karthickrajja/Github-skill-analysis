


def get_report(basic_info , top_langagues, analyz):
    print(f"====================================\nGitHub Profile Analysis\n====================================\nDeveloper\nName: {basic_info['Name']}\nFollowing : {basic_info['Following']}\nPublic Repos: {basic_info['Public Repos']}")
    print(f"====================================\nRepository Analysis\nTop Languages")
    for i , j in top_langagues.items():
        print(i,j)
    print(f"====================================\nRepository Statistics\n------------------------------------")
    for i , j in analyz.items():
        print(i,j)



def identify_skills(repo_data):
    words = []
    for i in repo_data:
        words.append(i["name"])
        words.append(i['description'])
        for j in i["topics"]:
            words.append(j)
    word_lower = []
    for i in words:
        if i != None:
            word_lower.append(i.lower())
    return word_lower



def check_skills(words):
    skills = {"Python": ["python"],"SQL": ["sql", "mysql", "postgres"],"Pandas": ["pandas"],"NumPy": ["numpy"],"FastAPI": ["fastapi"],"Docker": ["docker"],"Git": ["git"]}
    status = {}
    for i , j in skills.items():
        for skill in j:
            if skill in words:
                status[i] =  "Yes"
                break
        else :
            status[i] =  "No"
    return status