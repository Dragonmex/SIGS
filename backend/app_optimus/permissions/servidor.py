from rest_framework.permissions import BasePermission

class IsServidor(BasePermission):
    """
    Permissão personalizada que permite acesso apenas a servidores.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil == 'servidor'
