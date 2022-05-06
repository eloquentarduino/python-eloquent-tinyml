from everywhereml.sklearn.ensemble import RandomForestClassifier


class IrisRandomForestClassifier:
    """
    Synctactic sugar to fit a RandomForestClassifier on the Iris dataset
    """
    def __init__(self):
        """
        Constructor
        """
        self.clf = RandomForestClassifier(n_estimators=10, max_leaf_nodes=20)

    def __getattr__(self, item):
        """
        Proxy to classifier
        :param item:
        :return:
        """
        return getattr(self.clf, item)
