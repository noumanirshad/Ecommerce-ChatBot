import setuptools
from typing import List

# with open("README.md", "r", encoding='utf-8') as f:
#     long_description = f.read()
# repo_description = "This is repo description "
# long_description = "This is long description"
# REPO_NAME = " repo_Name "
# url = f"https://github.com/noumanirshad/local_setup "


hy_e = '-e .'

def get_requirements(path: str) -> List[str]:
    '''Returns a list of requirements'''
    requirement = []
    with open(path, 'r') as f: 
        requirement = f.readlines()
        requirement = [req.replace('\n', '') for req in requirement]
        if hy_e in requirement:
            requirement.remove(hy_e)
    return requirement


__version__ = "0.0.0"

AUTHOR_USER_NAME = "noumanirshad"
SRC_REPO = "Local_setup_For-AI_Development"
AUTHOR_EMAIL = "noumanirshad564@gmail.com"


setuptools.setup(    
    version=__version__,
    author= AUTHOR_USER_NAME, 
    author_email= AUTHOR_EMAIL,    
    long_description_content= "text/markdown",    
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',        
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    license="MMIT License",
    include_package_data=True,
    install_requires=get_requirements('requirements.txt'),
    zip_safe=False,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    # long_description=long_description,
    # name=SRC_REPO,
    # url = url,
    # project_urls = {
    #     "Bug Tracker": url,
    # },
)

