from shared.mixins import BaseMixin


class ContactMixin(BaseMixin):
    """Mixin class to be inherited by `contact` app views."""
    page_name = 'contact_us'
