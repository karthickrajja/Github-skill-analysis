


def get_report(basic_info , top_langagues, analyz):
    print(f"====================================\nGitHub Profile Analysis\n====================================\nDeveloper\nName: {basic_info['Name']}\nFollowing : {basic_info['Following']}\nPublic Repos: {basic_info['Public Repos']}")
    print(f"====================================\nRepository Analysis\nTop Languages")
    for i , j in top_langagues.items():
        print(i,j)
    print(f"====================================\nRepository Statistics\n------------------------------------")
    for i , j in analyz.items():
        print(i,j)