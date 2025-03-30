from setuptools import find_packages, setup

from typing import List

HYPEN_E_DOT='-3 .'
def get_requirements(file_path:str)->List[str]:
    '''
This function will return a list of requriements

    '''     
    requirements=[]

    with open(file_path) as file_obj:
        rrequirements=file_obj.readlines()

        [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
        
setup(
    name="mlproject",
    version="0.01",
    author='Amrit',
    author_email='amrit.sequeira@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
    
    )



