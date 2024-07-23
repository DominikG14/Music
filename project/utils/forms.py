class FormSetup():
    """Modifies standard django form look and functionality.
    Must be inherited FIRST."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = '' # removes colon ':' after every label name

    # adds empty placeholder value to every input (for styling purposes)
        for visible in self.visible_fields():
            visible.field.widget.attrs.update({'placeholder': ' '})