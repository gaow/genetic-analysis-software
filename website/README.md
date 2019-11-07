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
## Page specific disqus
This is essentially writing raw HTML to markdown file in HUGO, which involves using `shortcodes`:
```
mkdir -p layouts/shortcodes/
echo "{{ .Inner }}" > layouts/shortcodes/raw.html
```
Then see `disqus_tpl` related code in `release.sos`
