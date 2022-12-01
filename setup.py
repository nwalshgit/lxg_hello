from setuptools import setup

setup(
    name='lxg_hello',
    version='0.0.1',
    description='A small example package',
    url='https://github.com/nwalshgit/lxg_hello',
    author='Nathan Walsh <nwalsh@example.com>',
    license='MIT',
    packages=['lxg_hello'],
    install_requires=[
       "pandas>=1.5.0",
       "lxg-world==0.0.1",
    ],
    dependency_links=[
        #"git+ssh://git@github.com/nwalshgit/lxg_world.git@0.0.1#egg=lxg_world",
        "https://github.com/nwalshgit/lxg_world.git#egg=lxg_world-0.0.1",
        #"https://github.com/dmfigol/smartsheet-python.sdk/archive/no-setuptools-scm.zip#egg=smartsheet-python-sdk-10.1.3.3"
    ],
    zip_safe=False
)
