class DateDatabaseRouter:
    """
    Router para direcionar migrações do modelo Person ao banco `dados_db` e bloquear outros modelos.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app_optimus' and model.__name__ == 'Person':
            return 'dados_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app_optimus' and model.__name__ == 'Person':
            return 'dados_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == 'app_optimus' and obj1.__class__.__name__ == 'Person' or
            obj2._meta.app_label == 'app_optimus' and obj2.__class__.__name__ == 'Person'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Verifica o banco e o diretório de migrações
        if db == 'dados_db':
            return app_label == 'app_optimus' and model_name == 'person'
        return None



