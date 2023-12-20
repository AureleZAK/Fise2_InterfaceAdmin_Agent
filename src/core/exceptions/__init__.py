"""
Ce module importe et expose des exceptions personnalisées pour la gestion des erreurs spécifiques.

Il importe les exceptions suivantes depuis le module `base` :
- `CustomException`: Classe de base pour les exceptions personnalisées.
- `BadRequestException`: Exception pour les requêtes incorrectes.
- `NotFoundException`: Exception pour les éléments non trouvés.
- `ForbiddenException`: Exception pour les autorisations refusées.
- `UnprocessableEntity`: Exception pour les entités non traitables.
- `DuplicateValueException`: Exception pour les valeurs en double.
- `UnauthorizedException`: Exception pour les autorisations non accordées.

"""
from .base import (
    CustomException,
    BadRequestException,
    NotFoundException,
    ForbiddenException,
    UnprocessableEntity,
    DuplicateValueException,
    UnauthorizedException,
)


__all__ = [
    "CustomException",
    "BadRequestException",
    "NotFoundException",
    "ForbiddenException",
    "UnprocessableEntity",
    "DuplicateValueException",
    "UnauthorizedException",
]
