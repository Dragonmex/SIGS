class DatabaseRouter:
    def db_for_read(self, model, **hints):
        """Define qual banco usar para leitura"""
        if model._meta.app_label == 'conteudos':
            return 'conteudos'
        # Modelos de outras apps (como auth) usam o banco padrão
        return 'default'

    def db_for_write(self, model, **hints):
        """Define qual banco usar para escrita"""
        if model._meta.app_label == 'conteudos':
            return 'conteudos'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Permitir relações entre objetos de bancos diferentes"""
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Define onde aplicar migrações"""
        if app_label == 'conteudos':
            return db == 'conteudos'
        # Tudo que não é 'conteudos' vai para o banco padrão
        return db == 'default'
