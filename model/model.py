import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._idMap = {}
        self.max_edge = []
        self.max_sol = 0

    def getAllSeasons(self):
        return DAO.getAllSeasons()

    def buildGraph(self,season):
        self._graph.clear()
        self.races = DAO.getAllRaces(int(season))
        self._graph.add_nodes_from(self.races)
        for race in self.races:
            self._idMap[race.raceId] = race

        allEdges = DAO.getAllEdges(season)
        for edge in allEdges:
            self._graph.add_edge(self._idMap[edge[0]], self._idMap[edge[1]],weight=edge[2])
            if edge[2] > self.max_sol:
                self.max_edge = [edge]
                self.max_sol = edge[2]
            elif edge[2] == self.max_sol:
                self.max_edge.append(edge)

    def getName(self,raceId):
        return self._idMap[raceId].name