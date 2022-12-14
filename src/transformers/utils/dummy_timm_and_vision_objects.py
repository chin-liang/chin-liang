# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa
from ..utils import DummyObject, requires_backends


DEFORMABLE_DETR_PRETRAINED_MODEL_ARCHIVE_LIST = None


class DeformableDetrForObjectDetection(metaclass=DummyObject):
    _backends = ["timm", "vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["timm", "vision"])


class DeformableDetrModel(metaclass=DummyObject):
    _backends = ["timm", "vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["timm", "vision"])


class DeformableDetrPreTrainedModel(metaclass=DummyObject):
    _backends = ["timm", "vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["timm", "vision"])


DETR_PRETRAINED_MODEL_ARCHIVE_LIST = None


class DetrForObjectDetection(metaclass=DummyObject):
    _backends = ["timm", "vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["timm", "vision"])


class DetrForSegmentation(metaclass=DummyObject):
    _backends = ["timm", "vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["timm", "vision"])


class DetrModel(metaclass=DummyObject):
    _backends = ["timm", "vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["timm", "vision"])


class DetrPreTrainedModel(metaclass=DummyObject):
    _backends = ["timm", "vision"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["timm", "vision"])
