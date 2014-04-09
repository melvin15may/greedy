from django.forms import ModelForm

from .models import Bookmark


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        exclude = ('date_created', 'date_updated', 'owner')

    def save(self, commit=True, owner=None):
        if not self.instance.pk:
            if not owner:
                raise TypeError("Owner is required to create a Bookmark.")
            self.instance.owner = owner
        return super(BookmarkForm, self).save(commit)