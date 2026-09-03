class classifier:

    def __init__(self, threshold):
        self.threshold = threshold
        self.is_trained = False

    def train(self, X, y):

        print ("Model Training Completed")
        self.is_trained = True

    def predict(self, X):

        if not self.is_trained:
            raise Exception("Please train the model first")

        predictions = [1 if x > self.threshold else 0 for x in X]
        return predictions




model = classifier(threshold=50)


model.train([10, 50, 120, 200], [0, 0, 1, 1])

results = model.predict([30, 150, 80, 200])

print("Predictions: ", results)