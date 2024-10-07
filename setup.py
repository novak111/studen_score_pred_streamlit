from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this func will return the list of requirements
    :param file_path: path of requirements.txt
    :return: list of requirements
    '''
    requirements = []
    with open(file_path) as fle_obj:
        requirements = fle_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='novak111',
    author_email='novak.jn.111@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
