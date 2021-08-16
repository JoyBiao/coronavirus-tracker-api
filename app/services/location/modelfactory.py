from ...models import *
class ModelFactory():
    def create_model(self, type, data):
        """Factory Method"""
        models = {
            "timeline": Timeline(timeline = data),
            "latest": Latest(confirmed = data.confirmed, deaths = data.deaths, recovered = data.recovered),
            "timelines": Timelines(confirmed = data.confirmed, deaths = data.deaths, recovered = data.recovered),
            "location": Location(data)
        }
 
        return models[type]
