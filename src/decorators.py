def deco(color: str):
    ansi_codes = {"red": "\033[91m", "green": "\033[92m", "end": "\033[0m"}
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{ansi_codes.get(color, '')}{result}{ansi_codes['end']}"
        return wrapper
    return decorator