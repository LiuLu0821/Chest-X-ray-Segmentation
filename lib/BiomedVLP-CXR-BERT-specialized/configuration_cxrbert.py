
from typing import Any

from transformers import BertConfig, BertTokenizer


class CXRBertConfig(BertConfig):
    """
    Config class for CXR-BERT model.
    :param projection_size: Dimensionality of the joint latent space.
    """

    model_type = "cxr-bert"

    def __init__(self, projection_size: int = 128, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.projection_size = projection_size


class CXRBertTokenizer(BertTokenizer):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

