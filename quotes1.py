def get_random_quote():
    return random.choice(QUOTES)

def save_history(quote, filename="history.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []
    history.append(quote)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def load_history(filename="history.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
