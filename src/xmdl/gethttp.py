import urllib.request
from git import repo

repo = repo("../..")

def get_package() :
    print("niosem AIrOS package")

def get_package_aur() :
    print("Aur package")
    repo.clone(repo)

def GetInScription() :
    print("nopdm")