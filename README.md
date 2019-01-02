# blog

https://manage-it.github.io/blog/

## Build prequisities

```
# clone via https or ssh, recursive for @themes @plugins
git clone --recursive git@github.com:manage-it/blog.git

cd blog/

# create virtualenv
# if use pyenv:
#     pyenv virtualenv 3.6.7 venv-manage-it
virtualenv venv-manage-it

pip install -r requirements.txt


# Copy theme to working folder
pelican-themes --install ./pelican-themes/pelican-bootstrap3 --verbose

# Listing out themes:
pelican-themes -l

# Local Develop
make html & make devserve

# access
http://localhost:8000/
```

## Publish to the website

build in `publish` mode and push to the branch `gh-pages`
```
make publish
ghp-import output
git push origin gh-pages
```
## Change theme
```
pelican-themes --install ./pelican-themes/pelican-bootstrap3 --verbose
# edit ./pelicanconf.py THEME
```
