## Contribution Guidelines
Numerous analysis software are being developed as our field continues to flourish. We need your contribution to keep the list up-to-date!

To contribute, please provide information of the software in `*.ini` format taking the form of [this template](https://raw.githubusercontent.com/gaow/genetic-analysis-software/master/db/template.ini). You may include less properties of the software than the template suggests (for example it may not have a version number or executable names) but please do not introduce new properties as they will be ignored when the pages are generated.

Once you have completed the `*.ini` file, you may either fork this repository, add the `*.ini` file to `db` folder, commit and send a github pull request, or you can simply email the `*.ini` file to <gaow@uchicago.edu> preferably with the phrase "Rockefeller List" in your email subject.

### Format of long text
If you have a long section e.g. for the `DESCRIPTION` section where there are multiple paragraphs and bullet points, you need to use `\\` to separte paragraphs and `\\*` for bullet points. For example in your `*.ini` file, 

```
DESCRIPTION=Paragrah 1 \\ Paragraph 2 \\* Point 1 \\* Point 2
``` 

will render the following text:

#### Description
Paragraph 1

Paragraph 2

* Point 1
* Point 2