from behave import *

@when  ('Checkout page: Enter "{street}" address')
def step_impl(context,street):
    context.checkout_page_obiect.street_address(street)

@when ('Checkout page: Select "{state}" and "{province}"')
def step_impl(context,state, province):
    context.checkout_page_obiect.country_region(state,province)

@when ('Checkout page: Enter "{postcode}" and "{city}"')
def step_impl(context,postcode, city):
    context.checkout_page_obiect.postcode_city(postcode, city)

@when ('Checkout page: Enter "{phone}" number')
def step_impl(context, phone):
    context.checkout_page_obiect.phone_number(phone)

@then ("Checkout page: Click next and place order buttons")
def step_impl(context):
    context.checkout_page_obiect.next_place_order()