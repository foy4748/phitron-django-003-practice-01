from django.shortcuts import render

from .forms import FormExample


def showForm(req):
    form = FormExample()
    return render(req, "practice_form_fields_project/formExample.html", {"form": form})
