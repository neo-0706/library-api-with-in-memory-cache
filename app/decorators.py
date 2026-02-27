from functools import wraps
from app.cache import search_cache
from typing import Callable , Any

def cached(func: Callable) -> callable:
    @wraps(func)
    async def wrapper(q: str , limit : int , *args , **kwargs):
        cached_result =search_cache.get(q , limit)

        if cached_result is not None :
            return cached_result
        
        result = await func(q , limit , *args , **kwargs)

        search_cache.set(q , limit , result)

        return result
    
    return wrapper