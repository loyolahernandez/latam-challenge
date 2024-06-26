import json
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
from memory_profiler import profile

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Leer y procesar cada línea del archivo JSON por separado para minimizar el uso de memoria
    date_user_count = defaultdict(lambda: defaultdict(int))
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                tweet = json.loads(line)
                date = datetime.fromisoformat(tweet['date']).date()
                user = tweet['user']['username']
                date_user_count[date][user] += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    # Encontrar las 10 fechas con más tweets
    top_dates = sorted(date_user_count.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Encontrar el usuario con más publicaciones para cada una de las 10 fechas principales
    result = [(date, max(user_count, key=user_count.get)) for date, user_count in top_dates]

    return result
