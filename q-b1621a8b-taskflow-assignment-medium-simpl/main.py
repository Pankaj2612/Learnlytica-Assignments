class SimpleCache:
    def __init__(self):
        self._entries = {}
    def set(self, key, value, now, ttl):
        self._entries[key] = (value, now + ttl)
        return self
    def get(self, key, now):
        entry = self._entries.get(key)
        if entry is None:
            return None
        value, expires_at = entry
        if now >= expires_at:
            del self._entries[key]
            return None
        return value
    def get_or_set(self, key, loader, now, ttl):
        entry = self._entries.get(key)
        if entry is not None:
            value, expires_at = entry
            if now < expires_at:
                return value
            del self._entries[key]
        value = loader()
        self.set(key, value, now, ttl)
        return value
    def invalidate(self, key):
        self._entries.pop(key, None)
        return self