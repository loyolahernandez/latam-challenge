import json
from typing import List, Tuple
from collections import Counter
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_count = Counter()
    
    # Leer y procesar cada línea del archivo JSON para minimizar el uso de memoria
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                tweet = json.loads(line)
                mentions = re.findall(r'@\w+', tweet['content'])
                for mention in mentions:
                    mention_count[mention.strip('@')] += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    # Encontrar los 10 usuarios más mencionados
    top_mentions = mention_count.most_common(10)

    return top_mentions
