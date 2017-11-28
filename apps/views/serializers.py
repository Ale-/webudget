# django
from django.core.serializers.json import Serializer

class BlankSerializer(Serializer):
    def get_dump_object(self, obj):
        data = self._current
        data['pk'] = obj.pk
        pass
        return data
