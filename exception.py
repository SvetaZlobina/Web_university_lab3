class HandlerException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        print(self.value)
