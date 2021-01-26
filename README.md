# jisho-scraper

Jisho scraper capable of outputting search results to CSV or Anki.

## Requirements

* Python 3.7+

## Installation

```shell
pip install jisho-scraper
```

## Usage

```
jisho-scraper [-h] [--csv PATH] [--tsv PATH] [--anki DECK] search_keyword
```

CSV/TSV exports the search results in "kanji,kana,meaning" form.

Anki exporting feature requires [AnkiConnect](https://foosoft.net/projects/anki-connect/) to be installed with default settings (listening on `http://localhost:8765`). The app assumes that the there are `jisho-scraper (kanji + kana + meaning)` and `jisho-scraper (kana + meaning)` Anki note types available with `Kanji`, `Kana`, and `Meaning` fields.
