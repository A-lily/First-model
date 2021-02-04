class RuleBasedModel:
    def __init__(self, train_data, test_data):
        """
        Initializes the classifier based on the given data.

        Parameters
        ----------
        train_data: list
            A list of dictionaries representing the train data where each item
            in the list is a dictionary describing a whole data entry.
        test_data: list
            A list of dictionaries representing the test data where each item
            in the list is a dictionary describing a whole data entry.
        """
        self.train_data = train_data
        self.test_data = test_data
        self.cols = self.train_data[0].keys()
        self.true_values = [entry["class"] for entry in self.test_data]


    def classify_sample_using_id(self, sample_id):
        """
        Classifies just one data point knowing its id.

        Parameters
        ----------
        data_point: dict
            A dictionary contains one datapoint to be classified.
        
        Returns
        -------
        int:
            An integer describing the class (either `1` or `2`).
        """
        data_point = self.test_data[sample_id]
        return self.classify_one(data_point)


    def classify_one(self, data_point):
        """
        Classifies just one data point into either class `1` or `2` based on
        some given features.

        Parameters
        ----------
        data_point: dict
            A dictionary contains one datapoint to be classified.
        
        Returns
        -------
        int:
            An integer describing the class (either `1` or `2`).
        """
        if data_point["f8"] > 0.24:
            return 1
        else:
            return 2


    def classify(self, test_data):
        """
        Classifies the whole test data.

        Parameters
        ----------
        test_data: list
            A list of dictionaries representing the test data where each item
            in the list is a dictionary describing a whole data entry.
        
        Returns
        -------
        list:
            A list of the predicted classes for the whole test data.
        """
        pred_values = []
        self.test_data = test_data
        self.true_values = [entry["class"] for entry in self.test_data]
        for test in self.test_data:
            pred_class = self.classify_one(test)
            pred_values.append(int(pred_class))
        return pred_values
    

    def calculate_accuracy(self, pred_values):
        """
        Calculate the accuracy of the whole test data.

        Parameters
        ----------
        pred_values: list
            A list of all predicted classes returned from the classifier.
        
        Returns
        -------
        acc: float
            A number representing the accuracy (max is 1.0)
        num_correct: int
            A number representing the total number of entries that was
            predicted correctly.
        total_samples: int
            The total number of entries we have.
        """
        num_correct = 0
        total_samples = len(self.true_values)
        for pred, gold in zip(pred_values, self.true_values):
            if int(pred) == int(gold):
                num_correct += 1
        acc = (num_correct / total_samples) * 100
        return acc, num_correct, total_samples

