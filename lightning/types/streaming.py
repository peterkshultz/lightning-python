from lightning.types.base import Base
from lightning.types.decorators import viztype
from lightning.types.utils import array_to_lines


@viztype
class LineStreaming(Base):

    _name = 'line-streaming'
    _func = 'linestreaming'

    @staticmethod
    def clean(series):

        data = array_to_lines(series)
        return {'data': data}


@viztype
class ScatterStreaming(Base):

    _name = 'scatter-streaming'
    _func = 'scatterstreaming'

    @staticmethod
    def clean(x, y, color=None, label=None, size=None):
        """
        Create a streaming scatter plot of x and y.

        Plotting once returns a visualization on which 'append' can be called to add new data
        in a streaming fashion. The opacity of old and new data is automatically set
        to highlight the most recent data and fade old data away.

        Parameters
        ----------
        x, y : array-like, each (n,)
            Input data

        color : array-like, optional, singleton or (n,3)
            Single rgb value or array to set colors

        label : array-like, optional, singleton or (n,)
            Single integer or array to set colors via groups

        size : array-like, optional, singleton or (n,)
            Single size or array to set point sizes
        """

        points = vecs_to_points(x, y)
        outdict = {'points': points}

        outdict = add_property(outdict, color, 'color')
        outdict = add_property(outdict, label, 'label')
        outdict = add_property(outdict, size, 'size')

        return outdict