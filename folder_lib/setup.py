try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import used_car_prediction_lib


def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='used_car_prediction_lib',
    version=used_car_prediction_lib.__version__,
    description='used_car_prediction_lib',
    author=['Ed Monbiot','Mathieu Breier','Luke Atazona','Wu Hangze'],
    
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    url='https://github.com/monbiote/Used_Car_Predictor',
    classifiers=[
        'Programming Language :: Python :: 3.12.0'
    ]
)
