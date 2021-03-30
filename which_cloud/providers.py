from enum import Enum


class Providers(Enum):
    PRIVATE = "private"
    LOCAL="local"
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    MICROSOFT = "microsoft"
