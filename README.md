# Annals

A wrapper built for [my scraping API](https://github.com/revan/RU-Food-Scraper) to collect and serve historical data.

Annals runs whatever script you hand it, saving the output to a file matching the date.
It then updates a symlink to the latest results, and generates a static HTML page linking to everything.

Meant to be called by a cron job, and served statically with `nginx` or `apache`.

## Config file format
```
{
	"command": "./dummy.py",
	"entries": [], // database
	"index": true, // generate HTML?
	"title": "Page Title"
}
```

## TODO
	- Extend to support a merging strategy for APIs that return an array.
	- Configurable GitHub link / project info

## Dependencies
`pip install jinja2`
