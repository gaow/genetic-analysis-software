## Basic setup
```bash
git clone https://github.com/matcornic/hugo-theme-learn.git themes/hugo-theme-learn
rm -rf themes/hugo-theme-learn/.git*
echo '''theme = "hugo-theme-learn"''' >> config.toml
```
## Create chapter folders
```
for x in 0 1 {a..z}; do hugo new --kind chapter $x/_index.md; done
```
## Enable search functionality
(not yet working)
```
npm install lunr-hugo
sudo ln -s /usr/bin/nodejs /usr/bin/node
mkdir -p static/json
node_modules/.bin/lunr-hugo -i content/**/*.md -o static/json/search.json -l toml
```
## Page specific disqus
This is essentially writing raw HTML to markdown file in HUGO, which involves using `shortcodes`:
```
mkdir -p layouts/shortcodes/
echo "{{ .Inner }}" > layouts/shortcodes/raw.html
```
Then see `disqus_tpl` related code in `UpdateHTML.sos`
