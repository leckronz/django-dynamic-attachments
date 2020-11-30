
class AttachmentsAdminMixin:

    # label, slug, content_type
    # relation_name specifies the name cooresponding with the genericRelation
    relation_name = 'attachments'
    
    def __init__():
        self.list_display.update('has_attachments')


class AttachmentsAdminFormMixin:

    # label, slug, content_type
    # relation_name specifies the name cooresponding with the genericRelation
    relation_name = 'attachments'

    def __init__():
        pass


