from django import forms


class FormExample(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    email = forms.EmailField(help_text="Please, enter a valid email")
    agree = forms.BooleanField(label="Agree with your terms and conditions")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )
    FAVORITE_COLORS_CHOICES = [
        ("blue", "Blue"),
        ("green", "Green"),
        ("black", "Black"),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    second_favorite_color = forms.ChoiceField(
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES
    )
    more_favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    multiple_select_favorite_colors = forms.MultipleChoiceField(
        choices=FAVORITE_COLORS_CHOICES, widget=forms.CheckboxSelectMultiple()
    )
