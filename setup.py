from setuptools import setup,find_packages
from typing import List

Hypen_dot_e='-e .'

def get_requirements(filepath:str)->[List]:
    requirements=[]
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[req.replace('/n','') for req in requirements]

        if Hypen_dot_e in requirements:
            requirements.remove(Hypen_dot_e)

    return requirements

setup(
    name='Gemstone',
    version='0.0.1',
    author='arpanchakraborty',
    author_email='arpanchakraborty@gmail.com',
    url='github.com/arpanchakraborty23/gemstone.git',
    packages=find_packages(),
    install_requries=get_requirements('requirements.txt')
)        