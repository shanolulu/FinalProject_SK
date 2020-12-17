from django import forms

class UploadImageForm(forms.Form):
    # title = forms.CharField(max_length=50)
    image = forms.ImageField()
    print(image)
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['subject', 'content']