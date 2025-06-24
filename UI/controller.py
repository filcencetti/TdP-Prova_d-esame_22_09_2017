import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDSeason(self):
        allSeasons = self._model.getAllSeasons()
        ddOptions = list(map(lambda x: ft.dropdown.Option(x), allSeasons))
        self._view._ddSeason.options = ddOptions

    def handleSelectedSeason(self, e):
        self._model.buildGraph(self._view._ddSeason.value)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente!!!"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model._graph.number_of_nodes()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model._graph.number_of_edges()}"))
        self._view.txt_result.controls.append(ft.Text(f"Gli archi con peso maggiore {self._model.max_sol} sono:"))
        for edge in self._model.max_edge:
            self._view.txt_result.controls.append(ft.Text(f"{self._model.getName(edge[0])} - {self._model.getName(edge[1])}"))
        self._view.update_page()
