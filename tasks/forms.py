from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': "form-control mb-2"})

        self.fields['due_date'].widget = forms.DateInput(attrs={"type": "date", 'class': "form-control mb-2"})


class TaskFilterForm(forms.Form):
    STATUS_CHOISES = [
        ("", "Всі"),
        ("todo", "Потрібно зробити"),
        ("in_progress", "В процесі"),
        ("done", "Виконано"),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOISES, required=False, label="Статус")

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm,self).__init__(*args, **kwargs)
        self.fields["status"].widget.attrs.update({"class": "col-auto"})
