class InvestmentRouter(object):
      def db_for_read(self, model, **hints):
          if model._meta.app_label == 'mse':
             return 'investments'
          return None

      def db_for_write(self, model, **hints):
          if model._meta.app_label == 'mse':
             return 'investments'
          return None
