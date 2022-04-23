from django.forms import ModelForm
from .models import emp


class empform(ModelForm):
	class Meta:
		model = emp
		fields = '__all__'