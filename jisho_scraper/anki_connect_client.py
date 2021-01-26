from dataclasses import dataclass
from typing import Dict, List

import requests


@dataclass
class Note:
    deck_name: str
    model_name: str
    fields: Dict[str, str]
    tags: List[str]

    def to_json(self):
        return {
            'deckName': self.deck_name,
            'modelName': self.model_name,
            'fields': self.fields,
            'tags': self.tags,
        }


class AnkiConnectClient:
    def __init__(self, host: str = 'localhost', port: int = 8765):
        self.host = host
        self.port = port

    def add_notes(self, notes: List[Note]):
        notes_json = [note.to_json() for note in notes]
        payload = {
            'action': 'addNotes',
            'version': 6,
            'params': {
                'notes': notes_json
            }
        }
        r = requests.post(f'http://{self.host}:{self.port}/', json=payload)
        r.raise_for_status()
