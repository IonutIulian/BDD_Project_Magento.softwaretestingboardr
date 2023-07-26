from behave import *



@when ('Login page: I enter the email address, "{email}"')
def step_impl(context, email):
    context.login_page_object.enter_email(email)

@when ('Login page: I enter the password, "{passowrd}"')
def step_impl(context, passowrd):
    context.login_page_object.enter_password(passowrd)

@then ("Login page: Click on the Sign in button")
def step_impl(context):
    context.login_page_object.click_signin()