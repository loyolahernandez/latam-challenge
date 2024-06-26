from typing import List, Tuple
import json
from collections import defaultdict
import emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Inicializar un diccionario para contar los emojis
    emoji_count = defaultdict(int)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    tweet = json.loads(line)
                    content = tweet.get('content', '')  # Obtener el contenido del tweet
                    # Contar emojis en el contenido del tweet
                    for char in content:
                        if char in emoji.EMOJI_DATA:
                            emoji_count[char] += 1
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")

    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

    # Obtener los 10 emojis más usados
    top_emojis = sorted(emoji_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_emojis
