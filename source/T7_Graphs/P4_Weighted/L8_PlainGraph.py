from random import Random

from source.T7_Graphs.P4_Weighted.L2_GraphForAlgorithms import GraphForAlgorithms
from source.T7_Graphs.P4_Weighted.L7_VertexWithHeuristic import VertexWithHeuristic
from source.T7_Graphs.P4_Weighted.L3_BelmanFord import BelmanFord
from source.T7_Graphs.P4_Weighted.L6_Dijkstra import Dijkstra


class PlainGraph(GraphForAlgorithms):
    """ Граф, вершини якого містять геометричні координати,
        а вага ребер - відстані між ними

        Використовується для тестування алгоритму А*
        """

    def addEdge(self, source, destination, weight=1):
        """ Додавання ребра з кінцями в точках source та destination
        з вагою, що дорівнює геометричній відстані між цими вершинами

        :param source: Перша вершина
        :param destination: Друга вершина
        :param weight: Вага ребра - формальний параметер, що необхідний лише для наслідування
        :return: None
        """

        weight = self.distance(source, destination)
        super().addEdge(source, destination, weight)

    def addVertex(self, vertex) -> bool:
        """ Додає вершину у граф, якщо така вершина не міститься у ньому

        :param vertex: ключ (тобто ім'я) нової вершини
        :return: True, якщо вершина успішно додана
        """

        if vertex in self:  # Якщо вершина міститься у графі, її вже не треба додавати
            return False

        newVertex = VertexWithHeuristic(vertex)  # створюємо нову вершину з іменем key
        self.mVertices[vertex] = newVertex  # додаємо цю вершину до списку вершин графу
        self.mVertexNumber += 1          # Збільшуємо лічильник вершин у графі
        return True

    def distance(self, source, destination):
        """ Визначає геометричну відстань (по прямій лінії) між двома вершинами source та destination у графі

        :param source: Перша вершина
        :param destination: Друга вершина
        :return: Геометрична відстань між вершинами source та destination
        """
        source_position = self.getData(source)
        destination_position = self.getData(destination)
        assert source_position is not None and destination_position is not None

        return (((destination_position[0] - source_position[0]) ** 2) + ((destination_position[1] - source_position[1]) ** 2)) ** 0.5


def inputGraphWithRandomVertexPositions(graph, vertices, edges):
    """ Ініціалізація графу випадковим чином.

    Заповнює граф вершинами з випадковими позиціями та ребрами з випадковою вагою

    :param graph: Порожній граф
    :param vertices: Кількість вершин
    :param edges: Кількість ребер
    :return: None
    """

    for v in range(vertices + 1):
        graph.addVertex(v)

        rnd = Random()
        x = rnd.randint(-10, 10)
        y = rnd.randint(-10, 10)
        pos = (x, y)
        graph.setData(v, pos)

    for e in range(edges):
        rnd = Random()
        frm = rnd.randint(0, vertices)
        to = rnd.randint(0, vertices)
        if frm != to:
            graph.addEdge(frm, to)


if __name__ == "__main__":
    g = PlainGraph(False)

    points = 10
    edges = 30
    inputGraphWithRandomVertexPositions(g, points, edges)

    # To compare results.
    Dijkstra(g, 0, points)
    BelmanFord(g, 0, points)

    print(g)

