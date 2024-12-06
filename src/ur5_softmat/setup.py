import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ur5_softmat'

data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
]

def package_files(data_files, directory_list):

    paths_dict = {}

    for directory in directory_list:
        
        for (path, directories, filenames) in os.walk(directory):

            for filename in filenames:

                file_path = os.path.join(path, filename)
                install_path = os.path.join('share', package_name, path)
                
                if install_path in paths_dict.keys():
                    paths_dict[install_path].append(file_path)
                    
                else:
                    paths_dict[install_path] = [file_path]
                
    for key in paths_dict.keys():
        data_files.append((key, paths_dict[key]))

    return data_files


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    # packages=find_packages(exclude=['test']),

    # data_files=[
    #     ('share/ament_index/resource_index/packages',
    #         ['resource/' + package_name]),
    #     ('share/' + package_name, ['package.xml']),

    # Include launch and other required files.
    # (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    # (os.path.join('share', package_name, 'models/ur5_base'), glob(os.path.join('models/ur5_base', '*.sdf'))),
    # (os.path.join('share', package_name, 'scripts'), glob(os.path.join('scripts', '*py'))),
    # (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz', '*rviz'))),
    # (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*urdf'))),
    # (os.path.join('share', package_name, 'worlds'), glob(os.path.join('worlds', '*world'))),
    # ],

    data_files=package_files(data_files, ['models/', 'launch/', 'scripts/', 'urdf/', 'rviz/', 'worlds/']),
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
