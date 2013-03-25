from setuptools import setup, find_packages
import os

name = 'rbco.scripts'

version = '0.0.1-dev'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n'
)


def console_script(module, function='main'):
    return '{script} = {project}.{module}:{function}'.format(
        project=name,
        script=module.split('.')[-1],
        module=module,
        function=function
    )

console_script_modules = [
    'cvs.cvs_bump_version',
    'cvs.cvs_make_version_final',
    'cvs.cvs_tag_current_version',
    'datetime.ddiff',
    'finance.parcelas',
    'latex.latex2html_wrap',
    'latex.latex_flatten',
    'latex.latex_lift',
    'latex.latex_showcites',
    'misc.buildout_versions',
    'misc.ack_ps',
    'misc.ack_kill',
    'misc.ack_find',
    'text.oneline',
    'text.rbeautifysql',
    'text.last_changelog_entry',
    'music.cp_rand_albums',
]

setup(
    name=name,
    version=version,
    description="Little assorted useful scripts.",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='',
    author='Rafael Oliveira',
    author_email='rafaelbco@gmail.com',
    url='http://github.com/rafaelbco/rbco.scripts',
    license='gpl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=[name.split('.')[0]],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'clom',
        'docopt',
        'walkdir',
        'rbco.commandwrap',
        'prdg.util',
        'pathlib',
    ],
    entry_points={'console_scripts': [console_script(m) for m in console_script_modules]},
)
