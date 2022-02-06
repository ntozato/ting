class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        data_len = len(self.data)

        if (index < 0) or (index > data_len):
            raise IndexError

        return self.data[index]
