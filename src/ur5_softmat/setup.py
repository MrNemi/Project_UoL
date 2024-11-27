import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ur5_softmat'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

    # Include launch and other required files.
    (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    (os.path.join('share', package_name, 'models/ur5e'), glob(os.path.join('models/ur5e', '*sdf'))),
    #(os.path.join('share', package_name, 'scripts'), glob(os.path.join('scripts', '*launch.[pxy][yma]*'))),
    #(os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz', '*rviz'))),
    (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*urdf'))),
    (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*world'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Emmanuel W Ombo',
    maintainer_email='manny@liverpool.ac.uk',
    description='Packages and launch files for UR5e Robotic Arm Gazebo Simulation',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
