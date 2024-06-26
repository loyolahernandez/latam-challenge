
import json
from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
from memory_profiler import profile

@profile
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    # leer los datos del archivo JSON
    tweets_data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    # Contar numeros de tweets por fecha y usuario
    date_user_count = defaultdict(Counter)
    for tweet in tweets_data:
        date = datetime.fromisoformat(tweet['date']).date()
        user = tweet['user']['username']
        date_user_count[date][user] += 1

    # Encontrar las 10 fechas con mas tweets
    top_dates = sorted(date_user_count.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Encontrar el usuario con mas publicaciones para cada una de las 10 fechas principales
    result = [(date, user_count.most_common(1)[0][0]) for date, user_count in top_dates]

    return result
