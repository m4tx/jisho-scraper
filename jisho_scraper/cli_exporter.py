from typing import List

from jisho_scraper.output_prepare import OutputWord

CITALIC = '\33[3m'
CGREEN = '\33[32m'
CBOLD = '\33[1m'
CEND = '\33[0m'


def output_cli(word_list: List[OutputWord]):
    plural = '' if len(word_list) == 1 else 's'
    print(f'{CGREEN}{CBOLD}Added {len(word_list)} new term{plural}:{CEND}')
    for word in word_list:
        print(f'• {word.kanji} ({word.kana}) — {CITALIC}{word.meaning}{CEND}')
