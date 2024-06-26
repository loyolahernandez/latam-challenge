from typing import List, Tuple
import json
from collections import Counter
from datetime import datetime
import emoji


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emojis_count = Counter()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    tweet = json.loads(line)
                    content = tweet.get('content', '')  # Obtener el contenido del tweet
                    for char in content:
                        if char in emoji.EMOJI_DATA:
                            emojis_count[char] += 1
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")

    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    # Obtener los top 10 emojis más usados
    top_emojis = emojis_count.most_common(10)
    return top_emojis
