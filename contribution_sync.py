import git
import os
# from src.Importer import *

from src.Content import *
from src.Importer import *
from src.Committer import *


folder_path = '/home/kmeinerz/Desktop/Work/'
# list_repos = ['rsc', 'qec', 'paper_qec', 'qec_code', 'ft_qec', 'topologicalcodes', 'machinelearning', 'thesis', 'small_codes']
list_repos = ['small_codes']


for repos in list_repos:
    print(f'syncing {repos}')
    repo = git.Repo(f"{folder_path}/{repos}")
    mock_repo = git.Repo(f"{folder_path}/MockRepos/{repos}")

    importer = Importer([repo], mock_repo)
    importer.set_author('kmeinerz@thp.uni-koeln.de')

    importer.import_repository()
    os.system( f"cd {folder_path}MockRepos/{repos}/ \n git push" )
