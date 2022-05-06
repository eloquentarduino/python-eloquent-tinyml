from everywhereml.preprocessing import MinMaxScaler
from everywhereml.preprocessing import Pipeline


class IrisPipeline:
    """
    Synctactic sugar to pre-process the Iris dataset
    """
    def __init__(self):
        self.pipeline = Pipeline([
            MinMaxScaler()
        ], name='Iris')

    def __getattr__(self, item):
        """
        Proxy to pipeline
        :param item:
        :return:
        """
        return getattr(self.pipeline, item)
