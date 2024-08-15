#Reason for setup.py:Building app as a package using setup.py

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
   '''
   This Func will return the list of requriments
   '''
   requriments=[]
   with open(file_path) as file_obj:
      requriments=file_obj.readlines()
      requriments=[req.replace('\n','') for req in requriments]

      if HYPEN_E_DOT in requriments:
         requriments.remove(HYPEN_E_DOT)
   return requriments

setup(
   name='ML-Project-Generic',
   version='0.0.1',
   author='Tushar-Chaudhari',
   author_email='tushar.c8942@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt')
)

