import cProfile
import pstats
from typing import Callable
from memory_profiler import profile

def profile_time(func: Callable, *args, **kwargs):
    """
    Perfilar el tiempo de ejecución de una función.

    Parameters:
    - func (Callable): La función que se va a perfilar.
    - args, kwargs: Argumentos y palabras clave para pasar a la función.
    """
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()

    # Imprimir estadísticas de tiempo
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()
    
    return result


def profile_memory(func: Callable, *args, **kwargs):
    """
    Perfilar el uso de memoria de una función.

    Parameters:
    - func (Callable): La función que se va a perfilar.
    - args, kwargs: Argumentos y palabras clave para pasar a la función.
    """
    @profile
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper(*args, **kwargs)
