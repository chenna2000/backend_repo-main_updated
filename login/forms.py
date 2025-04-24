from django import forms # type: ignore
from .models import AdmissionReview1, Answer, Contact, JobSeeker, Question, Subscriber1,Consultant,Forgot2,UniversityInCharge,Subscriber, UnregisteredColleges,Verify,Forgot,CompanyInCharge,new_user

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = new_user
        fields = [
            'firstname', 'lastname', 'email', 'country_code',
            'phonenumber', 'gender', 'password', 'confirm_password', 'agreed_to_terms'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if new_user.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")
        username_part = email.split('@')[0]
        if len(set(username_part.replace(" ", "").lower())) < 2:
            raise forms.ValidationError("Email must contain at least 2 unique characters before @.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        phone = cleaned_data.get("phonenumber")
        country_code = cleaned_data.get("country_code")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        if new_user.objects.filter(phonenumber=phone, country_code=country_code).exists():
            self.add_error('phonenumber', "Phone number already registered.")

        return cleaned_data


class CompanyInChargeForm(forms.ModelForm):
    class Meta:
        model = CompanyInCharge
        fields = ['company_name','official_email','country_code','mobile_number', 'designation', 'password', 'confirm_password', 'linkedin_profile','company_person_name','agreed_to_terms']


class UniversityInChargeForm(forms.ModelForm):
    class Meta:
        model = UniversityInCharge
        fields = ['university_name','official_email','country_code','mobile_number', 'designation', 'password', 'confirm_password', 'linkedin_profile','college_person_name','agreed_to_terms']


class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = ['consultant_name','official_email','country_code','mobile_number', 'designation', 'password', 'confirm_password', 'linkedin_profile','consultant_person_name','agreed_to_terms']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'})
}

class ForgotForm(forms.ModelForm):
    class Meta:
        model = Forgot
        fields = ['email']

class VerifyForm(forms.ModelForm):
    class Meta:
        model = Verify
        fields = ['otp']

class Forgot2Form(forms.ModelForm):
    class Meta:
        model = Forgot2
        fields = '__all__'

class SubscriptionForm1(forms.ModelForm):
    class Meta:
        model = Subscriber1
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'})

}

class JobSeekerRegistrationForm(forms.ModelForm):
   class Meta:
      model = JobSeeker
      fields = ['first_name', 'last_name', 'email', 'mobile_number', 'designation', 'password',  'confirm_password', 'linkedin_profile', 'country_code','agreed_to_terms']
      widgets = {
         'password': forms.PasswordInput(),
    }

def clean_email(self):
        email = self.cleaned_data.get('email')
        if JobSeeker.objects.filter(email=email).exists():
         raise forms.ValidationError("Email already in use.")
        return email

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'website', 'message']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
		
class Step1Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview1
        fields = [
            "college_name", "other_college_name", "course_name", "other_course_name",
            "student_name", "email", "country_code", "phone_number", "gender",
            "linkedin_profile", "course_fees", "year", "referral_code","apply",
            "anvil_reservation_benefits", "benefit", "gd_pi_admission", "class_size",
            "opted_hostel", "college_provides_placements", "hostel_fees", "average_package"
        ]

class Step2Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview1
        fields = ["admission_process", "course_curriculum_faculty"]

class Step3Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview1
        fields = ["fees_structure_scholarship"]

class Step4Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview1
        fields = ["liked_things", "disliked_things"]

class Step5Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview1
        fields = ["profile_photo", "campus_photos", "agree_terms"]
    
    # Handling file upload fields
    profile_photo = forms.FileField(required=False)
    campus_photos = forms.FileField(required=False)

class Step6Form(forms.ModelForm):
    class Meta:
        model = AdmissionReview1
        fields = ["certificate_id_card", "graduation_certificate"]

    certificate_id_card = forms.FileField(required=False)

class UnregisteredCollegesForm(forms.ModelForm):
    class Meta:
        model = UnregisteredColleges
        fields = ['university_name','official_email','country_code','mobile_number','password','linkedin_profile','college_person_name','agreed_to_terms']

