# blog

## Publish

build in `publish` mode and push to the branch `gh-pages`
```
make publish
ghp-import output
git push origin gh-pages
```
## Local Develop

```
make html & make devserve
```

## Change theme
```
pelican-themes --install ./pelican-themes/pelican-bootstrap3 --verbose
# edit ./pelicanconf.py THEME
```

## From Scratch

```
git submodule add https://github.com/getpelican/pelican-themes.git
pelican-themes --install ./pelican-themes/pelican-bootstrap3 --verbose
pelican-themes -l

git submodule add https://github.com/getpelican/pelican-plugins
# conf plugins
```

