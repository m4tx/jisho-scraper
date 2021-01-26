from dataclasses import dataclass
from typing import List

from jisho_scraper.jisho_data import WordData, Sense


@dataclass
class OutputWord:
    kanji: str
    kana: str
    meaning: str


def word_list_to_output(word_list: List[WordData]) -> List[OutputWord]:
    return [__process_word_data(x, word_list) for x in word_list]


def __process_word_data(word_data: WordData,
                        word_list: List[WordData]) -> OutputWord:
    kanji = word_data.japanese[0].word
    kana = word_data.japanese[0].reading
    same_reading = [x.japanese[0].word for x in word_list
                    if x != word_data and x.japanese[0].reading == kana]
    if same_reading:
        kana = f'{kana} (not: {", ".join(same_reading)})'

    meaning = '; '.join(', '.join(x.english_definitions)
                        for x in word_data.senses
                        if __filter_sense(x))

    return OutputWord(kanji, kana, meaning)


def __filter_sense(sense: Sense) -> bool:
    if 'Wikipedia definition' in sense.parts_of_speech:
        return False
    if 'Archaism' in sense.tags:
        return False

    return True
