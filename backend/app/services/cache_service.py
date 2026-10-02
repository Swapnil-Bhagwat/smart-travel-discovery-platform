"""
Lightweight In-Process Cache Service.
Step 9 - Performance & Caching.

Caches static or infrequently changing metadata (themes, destinations, operators, provider status)
in-memory with configurable Time-To-Live (TTL).
Does NOT cache dynamic user-specific search results.
"""

import time
import threading
from typing import Any, Callable, Dict, Optional, Tuple


class InMemoryCache:
    """
    Thread-safe, in-process key-value cache with TTL expiration.
    """

    def __init__(self, default_ttl_seconds: int = 300):
        self._cache: Dict[str, Tuple[Any, float]] = {}
        self._lock = threading.Lock()
        self._default_ttl = default_ttl_seconds

    def get(self, key: str) -> Optional[Any]:
        """Retrieve value by key if not expired and not in TESTING mode."""
        try:
            from flask import current_app
            if current_app and current_app.config.get('TESTING'):
                return None
        except Exception:
            pass

        with self._lock:
            if key not in self._cache:
                return None
            value, expiry = self._cache[key]
            if time.time() > expiry:
                del self._cache[key]
                return None
            return value

    def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> None:
        """Store value with TTL."""
        ttl = ttl_seconds if ttl_seconds is not None else self._default_ttl
        expiry = time.time() + ttl
        with self._lock:
            self._cache[key] = (value, expiry)

    def delete(self, key: str) -> None:
        """Remove key from cache."""
        with self._lock:
            self._cache.pop(key, None)

    def clear(self) -> None:
        """Clear all cached entries."""
        with self._lock:
            self._cache.clear()

    def get_or_set(self, key: str, fetcher: Callable[[], Any], ttl_seconds: Optional[int] = None) -> Any:
        """Retrieve value or compute and store it if missing/expired."""
        cached = self.get(key)
        if cached is not None:
            return cached
        val = fetcher()
        self.set(key, val, ttl_seconds=ttl_seconds)
        return val


# Global shared cache instance for application metadata
metadata_cache = InMemoryCache(default_ttl_seconds=300)
