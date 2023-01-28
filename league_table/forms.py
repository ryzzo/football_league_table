from django import forms
from .models import MatchStat

class MatchStatForm(forms.ModelForm):
    class Meta:
        model = MatchStat
        fields = ['home_team', 'away_team', 'home_goals', 'away_goals']