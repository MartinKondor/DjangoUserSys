
def send_error(text: str, context: dict):
    return send_message(text, context, "danger")


def send_info(text: str, context: dict):
    return send_message(text, context, "info")


def send_success(text: str, context: dict):
    return send_message(text, context, "success")


def send_messages(texts: list, context: dict, type: str="warning"):
    return {
        **context,
        "messages": [
            {"text": text, "type": type}
        for text in texts]
    }


def send_message(text: str, context: dict, type: str="warning"):
    return {
        **context,
        "messages": [
            {"text": text, "type": type}
        ]
    }
