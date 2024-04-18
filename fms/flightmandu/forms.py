from django import forms

class UserSignupForm(forms.Form):
    userFname = forms.CharField(label='First Name', max_length=100)
    userLname = forms.CharField(label='Last Name', max_length=100)
    userDob = forms.DateField(label='Date of Birth')
    userEmail = forms.EmailField(label='Email')
    userPhone = forms.CharField(label='Phone', max_length=20)
    userPassword = forms.CharField(label='Password', widget=forms.PasswordInput)
    userCpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('userPassword')
        confirm_password = cleaned_data.get('userCpassword')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data