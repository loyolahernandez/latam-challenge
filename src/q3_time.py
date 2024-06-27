import json
from typing import List, Tuple
from collections import defaultdict, Counter
import re

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_count = Counter()
    
    # Leer y procesar cada línea del archivo JSON
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                tweet = json.loads(line)
                mentions = re.findall(r'@\w+', tweet['content'])
                mention_count.update(mentions)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    # Encontrar los 10 usuarios más mencionados
    top_mentions = mention_count.most_common(10)

    return [(mention.strip('@'), count) for mention, count in top_mentions]
