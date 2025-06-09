user_histories = {}

def add_message(user_id: int, role: str, content: str):
    history = user_histories.setdefault(user_id, [])
    history.append({"role": role, "content": content})
    if len(history) > 20:
        history.pop(0)

def get_history(user_id: int):
    return user_histories.get(user_id, [])
