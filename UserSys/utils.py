import json


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


class JsonSerializable:
    
    def to_dict(self):
        obj = {}
        fields = [f.name for f in self.__class__._meta.get_fields()]
        for field in fields:
            if hasattr(self, field):
                obj[field] = str(getattr(self, field))
        return obj

    def to_json(self, indent=4):
        return json.dumps(self.to_dict(), indent=indent)
