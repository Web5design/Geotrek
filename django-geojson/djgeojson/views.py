from http import HttpJSONResponse
from serializers import Serializer as GeoJSONSerializer
from django.views.generic import ListView


class GeoJSONResponseMixin(object):
    """
    A mixin that can be used to render a GeoJSON response.
    """
    response_class = HttpJSONResponse
    fields = []

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        serializer = GeoJSONSerializer()
        response = self.response_class(**response_kwargs)
        serializer.serialize(self.queryset, stream=response, fields=self.fields, ensure_ascii=False)
        return response


class GeoJSONLayerView(GeoJSONResponseMixin, ListView):
    """
    A generic view to serve a model as a layer.
    """