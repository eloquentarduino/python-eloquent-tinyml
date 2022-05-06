from distutils.core import setup

packages=["eloquent_tinyml", "eloquent_tinyml.getting_started", "eloquent_tinyml.getting_started.iris"]

setup(
  name='eloquent_tinyml',
  packages=packages,
  version='0.0.1',
  license='MIT',
  description='A collection of utilities to perform TinyML from Python',
  author='Simone Salerno',
  author_email='support@eloquentarduino.com',
  url='https://github.com/eloquentarduino/python-eloquent-tinyml',
  download_url='https://github.com/eloquentarduino/python-eloquent-tinyml/blob/master/dist/eloquent_tinyml-0.0.1.tar.gz?raw=true',
  keywords=[
    'ML',
    'machine learning'
  ],
  install_requires=[
    'sklearn',
    'everywhereml',
  ],
  package_data={

  },
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Code Generators',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
