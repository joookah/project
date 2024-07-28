Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.graphics import RoundedRectangle, Color, Rectangle, InstructionGroup
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import sp
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.uix.filechooser import FileChooserListView
import os
import subprocess
import fitz  # PyMuPDF
from plyer import filechooser
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from plyer import filechooser, notification
import os
import platform
from kivy.clock import Clock
from kivy.core.window import Window
from plyer import filechooser
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout


kivy.require('2.0.0')

# Setting the window background color to light purple
Window.clearcolor = (0.9, 0.9, 1, 1)  # Light purple background

class CreateProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(CreateProfileScreen, self).__init__(**kwargs)

        # Define RGB values for the gradient start and end colors
        r_start, g_start, b_start = 254, 89, 61  # RGB for start color (orange)
        r_end, g_end, b_end = 255, 112, 68  # RGB for end color (light orange)

        # Normalize RGB values
        norm_r_start = r_start / 255.0
        norm_g_start = g_start / 255.0
        norm_b_start = b_start / 255.0

        norm_r_end = r_end / 255.0
        norm_g_end = g_end / 255.0
        norm_b_end = b_end / 255.0

        # Main layout with vertical orientation
        layout = BoxLayout(orientation='vertical', padding=(40, 20), spacing=20)

        # Add gradient background
        with layout.canvas.before:
            Color(norm_r_start, norm_g_start, norm_b_start, 1)  # Start color
            self.gradient_rect = Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=self.update_gradient_rect, size=self.update_gradient_rect)

        # Add title with icon
        header_layout = BoxLayout(orientation='horizontal', spacing=5, size_hint_y=None, height=dp(60))

        # Add icon
        icon = Image(source='C:/Users/user/PycharmProjects/Sekao APP/iconyes.png', size_hint_x=None, width=dp(40))
        header_layout.add_widget(icon)

        # Add title label
        title_label = Label(text="Create Your Profile", font_size=sp(36), color=(0, 0, 0, 1), bold=True)
        header_layout.add_widget(title_label)

        layout.add_widget(header_layout)

        # Form layout with grid orientation
        form_layout = GridLayout(cols=2, padding=(20, 10), spacing=(20, 20), size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))

        # Full Name
        full_name_label = Label(text="Full Name:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(full_name_label)
        self.full_name = TextInput(font_size=sp(24), background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                                   size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.full_name)


        # Email
        email_label = Label(text="Email:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(email_label)
        self.email = TextInput(font_size=sp(24), background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                               size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.email)

        # Password
        password_label = Label(text="Password:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(password_label)
        self.password = TextInput(font_size=sp(24), password=True, background_normal='',
                                  background_color=(0.9, 0.9, 0.9, 1),
                                  size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.password)

        # Confirm Password
        confirm_password_label = Label(text="Confirm Password:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(confirm_password_label)
        self.confirm_password = TextInput(font_size=sp(24), password=True, background_normal='',
                                          background_color=(0.9, 0.9, 0.9, 1),
                                          size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.confirm_password)

        # Date of Birth
        dob_label = Label(text="Date of Birth:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(dob_label)
        self.dob = TextInput(font_size=sp(24), background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                             size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.dob)

        # Grade/Year Level
        grade_label = Label(text="Grade/Year Level:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(grade_label)
        self.grade = TextInput(font_size=sp(24), background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                               size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.grade)

        # Interests
        interests_label = Label(text="Interests:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(interests_label)
        self.interests = TextInput(font_size=sp(24), background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                                   size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.interests)

        # Goals
        goals_label = Label(text="Goals:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(goals_label)
        self.goals = TextInput(font_size=sp(24), background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                               size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.goals)

        # School/Institution
        school_label = Label(text="School/Institution:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(school_label)
        self.school = TextInput(font_size=sp(24), background_normal='', background_color=(0.9, 0.9, 0.9, 1),
                                size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.school)

        # Junior/Senior Selector
        selector_label = Label(text="School Level:", font_size=sp(24), color=(0, 0, 0, 1))
        form_layout.add_widget(selector_label)

        self.school_level = Spinner(text='Junior', values=('Junior', 'Senior'), font_size=sp(24),
                                    background_color=(0, 0, 0, 1), size_hint_y=None, height=dp(60))
        form_layout.add_widget(self.school_level)



        # Create and Cancel buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(80), padding=(40, 20),
                                  spacing=20)
        submit_button = Button(text="Submit", on_press=self.submit_profile, font_size=sp(24),
                               size_hint_x=None, width=dp(200), background_normal='', background_color=(0, 0, 0, 1))
        button_layout.add_widget(submit_button)
        cancel_button = Button(text="Cancel", on_press=self.cancel_profile, font_size=sp(24),
                               size_hint_x=None, width=dp(200), background_normal='', background_color=(0, 0, 0, 1))
        button_layout.add_widget(cancel_button)

        # Scroll view for the form layout
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - dp(200)),
                                 bar_color=(0, 0, 0, 1), bar_width=dp(10))
        scroll_view.add_widget(form_layout)

        layout.add_widget(scroll_view)
        layout.add_widget(button_layout)
        self.add_widget(layout)

    def update_gradient_rect(self, instance, value):
        self.gradient_rect.pos = instance.pos
        self.gradient_rect.size = instance.size

    def submit_profile(self, instance):
        if self.password.text != self.confirm_password.text:
            popup = Popup(title='Error', content=Label(text='Passwords do not match!'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            # Pass the name to the ProfileScreen
            App.get_running_app().root.get_screen('profile_screen').update_name(self.full_name.text)
            App.get_running_app().root.current = 'payment'

    def cancel_profile(self, instance):
        # Clear all fields or handle cancellation
        self.full_name.text = ''
        self.username.text = ''
        self.email.text = ''
        self.password.text = ''
        self.confirm_password.text = ''
        self.dob.text = ''
        self.grade.text = ''
        self.interests.text = ''
        self.goals.text = ''
        self.school.text = ''
        App.get_running_app().root.current = 'home'

    def go_home(self, instance):
        App.get_running_app().root.current = 'home'


class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = 0, 0, 0, 1 # Black background
        self.background = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_background_size, pos=self.update_background_pos)

        self.text_color = Color(1, 1, 1, 1)  # White text

    def update_background_size(self, instance, value):
        self.background.size = value

    def update_background_pos(self, instance, value):
        self.background.pos = value





class BackgroundImageWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(BackgroundImageWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        with self.canvas.before:
            Color(1, 1, 1, 1)  # White color
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg_rect, size=self.update_bg_rect)

        self.image = Image(source='C:/Users/user/PycharmProjects/Sekao APP/home2.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.image)

    def update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        # Define RGB values for the gradient start and end colors
        r_start, g_start, b_start = 254, 89, 61  # RGB for start color (orange)
        r_end, g_end, b_end = 255, 112, 68  # RGB for end color (light orange)

        # Normalize RGB values
        norm_r_start = r_start / 255.0
        norm_g_start = g_start / 255.0
        norm_b_start = b_start / 255.0
        norm_r_end = r_end / 255.0
        norm_g_end = g_end / 255.0
        norm_b_end = b_end / 255.0

        # Create the main layout with vertical orientation
        layout = BoxLayout(orientation='vertical')

        # Add gradient background
        with layout.canvas.before:
            Color(norm_r_start, norm_g_start, norm_b_start, 1)  # Start color
            self.gradient_rect = Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=self.update_gradient_rect, size=self.update_gradient_rect)

        # Header with logo and welcome message
        header_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(160), padding=dp(20))

        # Add logo image (adjusted size)
        logo_image = Image(source='C:/Users/user/Downloads/logo2.jpeg', size_hint_y=None, height=dp(120))
        header_layout.add_widget(logo_image)

        # Add welcome message
        welcome_label = Label(text="Welcome to Your Educational App!", font_size='24sp', color=(0, 0, 0, 1),
                              size_hint_y=None, height=dp(40))
        header_layout.add_widget(welcome_label)

        layout.add_widget(header_layout)

        # Background image widget
        bg_image_widget = BackgroundImageWidget(size_hint_y=None, height=dp(200))
        layout.add_widget(bg_image_widget)

        # List of services
        services = [
            "Have access to educational content",
            "Try in-app exercises",
            "Track your progress",
            "All for P150 per month"
        ]

        services_layout = BoxLayout(orientation='vertical', padding=(20, 10), spacing=dp(10))
        for service in services:
            service_label = Label(text=service, font_size='18sp', color=(0, 0, 0, 1))
            services_layout.add_widget(service_label)

        layout.add_widget(services_layout)

        # Container for buttons
        button_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))

        # Add Create Profile button (centered, black background, white text)
        profile_button = RoundedButton(text="Create Profile", size_hint=(None, None), width=dp(200), height=dp(50),
                                       on_press=self.create_profile)
        button_layout.add_widget(profile_button)

        # Add Key Services button (centered, black background, white text)
        services_button = RoundedButton(text="Key Services", size_hint=(None, None), width=dp(200), height=dp(50),
                                        on_press=self.key_services)
        button_layout.add_widget(services_button)

        # Add spacer to push buttons to the bottom
        button_layout.add_widget(Label(size_hint_y=None, height=dp(20)))  # Adjusted spacer height

        layout.add_widget(button_layout)

        self.add_widget(layout)

    def update_gradient_rect(self, instance, value):
        self.gradient_rect.pos = instance.pos
        self.gradient_rect.size = instance.size

    def create_profile(self, instance):
        self.manager.current = 'create_profile'

    def key_services(self, instance):
        # Create a BoxLayout to hold the services labels
        services_layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))
        services = [
            "Have access to educational content",
            "Try in-app exercises",
            "Track your progress",
            "All for P150 per month"
        ]
        for service in services:
            service_label = Label(text=service, font_size='18sp', color=(0, 0, 0, 1))
            services_layout.add_widget(service_label)

        # Create a Popup to display the services
        popup = Popup(
            title='Key Services',
            content=services_layout,
            size_hint=(None, None),
            size=(400, 400)
        )
        popup.open()

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

        # Define RGB values for the gradient start and end colors
        r_start, g_start, b_start = 254, 89, 61  # RGB for start color (orange)
        r_end, g_end, b_end = 255, 112, 68  # RGB for end color (light orange)

        # Normalize RGB values
        norm_r_start = r_start / 255.0
        norm_g_start = g_start / 255.0
        norm_b_start = b_start / 255.0

        norm_r_end = r_end / 255.0
        norm_g_end = g_end / 255.0
        norm_b_end = b_end / 255.0

        # Main layout with vertical orientation
        layout = BoxLayout(orientation='vertical', padding=(40, 20), spacing=20)

        # Add gradient background
        with layout.canvas.before:
            Color(norm_r_start, norm_g_start, norm_b_start, 1)  # Start color
            self.gradient_rect = Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=self.update_gradient_rect, size=self.update_gradient_rect)

        # Add title
        title_label = Label(text="Profile", font_size=sp(36), color=(0, 0, 0, 1), bold=True)
        layout.add_widget(title_label)

        # Add icon in the middle
        icon = Image(source='C:/Users/user/PycharmProjects/Sekao APP/iconyes.png', size_hint=(None, None), size=(dp(100), dp(100)))
        layout.add_widget(icon)

        # Add name label
        self.name_label = Label(text="", font_size=sp(24), color=(0, 0, 0, 1))
        layout.add_widget(self.name_label)

        # Add other widgets
        self.set_target_button = Button(text="Set Study Targets", font_size=sp(24), background_normal='', background_color=(0, 0, 0, 1))
        layout.add_widget(self.set_target_button)

        self.generate_timetable_button = Button(text="Generate Study Timetable", font_size=sp(24), background_normal='', background_color=(0, 0, 0, 1))
        layout.add_widget(self.generate_timetable_button)

        self.set_reminders_button = Button(text="Set Reminders", font_size=sp(24), background_normal='', background_color=(0, 0, 0, 1))
        layout.add_widget(self.set_reminders_button)

        self.notes_button = Button(text="Go to Notes", on_press = self.go_to_notes, font_size=sp(24), background_normal='', background_color=(0, 0, 0, 1))
        layout.add_widget(self.notes_button)

        self.add_widget(layout)

    def update_name(self, name):
        self.name_label.text = f"Welcome, {name}!"

    def update_gradient_rect(self, instance, value):
        self.gradient_rect.pos = instance.pos
        self.gradient_rect.size = instance.size


    def go_to_notes(self, instance):
        # Navigate to Notes Screen
        App.get_running_app().root.current = 'note_screen'





class CreditCardInput(TextInput):
    def __init__(self, **kwargs):
        super(CreditCardInput, self).__init__(**kwargs)
        self.bind(text=self.on_text)
        self.max_length = 19  # 16 digits + 3 dashes

    def on_text(self, instance, value):
        Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        # Remove non-numeric characters
        cleaned_value = ''.join(filter(str.isdigit, self.text))
        # Limit to 16 digits
        if len(cleaned_value) > 16:
            cleaned_value = cleaned_value[:16]
        # Format into groups of 4 digits separated by dashes
        formatted_value = '-'.join([cleaned_value[i:i+4] for i in range(0, len(cleaned_value), 4)])
        # Set formatted text back to TextInput
        self.text = formatted_value
        # Place cursor at the end of the text
        self.cursor = (len(formatted_value), 0)

class ExpiryDateInput(TextInput):
    def __init__(self, **kwargs):
        super(ExpiryDateInput, self).__init__(**kwargs)
        self.bind(text=self.on_text)
        self.max_length = 5  # 4 digits + 1 slash

    def on_text(self, instance, value):
        Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        # Remove non-numeric characters
        cleaned_value = ''.join(filter(str.isdigit, self.text))
        # Limit to 4 digits
        if len(cleaned_value) > 4:
            cleaned_value = cleaned_value[:4]
        # Format as MM/YY
        formatted_value = cleaned_value[:2] + ('/' + cleaned_value[2:] if len(cleaned_value) > 2 else '')
        # Set formatted text back to TextInput
        self.text = formatted_value
        # Place cursor at the end of the text
        self.cursor = (len(formatted_value), 0)

class CVVInput(TextInput):
    def __init__(self, **kwargs):
        super(CVVInput, self).__init__(**kwargs)
        self.bind(text=self.on_text)
        self.max_length = 3  # 3 digits

    def on_text(self, instance, value):
        Clock.schedule_once(self.update_text)

    def update_text(self, dt):
        # Remove non-numeric characters
        cleaned_value = ''.join(filter(str.isdigit, self.text))
        # Limit to 3 digits
        if len(cleaned_value) > 3:
            cleaned_value = cleaned_value[:3]
        # Set text back to TextInput
        self.text = cleaned_value
        # Place cursor at the end of the text
        self.cursor = (len(cleaned_value), 0)


class PaymentScreen(Screen):
    def __init__(self, **kwargs):
        super(PaymentScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))

        with self.canvas.before:
            Color(254/255, 89/255, 61/255, 1)  # Start color (orange)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)

        # Create a layout for the back button and title
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))
        back_button = Button(size_hint=(None, None), size=(dp(80), dp(80)),
                             background_normal='C:/Users/user/PycharmProjects/Sekao APP/BACK2.png',  # Your back icon path
                             background_down='C:/Users/user/PycharmProjects/Sekao APP/back_icon.png')  # Optional: Different image when pressed
        back_button.bind(on_press=self.go_back)
        top_layout.add_widget(back_button)

        title_label = Label(text="Payment Information", font_size=sp(36), color=(0, 0, 0, 1), bold=True)
        top_layout.add_widget(title_label)

        layout.add_widget(top_layout)

        # Credit Card Number
        cc_layout = BoxLayout(orientation='horizontal', spacing=dp(10))
        cc_label = Label(text="Credit Card Number:", font_size=sp(24), color=(0, 0, 0, 1))
        cc_layout.add_widget(cc_label)
        visa_icon = Image(source='C:/Users/user/PycharmProjects/Sekao APP/visa.png', size_hint=(None, None), size=(dp(40), dp(40)))
        cc_layout.add_widget(visa_icon)
        self.credit_card = CreditCardInput(font_size=sp(24), multiline=False, background_normal='',
                                           background_color=(0.9, 0.9, 0.9, 1), hint_text='0000-0000-0000-0000')
        cc_layout.add_widget(self.credit_card)
        layout.add_widget(cc_layout)

        # Expiry Date
        expiry_label = Label(text="Expiry Date (MM/YY):", font_size=sp(24), color=(0, 0, 0, 1))
        layout.add_widget(expiry_label)
        self.expiry_date = ExpiryDateInput(font_size=sp(24), multiline=False, background_normal='',
                                           background_color=(0.9, 0.9, 0.9, 1), hint_text='MM/YY')
        layout.add_widget(self.expiry_date)

        # CVV
        cvv_label = Label(text="CVV:", font_size=sp(24), color=(0, 0, 0, 1))
        layout.add_widget(cvv_label)
        self.cvv = CVVInput(font_size=sp(24), multiline=False, password=True, background_normal='',
                            background_color=(0.9, 0.9, 0.9, 1), hint_text='123')
        layout.add_widget(self.cvv)

        # Payment Button
        payment_button = Button(text="Make Payment", size_hint=(None, None), size=(dp(200), dp(60)),
                                font_size=sp(24), background_color=(0, 0, 0, 1), color=(1, 1, 1, 1))
        payment_button.bind(on_press=self.make_payment)
        layout.add_widget(payment_button)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_back(self, instance):
        self.manager.current = 'create_profile'  # Replace with the actual screen name to navigate back

    def make_payment(self, instance):
        # Implement payment processing logic here
        # For demonstration purposes, assume payment is successful
        payment_successful = True  # Replace with actual payment processing logic

        if payment_successful:
            # Optionally, show a popup indicating payment success
            popup = Popup(title='Payment Status', content=Label(text='Payment Successful!'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()

            # Navigate to the NoteScreen after successful payment
            self.manager.current = 'profile_screen'  # Replace 'profile_screen' with the name of your ProfileScreen

        else:
            # Handle payment failure if needed
            popup = Popup(title='Payment Status', content=Label(text='Payment Failed. Please try again.'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()



class NoteScreen(Screen):
    def __init__(self, **kwargs):
        super(NoteScreen, self).__init__(**kwargs)

        # Main layout
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))

        # Add the background color gradient
        with self.canvas.before:
            Color(254 / 255, 89 / 255, 61 / 255, 1)  # Start color (orange)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Add a banner image
        banner_image = Image(
            source='C:/Users/user/PycharmProjects/Sekao APP/subject2.jpg',  # Update path as needed
            size_hint_y=None,
            height=dp(200),
            allow_stretch=True,
            keep_ratio=False
        )
        layout.add_widget(banner_image)

        # Title label
        title_label = Label(
            text="Subjects",
            font_size=sp(36),
            color=(0, 0, 0, 1),
            bold=True
        )
        layout.add_widget(title_label)

        # ScrollView for subjects
        scroll_view = ScrollView(size_hint=(1, 1))
        button_layout = BoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=None)
        button_layout.bind(minimum_height=button_layout.setter('height'))

        # Subjects buttons
        subjects = ['Biology', 'Chemistry', 'Physics', 'Mathematics', 'English', 'Computer-Studies', 'Accounting']
        for subject in subjects:
            subject_button = Button(
                text=subject,
                size_hint_y=None,
                height=dp(60),
                background_color=(0, 0, 0, 1),
                color=(1, 1, 1, 1),
                bold=True,
                font_size=sp(18)
            )
            subject_button.bind(on_release=self.on_subject_button_press)
            button_layout.add_widget(subject_button)

        scroll_view.add_widget(button_layout)
        layout.add_widget(scroll_view)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_subject_button_press(self, instance):
        subject_name = instance.text.lower().replace(' ', '-')  # Format subject names to match screen names
        if subject_name == 'computer-studies':
            screen_name = 'computer_screen'  # Match the name used in ScreenManager
        else:
            screen_name = f'{subject_name}_screen'

        if screen_name in self.manager.screen_names:
            self.manager.current = screen_name
        else:
            print(f"Screen name '{screen_name}' not found in screen manager")


class JuniorSchoolScreen(Screen):
    def __init__(self, **kwargs):
        super(JuniorSchoolScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Background image at the top
        background_image = Image(source='home3.jpeg', size_hint=(1, None), height=dp(200))
        layout.add_widget(background_image)

        # Container for the rest of the widgets
        container = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(1, 0.7))

        with container.canvas.before:
            Color(0.8, 0.8, 0.8, 1)  # Light grey background color for the container
            self.rect = Rectangle(size=container.size, pos=container.pos)
        container.bind(size=self.update_rect, pos=self.update_rect)

        title_label = Label(text="Junior School Subjects", font_size='24sp', color=(0.2, 0.4, 0.6, 1), bold=True)
        container.add_widget(title_label)

        scroll = ScrollView(size_hint=(1, 1))
        subject_layout = GridLayout(cols=1, padding=20, spacing=10, size_hint_y=None)
        subject_layout.bind(minimum_height=subject_layout.setter('height'))

        subjects = ['Biology', 'Chemistry', 'Physics', 'Maths', 'Accounting', 'Computer-Studies']
        for subject in subjects:
            subject_button = RoundedButton(text=subject, size_hint=(1, None), height=dp(40),
                                           on_press=lambda x, s=subject: self.select_subject(s))
            subject_layout.add_widget(subject_button)

        scroll.add_widget(subject_layout)
        container.add_widget(scroll)
        layout.add_widget(container)

        self.add_widget(layout)

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def select_subject(self, subject):
        popup = Popup(title='Subject Selected', content=Label(text=f'Selected {subject}'),
                      size_hint=(None, None), size=(400, 400))
        popup.open()



class BiologyScreen(Screen):
    def __init__(self, **kwargs):
        super(BiologyScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=dp(10))

        # Gradient background
        with self.canvas.before:
            Color(254 / 255, 89 / 255, 61 / 255, 1)  # Orange color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Toolbar with section buttons
        toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), padding=(dp(10), dp(10)))
        sections = ['Notes', 'Videos', 'Exercises']
        for section_name in sections:
            section_button = Button(
                text=section_name,
                size_hint_x=None,
                width=dp(100),
                background_color=(0, 0, 0, 1),
                color=(1, 1, 1, 1),
                background_normal='',
                background_down=''
            )
            section_button.bind(on_release=self.on_section_button_press)
            toolbar.add_widget(section_button)

        layout.add_widget(toolbar)

        # Banner image
        banner_image = Image(source='C:/Users/user/PycharmProjects/Sekao APP/biology1.jpeg', size_hint_y=None, height=dp(150))
        layout.add_widget(banner_image)

        # Content area for biology screen
        self.content_label = Label(
            text="Select a topic to view notes",
            font_size=dp(24),
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(100),
            valign='middle',
            halign='center'
        )
        self.content_label.bind(size=self._update_label)
        layout.add_widget(self.content_label)

        # Scrollable layout for topic buttons
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False)
        self.topic_layout = BoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=None, padding=(dp(10), dp(10)))
        self.topic_layout.bind(minimum_height=self.topic_layout.setter('height'))
        scroll_view.add_widget(self.topic_layout)
        layout.add_widget(scroll_view)

        self.add_widget(layout)

        # Load topics from files
        self.load_topics()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _update_label(self, instance, value):
        self.content_label.text_size = (self.content_label.width, None)

    def on_section_button_press(self, instance):
        section_name = instance.text.lower()  # Example: 'notes', 'videos', 'exercises'
        # Implement navigation or section content update logic here
        print(f"Switch to {section_name} section")

    def load_topics(self):
        # Replace with your actual file paths
        topic_files = [
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Detailed Notes - Topic 1 Key Concepts in Biology -  Biology GCSE.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Topic-2 Cells and control.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Topic-3 Genetics.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Topic-4 Natural selection and genetic modification.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Topic- 5 Health, disease and development of medicine.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Topic-6 Plant structures and their functions.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Topic-7 Animal coordination, control and homeostasis.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Topic-8 Ecosystems and natural cycles.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Use of biological resources explained.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Anaerobic respiration.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Breathing in humans.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Distribution and biodiversity.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Ecology and the environment.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Energy content of food.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Enzymes and pH.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Estimating population size.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Food tests.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Germination.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Photosynthesis practical notes.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Photosynthesis.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Gas exchange in plants.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Enzymes and temperature.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\The nature and variety of living organisms.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Biology1\Anaerobic respiration.pdf"
        ]
        for topic_file in topic_files:
            topic_button = Button(
                text=os.path.basename(topic_file).split('.')[0],
                size_hint_y=None,
                height=dp(40),
                background_color=(0, 0, 0, 1),
                color=(1, 1, 1, 1),
                background_normal='',
                background_down=''
            )
            topic_button.bind(on_release=lambda instance, topic=topic_file: self.open_file(topic))
            self.topic_layout.add_widget(topic_button)

    def open_file(self, topic_file):
        try:
            if os.path.exists(topic_file):
                if topic_file.endswith('.pdf'):
                    # For Android and iOS, use filechooser to open the file
                    if platform == 'android' or platform == 'ios':
                        filechooser.open_file(on_selection=self.on_file_selection)
                    else:
                        # For Windows, use os.startfile
                        if platform == 'win':
                            os.startfile(topic_file)
                        elif platform == 'macosx':  # macOS
                            os.system(f'open "{topic_file}"')
                        else:  # Linux variants
                            try:
                                subprocess.run(['xdg-open', topic_file], check=True)
                            except FileNotFoundError:
                                print("xdg-open command not found. Please ensure it's installed.")
                elif topic_file.endswith('.txt'):
                    with open(topic_file, 'r') as file:
                        self.content_label.text = file.read()
                else:
                    print("Unsupported file format")
            else:
                print(f"File not found: {topic_file}")
        except Exception as e:
            print(f"Error opening file: {e}")

    def on_file_selection(self, selection):
        if selection:
            selected_file = selection[0]
            notification.notify(title="File Selected", message=f"Opening {os.path.basename(selected_file)}")
            # Code to open the file using the default viewer on Android/iOS can be placed here
        else:
            print("No file selected")


class ChemistryScreen(Screen):
    def __init__(self, **kwargs):
        super(ChemistryScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))

        # Orange background gradient
        with self.canvas.before:
            Color(254 / 255, 89 / 255, 61 / 255, 1)  # Orange color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Toolbar with section buttons
        toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(10))

        sections = ['Notes', 'Videos', 'Exercises']
        for section_name in sections:
            section_button = Button(
                text=section_name,
                size_hint_x=None,
                width=dp(100),
                background_color=(0, 0, 0, 1),  # Black background
                color=(1, 1, 1, 1)  # White text
            )
            section_button.bind(on_release=self.on_section_button_press)
            toolbar.add_widget(section_button)

        # Add a banner image
        banner_image = Image(source='C:/Users/user/PycharmProjects/Sekao APP/chemistry2.jpg', size_hint_y=None, height=dp(200),
                             allow_stretch=True)

        # Content area for chemistry screen
        self.content_label = Label(text="Select a topic to view chemistry notes", font_size=dp(24), color=(0, 0, 0, 1))

        # Layout for topic buttons
        self.topic_layout = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        self.topic_layout.bind(minimum_height=self.topic_layout.setter('height'))
        topic_scrollview = ScrollView(size_hint=(1, None),
                                      size=(Window.width, Window.height - dp(300)))  # Adjusted height to fit everything
        topic_scrollview.add_widget(self.topic_layout)

        # Add widgets to the layout
        layout.add_widget(banner_image)
        layout.add_widget(self.content_label)
        layout.add_widget(toolbar)
        layout.add_widget(topic_scrollview)
        self.add_widget(layout)

        # Load topics from files
        self.load_topics()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_section_button_press(self, instance):
        section_name = instance.text.lower()  # Example: 'notes', 'videos', 'exercises'
        # Implement navigation or section content update logic here
        print(f"Switch to {section_name} section")

    def load_topics(self):
        # Mapping of file paths to topic names
        topic_mapping = {
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\1.1. Atomic structure.pdf": "Atomic Structure",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\1.3. Ionic bonding (1).pdf": "Ionic Bonding",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\1.4. Covalent bonding.pdf": "Covalent Bonding",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\1.5. Types of substance.pdf": "Types of Substances",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\1.6. Calculations involving masses.pdf": "Calculations Involving Masses",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\1.6. Calculations involving masses 2.pdf": "Calculations Involving Masses 2",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\2.1. States of matter.pdf": "States of Matter",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\2.2. Methods of separating and purifying substances.pdf": "Separation and Purification",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\3.1. Acids.pdf": "Acids",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\3.2. Electrolytic processes 2.pdf": "Electrolytic Processes",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\4.1. Obtaining and using metals.pdf": "Metals",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\4.1. Obtaining and using metals 2.pdf": "Metals 2",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\4.2. Reversible reactions and equilibria.pdf": "Reversible Reactions",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\5.1. Transition metals alloys and corrosion.pdf": "Transition Metals",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\5.2. Quantitative analysis.pdf": "Quantitative Analysis",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\5.2. Quantitative analysis (1).pdf": "Quantitative Analysis 2",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\5.3. Dynamic equilibria.pdf": "Dynamic Equilibria",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\5.4. Chemical cells and fuel cells.pdf": "Chemical Cells and Fuel Cells",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\6.1. Group 1.pdf": "Group 1",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\6.2. Group 7.pdf": "Group 7",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\6.3. Group 0 (1).pdf": "Group 0",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\7.1. Rates of reaction.pdf": "Rates of Reaction",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\7.2. Heat energy changes in chemical reactions.pdf": "Heat Energy Changes",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\8.1. Fuels.pdf": "Fuels",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\8.2. Earth and atmospheric science.pdf": "Earth and Atmospheric Science",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\9.1. Qualitative analysis - test for ions.pdf": "Qualitative Analysis",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\9.2. Hydrocarbons.pdf": "Hydrocarbons",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\9.3. Polymers.pdf": "Polymers",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\9.4. Alcohols and carboxylic acid.pdf": "Alcohols and Carboxylic Acid",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\9.5. Bulk and surface properties of matter including nanoparticles.pdf": "Bulk and Surface Properties",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\CP 2 - Investigating pH.pdf": "Investigating pH",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\CP 3 - Preparing Copper Sulfate.pdf": "Preparing Copper Sulfate",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\CP 4 - Electrolysis of copper sulfate solution.pdf": "Electrolysis of Copper Sulfate",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\CP 5 - Acid-Alkali Titration.pdf": "Acid-Alkali Titration",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\CP 6 - Investigating Reaction Rates.pdf": "Investigating Reaction Rates",
            r"C:\Users\user\PycharmProjects\Sekao APP\CHEM\CP 7 - Identifying Ions.pdf": "Identifying Ions"
        }

        for topic_file, topic_name in topic_mapping.items():
            topic_button = Button(
                text=topic_name,
                size_hint_y=None,
                height=dp(40),
                background_color=(0, 0, 0, 1),  # Black background
                color=(1, 1, 1, 1)  # White text
            )
            topic_button.bind(on_release=lambda instance, topic=topic_file: self.open_file(topic))
            self.topic_layout.add_widget(topic_button)

    def open_file(self, topic_file):
        try:
            if os.path.exists(topic_file):
                if topic_file.endswith('.pdf'):
                    # For Android and iOS, use filechooser to open the file
                    if platform == 'android' or platform == 'ios':
                        filechooser.open_file(on_selection=self.on_file_selection)
                    else:
                        # For desktop platforms, use the appropriate command to open the file
                        if platform == 'macosx':  # macOS
                            os.system(f'open "{topic_file}"')
                        elif platform == 'win':  # Windows
                            os.startfile(topic_file)
                        else:  # Linux variants
                            os.system(f'xdg-open "{topic_file}"')
                elif topic_file.endswith('.txt'):
                    with open(topic_file, 'r') as file:
                        self.content_label.text = file.read()
                else:
                    print("Unsupported file format")
            else:
                print(f"File not found: {topic_file}")
        except Exception as e:
            print(f"Error opening file: {e}")

    def on_file_selection(self, selection):
        if selection:
            selected_file = selection[0]
            self.open_file(selected_file)

class PhysicsScreen(Screen):
    def __init__(self, **kwargs):
        super(PhysicsScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))

        # Orange background gradient
        with self.canvas.before:
            Color(254 / 255, 89 / 255, 61 / 255, 1)  # Orange color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Toolbar with section buttons
        toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(10))

        sections = ['Notes', 'Videos', 'Exercises']
        for section_name in sections:
            section_button = Button(
                text=section_name,
                size_hint_x=None,
                width=dp(100),
                background_color=(0, 0, 0, 1),  # Black background
                color=(1, 1, 1, 1)  # White text
            )
            section_button.bind(on_release=self.on_section_button_press)
            toolbar.add_widget(section_button)

        # Add a banner image between toolbar and topic buttons
        banner_image = Image(source='C:/Users/user/PycharmProjects/Sekao APP/physics2.jpeg', size_hint_y=None, height=dp(200), allow_stretch=True)

        # Content area for physics screen
        self.content_label = Label(text="Select a topic to view physics notes", font_size=dp(24), color=(0, 0, 0, 1), size_hint_y=None, height=dp(40))

        # Layout for topic buttons
        self.topic_layout = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        self.topic_layout.bind(minimum_height=self.topic_layout.setter('height'))

        # Adjust ScrollView size to accommodate banner and content label
        topic_scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - dp(300)))  # 60 (toolbar) + 200 (banner) + 40 (content_label) = 300

        topic_scrollview.add_widget(self.topic_layout)

        # Add widgets to the layout
        layout.add_widget(toolbar)
        layout.add_widget(banner_image)
        layout.add_widget(self.content_label)
        layout.add_widget(topic_scrollview)
        self.add_widget(layout)

        # Load topics from files
        self.load_topics()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_section_button_press(self, instance):
        section_name = instance.text.lower()  # Example: 'notes', 'videos', 'exercises'
        # Implement navigation or section content update logic here
        print(f"Switch to {section_name} section")

    def load_topics(self):
        # Mapping of file paths to topic names
        topic_mapping = {
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\1.1. Motion.pdf": "Motion",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\1.2. Forces.pdf": "Forces",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\1.3. Energy.pdf": "Energy",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\2.1. Waves.pdf": "Waves",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\2.2. Sound.pdf": "Sound",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\3.1. Electricity.pdf": "Electricity",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\3.2. Magnetism.pdf": "Magnetism",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\4.1. Light.pdf": "Light",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\4.2. Optics.pdf": "Optics",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\5.1. Atomic physics.pdf": "Atomic Physics",
            r"C:\Users\user\PycharmProjects\Sekao APP\PHYS\5.2. Nuclear physics.pdf": "Nuclear Physics",
            # Add more topics as needed
        }

        for topic_file, topic_name in topic_mapping.items():
            topic_button = Button(
                text=topic_name,
                size_hint_y=None,
                height=dp(40),
                background_color=(0, 0, 0, 1),  # Black background
                color=(1, 1, 1, 1)  # White text
            )
            topic_button.bind(on_release=lambda instance, topic=topic_file: self.open_file(topic))
            self.topic_layout.add_widget(topic_button)

    def open_file(self, topic_file):
        try:
            if os.path.exists(topic_file):
                if topic_file.endswith('.pdf'):
                    # For Android and iOS, use filechooser to open the file
                    if platform == 'android' or platform == 'ios':
                        filechooser.open_file(on_selection=self.on_file_selection)
                    else:
                        # For desktop platforms, use the appropriate command to open the file
                        if platform == 'macosx':  # macOS
                            os.system(f'open "{topic_file}"')
                        elif platform == 'win':  # Windows
                            os.startfile(topic_file)
                        else:  # Linux variants
                            os.system(f'xdg-open "{topic_file}"')
                elif topic_file.endswith('.txt'):
                    with open(topic_file, 'r') as file:
                        self.content_label.text = file.read()
                else:
                    print("Unsupported file format")
            else:
                print(f"File not found: {topic_file}")
        except Exception as e:
            print(f"Error opening file: {e}")

    def on_file_selection(self, selection):
        if selection:
            selected_file = selection[0]
            self.open_file(selected_file)


class MathScreen(Screen):
    def __init__(self, **kwargs):
        super(MathScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))

        # Orange background gradient
        with self.canvas.before:
            Color(254 / 255, 89 / 255, 61 / 255, 1)  # Orange color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Toolbar with section buttons
        toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(10))

        sections = ['Notes', 'Videos', 'Exercises']
        for section_name in sections:
            section_button = Button(
                text=section_name,
                size_hint_x=None,
                width=dp(100),
                background_color=(0, 0, 0, 1),  # Black background
                color=(1, 1, 1, 1)  # White text
            )
            section_button.bind(on_release=self.on_section_button_press)
            toolbar.add_widget(section_button)

        # Banner image
        banner_image = Image(source='C:/Users/user/PycharmProjects/Sekao APP/math1.jpeg', size_hint_y=None, height=dp(200), allow_stretch=True)

        # Content area for math screen
        self.content_label = Label(text="Select a topic to view math notes", font_size=dp(24), color=(0, 0, 0, 1), size_hint_y=None, height=dp(40))

        # Layout for topic buttons
        self.topic_layout = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        self.topic_layout.bind(minimum_height=self.topic_layout.setter('height'))

        # Adjust ScrollView size to accommodate banner and content label
        topic_scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - dp(60) - dp(200) - dp(40) - dp(20)))  # Adjust height
        topic_scrollview.add_widget(self.topic_layout)

        # Back button (initially hidden)
        self.back_button = Button(
            text="Back",
            size_hint_y=None,
            height=dp(40),
            background_color=(0, 0, 0, 1),  # Black background
            color=(1, 1, 1, 1),  # White text
            on_release=self.go_back_to_topics,
            opacity=0,  # Initially hidden
            disabled=True  # Initially disabled
        )

        # Add widgets to the layout
        self.layout.add_widget(toolbar)
        self.layout.add_widget(banner_image)
        self.layout.add_widget(self.content_label)
        self.layout.add_widget(self.back_button)  # Add back button to layout
        self.layout.add_widget(topic_scrollview)
        self.add_widget(self.layout)

        # Load topics from files
        self.load_topics()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_section_button_press(self, instance):
        section_name = instance.text.lower()  # Example: 'notes', 'videos', 'exercises'
        # Implement navigation or section content update logic here
        print(f"Switch to {section_name} section")

    def load_topics(self):
        # Mapping of file paths to topic names
        topic_mapping = {
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\1- Notationand vocabulary.pdf": "Notation and Vocabulary",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\2- Solving linear equations.pdf": "Solving Linear Equations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\3 - Collecting like terms.pdf": "Collecting Like Terms",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\2- Solving linear equations.pdf": "Solving linear equations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\3 - Collecting like terms.pdf": "Collecting like terms",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\4 - Common sequences.pdf": "Common sequences",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\4 - Simplifying expressions.pdf": "Simplifying expressions",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\5 - Roots, intercepts and turning points.pdf":"Roots, intercepts and turning points.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\5 - Solving linear inequalities.pdf": "Solving linear inequalities",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\6 - Solving quadratic equations.pdf": "Solving quadratic equations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\7 - Completing the square.pdf":"Completing the square.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\8 - Expanding brackets.pdf":" Expanding brackets",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\9 - Forming and solving equations.pdf":"Forming and solving equations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\9 - Nth term.pdf": "Nth term",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\10 - Simultaneous equations.pdf": "Simultaneous equations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\11 - Numerical iteration.pdf": "Numerical iteration",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\12 - Sketching graphs - Linear, cubic and quadratic equations.pdf": "Sketching graphs - Linear, cubic and quadratic equations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\13 - Law of indices.pdf": " Law of indices",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\14 - Translations and reflections.pdf" : "Translations and reflections",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\15 - Expressions involving surd and quadratic fractions.pdf" : "Expressions involving surd and quadratic fractions",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\16 - Gradients and areas of graphs in context.pdf": "Gradients and areas of graphs in context",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\17 - Solving quadratic inequalities.pdf": "Solving quadratic inequalities",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\18 -  Equations of a circle and its tangent.pdf" : " Equations of a circle and its tangent",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\19 - Rearranging formulae.pdf" : "Rearranging formulae",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\20 - Equivalent algebraic expressions.pdf": "Equivalent algebraic expressions",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\21 - Functions.pdf" : "Functions",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\22 - Generating a sequence.pdf" : " Generating a sequence",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\23 - Standard and compound units.pdf" : "Standard and compound units",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Algebra\24 - Straight line graphs.pdf" : "Straight line graphs",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Arc length and area of sector.pdf" : "Arc length and area of sector",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Area nad perimeter of 2D shapes.pdf" : "Area nad perimeter of 2D shapes",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Circle theorems.pdf" : "Circle theorems",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Congruence - Length, area and volume.pdf" : "Congruence - Length, area and volume",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Congruent triangles.pdf" : "Congruent triangles",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Construction.pdf" : "Construction",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Geometric arguments and proof.pdf" : "Geometric arguments and proof",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Measuring lines,angles and bearings.pdf" : "Measuring lines,angles and bearings",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Plans and elevations.pdf" : "Plans and elevations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Properties of circles.pdf" : "Properties of circles",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Properties of triangles and quadrilaterals.pdf" : "Properties of triangles and quadrilaterals",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Pythagoraus' theorem.pdf" : "Pythagoraus' theorem",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Rotation, reflection, translation and enlargements.pdf" : "Rotation, reflection, translation and enlargements",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Sine and cosine rules and area of triangle.pdf" : "Sine and cosine rules and area of triangle",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Surface of shapes.pdf" : "Surface of shapes",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Trigonometric ratios and exact trigonometric values.pdf" : "Trigonometric ratios and exact trigonometric values",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Units of measurements.pdf" : "Units of measurements",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Vector operations.pdf" : "Vector operations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Vocubulary and notation.pdf" : "Vocubulary and notation",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Geometry and measures\Volume of 3D shapes.pdf" : "Volume of 3D shapes",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Estimation and approximation.pdf" : "Estimation and approximation",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Exact values and surds.pdf" : "Exact values and surds",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Factors, multiples and primes.pdf" : "Factors, multiples and primes",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Four operations.pdf" : "Four operations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Fractionla and percentage operators.pdf" : "Fractionla and percentage operators",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Powers, roots and fractional indices.pdf" : "Powers, roots and fractional indices",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Ratio problems.pdf" : "Ratio problems",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Rounding and limits of accuracy.pdf" : "Rounding and limits of accuracy",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Standard form.pdf" : "Standard form",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Systematic listing.pdf" : "Systematic listing",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Numbers\Terminating and reocurring decimals.pdf" : "Terminating and reocurring decimals",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Probability\Conditional probability.pdf" : "Conditional probability",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Probability\Enumeration, venn diagrams, tree diagrams and tables.pdf" : "Enumeration, venn diagrams, tree diagrams and tables",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Probability\Exhaustive and mutually exclusive events.pdf" : "Exhaustive and mutually exclusive events",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Probability\Expected outcomes, frequency and theoretical probability.pdf" : "Expected outcomes, frequency and theoretical probability",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Probability\Independent and dependent events.pdf" : "Independent and dependent events",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Probability\Sample spaces.pdf" : "Sample spaces",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Probability\Table of outcomes and frequency trees.pdf" : "Table of outcomes and frequency trees",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Compound growth and decay.pdf" : "Compound growth and decay",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Direct and inverse proportion.pdf" : "Direct and inverse proportion",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\General iterative processes.pdf" : "General iterative processes",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Intepreting percentages.pdf" : "Intepreting percentages",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Interpreting gradients.pdf" : "Interpreting gradients",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Percentage change.pdf" : "Percentage change",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Ratio(Ratio,proportion and rates of exchange).pdf" : "Ratio(Ratio,proportion and rates of exchange)",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Ratio and similar shapes.pdf" : "Ratio and similar shapes",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Scale factors and scale diagrams.pdf" : "Scale factors and scale diagrams",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Ration,proportion and rates of exchange\Simple interest.pdf" : "Simple interest",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Statistics\Graphical representation of distributions.pdf" : "Graphical representation of distributions",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Statistics\Grouped discrete data and continous data.pdf" : "Grouped discrete data and continous data",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Statistics\Measures of central tendency.pdf" : "Measures of central tendency",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Statistics\Populations.pdf" : "Populations",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Statistics\Sampling.pdf" : "Sampling",
            r"C:\Users\user\PycharmProjects\Sekao APP\Math2\Statistics\Table,charts and diagrams.pdf" : "Table,charts and diagrams"

        }

        for topic_file, topic_name in topic_mapping.items():
            topic_button = Button(
                text=topic_name,
                size_hint_y=None,
                height=dp(40),
                background_color=(0, 0, 0, 1),  # Black background
                color=(1, 1, 1, 1)  # White text
            )
            topic_button.bind(on_release=lambda instance, topic=topic_file: self.open_file(topic))
            self.topic_layout.add_widget(topic_button)

    def open_file(self, topic_file):
        try:
            if os.path.exists(topic_file):
                if topic_file.endswith('.pdf'):
                    # For Android and iOS, use filechooser to open the file
                    if platform == 'android' or platform == 'ios':
                        filechooser.open_file(on_selection=self.on_file_selection)
                    else:
                        # For desktop platforms, use the appropriate command to open the file
                        if platform == 'macosx':  # macOS
                            os.system(f'open "{topic_file}"')
                        elif platform == 'win':  # Windows
                            os.startfile(topic_file)
                        else:  # Linux variants
                            os.system(f'xdg-open "{topic_file}"')
                elif topic_file.endswith('.txt'):
                    with open(topic_file, 'r') as file:
                        self.content_label.text = file.read()
                else:
                    print("Unsupported file format")

                # Show the back button
                self.back_button.opacity = 1
                self.back_button.disabled = False
                # Hide the topic buttons
                self.topic_layout.parent.opacity = 0
                self.topic_layout.parent.disabled = True

            else:
                print(f"File not found: {topic_file}")
        except Exception as e:
            print(f"Error opening file: {e}")

    def on_file_selection(self, selection):
        if selection:
            selected_file = selection[0]
            self.open_file(selected_file)

    def go_back_to_topics(self, instance):
        # Hide the back button
        self.back_button.opacity = 0
        self.back_button.disabled = True
        # Show the topic buttons
        self.topic_layout.parent.opacity = 1
        self.topic_layout.parent.disabled = False
        # Reset the content label
        self.content_label.text = "Select a topic to view math notes"

class ComputerStudies(Screen):
    def __init__(self, **kwargs):
        super(ComputerStudies, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=dp(10))

        # Orange background gradient
        with self.canvas.before:
            Color(254 / 255, 89 / 255, 61 / 255, 1)  # Orange color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Toolbar with section buttons
        toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))

        sections = ['Notes', 'Videos', 'Exercises']
        for section_name in sections:
            section_button = Button(
                text=section_name,
                size_hint_x=None,
                width=dp(100),
                background_color=(0, 0, 0, 1),
                color=(1, 1, 1, 1),
                font_size=sp(16),
                bold=True
            )
            section_button.bind(on_release=self.on_section_button_press)
            toolbar.add_widget(section_button)

        layout.add_widget(toolbar)

        # Banner image
        banner_image = Image(
            source='C:/Users/user/PycharmProjects/Sekao APP/cs1.jpg',  # Update path as needed
            size_hint_y=None,
            height=dp(200),
            allow_stretch=True,
            keep_ratio=False
        )
        layout.add_widget(banner_image)

        # Content area for computer studies screen
        self.content_label = Label(
            text="Select a topic to view notes",
            font_size=dp(24),
            color=(0, 0, 0, 1),
            halign='center',
            size_hint_y=None,
            height=dp(50)
        )
        layout.add_widget(self.content_label)

        # Scrollable layout for topic buttons
        scroll_view = ScrollView(size_hint=(1, 1))
        self.topic_layout = BoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=None)
        self.topic_layout.bind(minimum_height=self.topic_layout.setter('height'))
        scroll_view.add_widget(self.topic_layout)
        layout.add_widget(scroll_view)

        self.add_widget(layout)

        # Load topics from files
        self.load_topics()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_section_button_press(self, instance):
        section_name = instance.text.lower()  # Example: 'notes', 'videos', 'exercises'
        # Implement navigation or section content update logic here
        print(f"Switch to {section_name} section")

    def load_topics(self):
        # Replace with your actual file paths
        topic_files = [
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Introduction to computers.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Introduction to computers and their applications.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Computer applications.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\impact_computers_on_our_society.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Computer security.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Data communications.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\File Management.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\File management and data processing.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Introduction to programming.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Introduction to programming part 2.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Computer packages.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Types of Operating System-converted.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\Systems_development_life_cycle.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Computer Studies\System Development Life Cycle (2).pdf"
        ]
        for topic_file in topic_files:
            topic_button = Button(
                text=os.path.basename(topic_file).split('.')[0],
                size_hint_y=None,
                height=dp(60),
                background_color=(0, 0, 0, 1),
                color=(1, 1, 1, 1),
                font_size=sp(16),
                bold=True
            )
            topic_button.bind(on_release=lambda instance, topic=topic_file: self.open_file(topic))
            self.topic_layout.add_widget(topic_button)

    def open_file(self, topic_file):
        try:
            if os.path.exists(topic_file):
                if topic_file.endswith('.pdf'):
                    # For Android and iOS, use filechooser to open the file
                    if platform == 'android' or platform == 'ios':
                        filechooser.open_file(on_selection=self.on_file_selection)
                    else:
                        # For desktop platforms, use the appropriate command to open the file
                        if platform == 'macosx':  # macOS
                            os.system(f'open "{topic_file}"')
                        elif platform == 'win':  # Windows
                            os.startfile(topic_file)
                        else:  # Linux variants
                            os.system(f'xdg-open "{topic_file}"')
                elif topic_file.endswith('.txt'):
                    with open(topic_file, 'r') as file:
                        self.content_label.text = file.read()
                else:
                    print("Unsupported file format")
            else:
                print(f"File not found: {topic_file}")
        except Exception as e:
            print(f"Error opening file: {e}")

    def on_file_selection(self, selection):
        if selection:
            selected_file = selection[0]
            notification.notify(title="File Selected", message=f"Opening {os.path.basename(selected_file)}")
            # Code to open the file using the default viewer on Android/iOS can be placed here
        else:
            print("No file selected")

class AccountingScreen(Screen):
    def __init__(self, **kwargs):
        super(AccountingScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=dp(10))

        # Orange background gradient
        with self.canvas.before:
            Color(254 / 255, 89 / 255, 61 / 255, 1)  # Orange color
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Toolbar with section buttons
        toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))

        sections = ['Notes', 'Videos', 'Exercises']
        for section_name in sections:
            section_button = Button(
                text=section_name,
                size_hint_x=None,
                width=dp(100),
                background_color=(0, 0, 0, 1),  # Black background
                color=(1, 1, 1, 1)  # White text color
            )
            section_button.bind(on_release=self.on_section_button_press)
            toolbar.add_widget(section_button)

        layout.add_widget(toolbar)

        # Banner image
        banner_image = Image(source='C:/Users/user/PycharmProjects/Sekao APP/accounting3.jpeg', size_hint_y=None, height=dp(150))
        layout.add_widget(banner_image)

        # Content area for accounting screen
        self.content_label = Label(
            text="Select a topic to view accounting notes",
            font_size=dp(24),
            color=(0, 0, 0, 1)
        )
        layout.add_widget(self.content_label)

        # ScrollView for topic buttons
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - dp(100) - dp(150)))
        scroll_view.do_scroll_x = False
        scroll_view.do_scroll_y = True

        # Layout for topic buttons inside ScrollView
        self.topic_layout = GridLayout(cols=2, spacing=dp(10), size_hint_y=None)
        self.topic_layout.bind(minimum_height=self.topic_layout.setter('height'))

        scroll_view.add_widget(self.topic_layout)
        layout.add_widget(scroll_view)

        self.add_widget(layout)

        # Load topics from files
        self.load_topics()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_section_button_press(self, instance):
        section_name = instance.text.lower()  # Example: 'notes', 'videos', 'exercises'
        # Implement navigation or section content update logic here
        print(f"Switch to {section_name} section")

    def load_topics(self):
        # Replace with your actual file paths for accounting
        topic_files = [
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Accounting Concepts and Conventions.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Accounting definitions.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Introduction to accounting.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Basics-of-Accounting.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\fundamentals-of-accounting.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Bookkeeping.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Basic-Farm-Accounting.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Bookkeeping.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Company accounts- 2.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Financial accounting.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Financial accounting -2.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Interpretation of financial statements.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Ledger.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Manufacturing accounts.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Non-profit organizations or club accounts.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Not for profit organizations.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Partnership accounting.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\partnership_notes.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Posting in ledgers and blancing the ledgers.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Single entry and.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Subsidiary books.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\Subsidiary books-2.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\The accounting equation.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\The double entry system.pdf",
            r"C:\Users\user\PycharmProjects\Sekao APP\Accounting2\The ledger and the trial balance.pdf"
        ]
        for topic_file in topic_files:
            topic_button = Button(
                text=os.path.basename(topic_file).split('.')[0],
                size_hint_y=None,
                height=dp(40),
                background_color=(0, 0, 0, 1),  # Black background
                color=(1, 1, 1, 1)  # White text color
            )
            topic_button.bind(on_release=lambda instance, topic=topic_file: self.open_file(topic))
            self.topic_layout.add_widget(topic_button)

    def open_file(self, topic_file):
        try:
            if os.path.exists(topic_file):
                if topic_file.endswith('.pdf'):
                    # For Android and iOS, use filechooser to open the file
                    if platform == 'android' or platform == 'ios':
                        filechooser.open_file(on_selection=self.on_file_selection)
                    else:
                        # For desktop platforms, use the appropriate command to open the file
                        if platform == 'macosx':  # macOS
                            os.system(f'open "{topic_file}"')
                        elif platform == 'win':  # Windows
                            os.startfile(topic_file)
                        else:  # Linux variants
                            os.system(f'xdg-open "{topic_file}"')
                elif topic_file.endswith('.txt'):
                    with open(topic_file, 'r') as file:
                        self.content_label.text = file.read()
                else:
                    print("Unsupported file format")
            else:
                print(f"File not found: {topic_file}")
        except Exception as e:
            print(f"Error opening file: {e}")

    def on_file_selection(self, selection):
        if selection:
            selected_file = selection[0]
            notification.notify(title="File Selected", message=f"Opening {os.path.basename(selected_file)}")
            # Code to open the file using the default viewer on Android/iOS can be placed here
        else:
            print("No file selected")

class SeniorSchoolScreen(Screen):
    def __init__(self, **kwargs):
        super(SeniorSchoolScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Background image at the top
        background_image = Image(source='home2.jpeg', size_hint=(1, None), height=dp(200))
        layout.add_widget(background_image)

        # Container for the rest of the widgets
        container = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(1, 0.7))

        with container.canvas.before:
            Color(0.8, 0.8, 0.8, 1)  # Light grey background color for the container
            self.rect = Rectangle(size=container.size, pos=container.pos)
        container.bind(size=self.update_rect, pos=self.update_rect)

        title_label = Label(text="Senior School Subjects", font_size='24sp', color=(0.2, 0.4, 0.6, 1), bold=True)
        container.add_widget(title_label)

        scroll = ScrollView(size_hint=(1, 1))
        subject_layout = GridLayout(cols=1, padding=20, spacing=10, size_hint_y=None)
        subject_layout.bind(minimum_height=subject_layout.setter('height'))

        subjects = ['Advanced Math', 'Physics', 'Chemistry', 'Biology', 'Literature', 'History', 'Economics']
        for subject in subjects:
            subject_button = RoundedButton(text=subject, size_hint=(1, None), height=dp(40),
                                           on_press=lambda x, s=subject: self.select_subject(s))
            subject_layout.add_widget(subject_button)

        scroll.add_widget(subject_layout)
        container.add_widget(scroll)
        layout.add_widget(container)
... 
...         self.add_widget(layout)
... 
...     def update_rect(self, instance, value):
...         self.rect.size = instance.size
...         self.rect.pos = instance.pos
... 
...     def select_subject(self, subject):
...         popup = Popup(title='Subject Selected', content=Label(text=f'Selected {subject}'),
...                       size_hint=(None, None), size=(400, 400))
...         popup.open()
... 
... class MyScreenManager(ScreenManager):
...     def __init__(self, **kwargs):
...         super(MyScreenManager, self).__init__(**kwargs)
...         self.add_widget(HomeScreen(name='home'))
...         self.add_widget(JuniorSchoolScreen(name='junior'))
...         self.add_widget(SeniorSchoolScreen(name='senior'))
...         self.add_widget(CreateProfileScreen(name='create_profile'))
...         self.add_widget(PaymentScreen(name='payment'))
...         self.add_widget(NoteScreen(name='note_screen'))
...         self.add_widget(BiologyScreen(name='biology_screen'))
...         self.add_widget(ChemistryScreen(name='chemistry_screen'))
...         self.add_widget(PhysicsScreen(name='physics_screen'))
...         self.add_widget(MathScreen(name='mathematics_screen'))
...         self.add_widget(ComputerStudies(name='computer_screen'))
...         self.add_widget(AccountingScreen(name='accounting_screen'))
...         self.add_widget(ProfileScreen(name="profile_screen"))
... 
... 
... 
... class MyApp(App):
...     def build(self):
...         return MyScreenManager()
... 
... 
... if __name__ == '__main__':
...     MyApp().run()
