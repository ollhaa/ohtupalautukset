class Project:
    def __init__(self, name, description, license_,authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license_
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        #return ", ".join(dependencies) if len(dependencies) > 0 else "-"
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\n"
            f"Authors: \n- {self._stringify_dependencies(self.authors)}"
            f"\n"
            f"\n"
            f"Dependencies: \n- {self._stringify_dependencies(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: \n- {self._stringify_dependencies(self.dev_dependencies)}"
        )
