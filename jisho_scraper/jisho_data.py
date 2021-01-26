from dataclasses import dataclass
from typing import List, Optional, Dict


@dataclass
class Japanese:
    word: Optional[str] = None
    reading: Optional[str] = None


@dataclass
class Link:
    text: str
    url: str


@dataclass
class Source:
    language: str
    word: str


@dataclass
class Sense:
    english_definitions: List[str]
    parts_of_speech: List[Optional[str]]
    links: List[Link]
    tags: List[str]
    restrictions: List[str]
    see_also: List[str]
    antonyms: List[str]
    source: List[Source]
    info: List[str]
    sentences: Optional[List[str]] = None


@dataclass
class WordData:
    slug: str
    tags: List[str]
    jlpt: List[str]
    japanese: List[Japanese]
    senses: List[Sense]
    attribution: Dict[str, bool]
    is_common: bool = False
