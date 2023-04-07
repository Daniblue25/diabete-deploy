from setuptools import find_packages, setup
from typing import List


_E_POINT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    la fontion permettant de retourner la liste des elements contenus dans requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if _E_POINT in requirements:
            requirements.remove(_E_POINT)

    return requirements


setup(
name='Application',
version= '0.0.1',
author= 'Daniblue25',
author_email= 'jeanjacques255@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')

)