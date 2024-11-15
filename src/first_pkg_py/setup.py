from setuptools import find_packages, setup

package_name = 'first_pkg_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kayttaja',
    maintainer_email='e@ma.il',
    description="Tommi's first ROS2 node!",
    license='At your own risk',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'first_node = first_pkg_py.first_node:main'
        ],
    },
)
