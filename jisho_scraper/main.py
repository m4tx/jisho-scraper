import argparse

from jisho_scraper.anki_exporter import output_anki_connect
from jisho_scraper.csv_exporter import output_csv, output_tsv
from jisho_scraper.jisho_client import search_word
from jisho_scraper.output_prepare import word_list_to_output


def main():
    parser = argparse.ArgumentParser(
        description='Retrieve word definitions from www.jisho.org and '
                    'output them in a convenient format.')
    parser.add_argument(
        'search_keyword', type=str, help='keyword to look for')
    parser.add_argument(
        '--csv', metavar='PATH', type=str,
        help='path to save the CSV (comma-separated values) file at')
    parser.add_argument(
        '--tsv', metavar='PATH', type=str,
        help='path to save the TSV (tab-separated values) file at')
    parser.add_argument(
        '--anki', metavar='DECK', type=str,
        help='Anki deck name to export the definitions to')

    args = parser.parse_args()
    run(args)


def run(args):
    results = search_word(args.search_keyword)
    out_words = word_list_to_output(results)

    if args.csv:
        output_csv(out_words, args.csv)

    if args.tsv:
        output_tsv(out_words, args.tsv)

    if args.anki:
        output_anki_connect(out_words, args.anki)


if __name__ == '__main__':
    main()
