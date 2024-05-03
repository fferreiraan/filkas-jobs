# import requests
import subprocess

# Função para verificar se há pull requests abertos para uma determinada branch remota
def has_open_pull_requests(owner: str, repo: str, branch_name: str):
    # url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    # params = {
    #     "base": branch_name,
    #     "state": "open"
    # }
    # response = requests.get(url, params=params)
    # return len(response.json()) > 0
    pass

def delete_branches(branches_to_delete: list):

    for branch in branches_to_delete:
        # Verifica se há pull requests abertos associados à branch remota
        if not has_open_pull_requests("<owner>", "<repo>", branch):
            # Deleta a branch local
            subprocess.run(["git", "branch", "-D", branch])
            print(f"Branch local '{branch}' deletada com sucesso.")

            # Deleta a branch remota correspondente
            subprocess.run(["git", "push", "origin", "--delete", branch])
            print(f"Branch remota '{branch}' deletada com sucesso.")
        else:
            print(f"Branch '{branch}' possui pull request(s) aberto(s) e não será deletada.")


BRANCHES_EXCLUDE = [
    'main',
    'develop'
]

if __name__ == '__main__':

    # Lista todas as branches locais, exceto main e develop
    output = subprocess.check_output(["git", "branch", "--format='%(refname:short)'"]).decode("utf-8")
    branches_to_delete = [branch.strip("'") for branch in output.split("\n") if branch.strip("'").lower() not in BRANCHES_EXCLUDE]


