import git
# from src.Importer import *

from src.Content import *
from src.Importer import *
from src.Committer import *

repo = git.Repo("C:/Users/Kaime/Desktop/Work/small_codes")
mock_repo = git.Repo("C:/Users/Kaime/Desktop/Work/MockRepos/small_codes")

importer = Importer([repo], mock_repo)
importer.set_author('kmeinerz@thp.uni-koeln.de')

importer.import_repository()