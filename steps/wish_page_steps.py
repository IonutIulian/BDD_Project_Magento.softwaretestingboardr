from behave import *


@when ("Wish page: Click on the Share Wish List button")
def step_impl(context):
    context.wish_page_object.share_wish()

@when ('Wish page: Enter friends email "{emails}"')
def step_impl(context , emails):
    context.wish_page_object.enter_emails(emails)

@when ('Wish page: Write them a message "{message}"')
def step_impl(context , message):
    context.wish_page_object.enter_message(message)

@then ("Wish page: Click on the Share Wish List button")
def step_impl(context):
    context.wish_page_object.share()

@then ("Wish page: Check confirmation message")
def step_impl(context):
    context.wish_page_object.confirm()