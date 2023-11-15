from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read() 

INSTALL_REQUIRES = []

def doSetup(install_requires):
    setup(
        name='checkprimetestfunction',
        version='0.1',
        author=' Will Chern ',
        author_email='wachern@uw.edu',
        url='https://github.com/wachern/Check_Prime.git',
        description='A function for checking if a number is prime',
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=['checkprimetestfunction'],
        package_dir={'Check_Prime':
            'checkprimetestfunction'},
        install_requires=install_requires,
        include_package_data=True,
        classifiers=[
            'Development Status :: 3 - Alpha',  
            'Intended Audience :: Science/Research',
            'Topic :: Scientific/Engineering',
            'License :: OSI Approved :: MIT License', 
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],
    )

if __name__ == '__main__':
  doSetup(INSTALL_REQUIRES)
