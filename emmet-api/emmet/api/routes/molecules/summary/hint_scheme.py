from maggma.api.resource import HintScheme


class SummaryHintScheme(HintScheme):
    """
    Hint scheme for the molecules/summary endpoint.
    """

    def generate_hints(self, query):

        for param in query["criteria"]:

            if "composition" in param:
                return {"hint": {"composition.$**": 1}}
            elif "nelements" in param:
                return {"hint": {"nelements": 1}}
            elif "has_props" in param:
                return {"hint": {"has_props": 1}}

        return {"hint": {}}
