import os

ENV = '{{ cookiecutter.environment }}'

os.rename('./{}.env'.format(ENV), '../{}.env'.format(ENV))
os.chdir('..')
os.rmdir('./{}.env.d'.format(ENV))
