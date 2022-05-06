from sklearn.datasets import load_iris
from  everywhereml.data.Dataset import Dataset


class IrisDataset:
    """
    Synctactic sugar to load the Iris dataset
    """
    def __init__(self):
        """
        Constructor
        """
        self.dataset = Dataset.from_sklearn(name='Iris', dataset=load_iris())

    def __getattr__(self, item):
        """
        Proxy to dataset
        :param item:
        :return:
        """
        return getattr(self.dataset, item)
