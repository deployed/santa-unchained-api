from typing import Dict

from rest_framework.serializers import Serializer


class ActionSerializerClassMixin:
    action_serializer_class: Dict[str, Serializer] = {}

    def get_serializer_class(self):
        if (
            self.action_serializer_class
            and self.action in self.action_serializer_class  # type: ignore
        ):
            return self.action_serializer_class[self.action]  # type: ignore
        return super().get_serializer_class()  # type: ignore
