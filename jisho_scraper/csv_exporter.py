import csv
from pathlib import Path
from typing import List

from jisho_scraper.output_prepare import OutputWord


def output_csv(word_list: List[OutputWord], path: Path):
    with open(path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        __output_to_writer(word_list, writer)


def output_tsv(word_list: List[OutputWord], path: Path):
    with open(path, 'w', newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t', quotechar='"')
        __output_to_writer(word_list, writer)


def __output_to_writer(word_list: List[OutputWord], writer):
    for word in word_list:
        writer.writerow([word.kanji, word.kana, word.meaning])
