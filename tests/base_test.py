class BaseTest:
    prefix = 'AUTOMATION_'
    prefix_email = 'automation_'

    def get_prefix(self, field_name):
        return self.prefix + field_name

    def get_prefix_email(self, field_name):
        return self.prefix_email + field_name
