from django.forms import widgets
from django.utils.safestring import mark_safe


class BSSearchWidget(widgets.URLInput):

    def render(self, name, value, attrs=None, renderer=None):
        extra_attrs = self.build_attrs(self.attrs, attrs)
        super_output = super(BSSearchWidget, self).render(name, value,
                                                          extra_attrs)
        # No extra attributes were added this is just for a demo.
        return mark_safe(super_output)
