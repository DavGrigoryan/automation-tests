class BaseTest:
    prefix = 'AUTOMATION_TEST: '

    def get_prefix(self, field_name):
        return self.prefix + field_name
