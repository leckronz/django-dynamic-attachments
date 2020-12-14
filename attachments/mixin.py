from django import forms
class AttachmentsAdminMixin:

    # label, slug, content_type
    # relation_name specifies the name cooresponding with the genericRelation
    relation_name = 'attachments'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_display += ('has_attachments',)

    def has_attachments(self, object):
        return getattr(object, self.relation_name).exists()



class AttachmentsAdminFormMixin:

    # label, slug, content_type
    # relation_name specifies the name cooresponding with the genericRelation
    relation_name = 'attachments'
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['list_attachments'] = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'readonly': True}))
        





