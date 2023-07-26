from behave import *


@when ('Create account page: Enter "{first_name}" "{last_name}" and "{email}"')
def step_impl(context,first_name,last_name,email):
    context.account_page_object.enter_names_email(first_name,last_name,email)

@when ("Create account page: Sign Up for Newsletter")
def step_impl(context):
    context.account_page_object.sign_newsletter()

@when ('Create account page: Enter a  weak password "{pass_1}"')
def step_impl(context,pass_1):
    context.account_page_object.weak_password(pass_1)

@then ('Create account page: Check message and change password to a stronger one"{pass_2}"')
def step_impl(context,pass_2):
    context.account_page_object.strong_pass_check_msg(pass_2)

@when ('Create account page: Enter the password in the confirmation-password textbox"{same_pass}"')
def step_impl(context,same_pass):
    context.account_page_object.confirm_pass(same_pass)

@then ("Create account page: Click the Create Account button")
def step_impl(context):
    context.account_page_object.click_create()

@then ("Create account page: Check if the registering message is displayed")
def step_impl(context):
    context.account_page_object.regist_msg()
