from setuptools import setup 
#python setup.py sdist upload -r pypi
#twine check dist/*

# reading long description from file 
with open('resattention/DESCRIPTION.rst') as file: 
	long_description = file.read() 


# specify requirements of your package here 
REQUIREMENTS = ['numpy','tensorflow','keras'] 

# some more details 
CLASSIFIERS = [ 
	'Development Status :: 4 - Beta', 
	'Intended Audience :: Developers', 
	'Topic :: Internet', 
	'License :: OSI Approved :: MIT License', 
	'Programming Language :: Python', 
	'Programming Language :: Python :: 2', 
	'Programming Language :: Python :: 2.6', 
	'Programming Language :: Python :: 2.7', 
	'Programming Language :: Python :: 3', 
	'Programming Language :: Python :: 3.3', 
	'Programming Language :: Python :: 3.4', 
	'Programming Language :: Python :: 3.5'
	] 

# calling the setup function 
setup(name='resattention', 
	version='0.0.3', 
	description='A library for implementing Residual Attention CNN for image classification problems.', 
	long_description=long_description,
	url='https://github.com/garain/resattention', 
	author='Avishek Garain', 
	author_email='avishekgarain@gmail.com', 
	license='MIT', 
	packages=['resattention'],
	package_data={'resattention': ['DESCRIPTION.rst']},
	classifiers=CLASSIFIERS, 
	install_requires=REQUIREMENTS, 
	keywords='attention CNN image-classification'
	) 
