from typing import List

from jisho_scraper.anki_connect_client import AnkiConnectClient, Note
from jisho_scraper.output_prepare import OutputWord

MODEL_NAME_KANJI = 'jisho-scraper (kanji + kana + meaning)'
MODEL_NAME_NO_KANJI = 'jisho-scraper (kana + meaning)'
KANJI_FIELD_NAME = 'Kanji'
KANA_FIELD_NAME = 'Kana'
MEANING_FIELD_NAME = 'Meaning'


def output_anki_connect(word_list: List[OutputWord], deck_name: str):
    notes = [output_word_to_note(x, deck_name) for x in word_list]
    AnkiConnectClient().add_notes(notes)


def output_word_to_note(output_word: OutputWord, deck_name: str) -> Note:
    model_name = (MODEL_NAME_KANJI if output_word.kanji
                  else MODEL_NAME_NO_KANJI)
    fields = {
        KANA_FIELD_NAME: output_word.kana,
        MEANING_FIELD_NAME: output_word.meaning,
    }
    if output_word.kanji:
        fields[KANJI_FIELD_NAME] = output_word.kanji

    return Note(deck_name, model_name, fields, [])
