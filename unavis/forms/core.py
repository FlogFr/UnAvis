from django import forms

from unavis import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('title', 'description', 'parent', )
        widgets = {
            'description': forms.Textarea(),
        }

    def save(self, request):
        return models.Category.objects.create(
            created_by=request.user,
            updated_by=request.user,
            **self.cleaned_data
        )
