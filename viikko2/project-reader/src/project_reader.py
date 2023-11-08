from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        parsed_toml = toml.loads(content)
        #print(parsed_toml)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])
        name = parsed_toml["tool"]["poetry"]["name"]
        description = parsed_toml["tool"]["poetry"]["description"]
        license_ = parsed_toml["tool"]["poetry"]["license"]
        authors = parsed_toml["tool"]["poetry"]["authors"]
        dependencies = parsed_toml["tool"]["poetry"]["dependencies"]
        dev_dependencies = parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"]

        return Project(name, description, license_,authors, dependencies, dev_dependencies)
