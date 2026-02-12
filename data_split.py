def train_test_split(data, test_size=0.2):
    split = int(len(data) * (1 - test_size))
    train = data[:split]
    test = data[split:]
    return train, test
