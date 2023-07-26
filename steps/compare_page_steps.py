from behave import *


@then ("Compare page: Cancel one item from the compare section")
def step_impl(context):
    context.compare_page_object.cancel_item()

@then ("Compare page: Add the other item to the wish list")
def step_impl(context):
    context.compare_page_object.add_wishlist()