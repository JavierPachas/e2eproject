from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function return the list of requirements
    '''
    requirements = []
    HYPEN_E_DOT = "-e ."

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(    
    name="e2eproject",
    version="0.0.1",
    author="Javier Pachas",
    author_email="javalepc@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)   