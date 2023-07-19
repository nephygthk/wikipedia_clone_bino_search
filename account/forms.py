from django import forms

from .models import Profile


class DateInput(forms.DateInput):
	input_type = 'date'

class AddProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date_of_birth'].widget = DateInput()
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control mb-3'})

    def clean_name(self):
        name = self.cleaned_data['name']
        if Profile.objects.filter(name=name).exists():
            raise forms.ValidationError(
                'A profile with this name already exist, please try another name or delete or add a letter to it to differentiate it')
        return name