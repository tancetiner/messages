import hashlib


class Message:
    def __init__(self):
        self.db = {}

    def putMessage(self, message):
        messageHash = hashlib.sha256(message.encode("utf-8")).hexdigest()
        self.db[messageHash] = message
        return {"messageHash": messageHash}

    def getMessage(self, hash):
        if not hash in self.db.keys():
            return -1
        return {"message": self.db[hash]}
