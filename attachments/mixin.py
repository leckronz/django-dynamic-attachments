from django.conf import settings
from django import forms
from django.utils.html import format_html_join


class AttachmentsAdminMixin:

    # label, slug, content_type
    # relation_name specifies the name corresponding with the genericRelation
    relation_name = 'attachments'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_display += ('has_attachments',)

    def has_attachments(self, object):
        return getattr(object, self.relation_name).exists()

    def list_attachments(self, instance):
        return format_html_join(
            '', "<a href={}{}>{}</a><br>",
            ((settings.BASE_URL, att.get_absolute_url(), att.file_name) for att in instance.attachments.all())
        )

    def get_readonly_fields(self, request, obj=None):
        return super().get_readonly_fields(request, obj=obj) + ('list_attachments',)






