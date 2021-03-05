from shared.mixins import BaseMixin


class PolicyMixin(BaseMixin):
    """Mixin class to be inherited by `policy` app views."""
    page_name = 'policy'
