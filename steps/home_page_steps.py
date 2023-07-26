from behave import *


@given("Home page: I am on magento.softwaretestingboard.com starting page")
def steo_impl(context):
    context.home_page_obiect.navigate_to_homepage()

@when ("Home page: I check if I am on the right page")
def step_impl(context):
    context.home_page_obiect.check_url()

@then ("Home page: Check that the welcome message is displayed")
def step_impl(context):
    context.home_page_obiect.check_welcome_msg()

@when ("Home page: Press the Create an Account link")
def step_impl(context):
    context.home_page_obiect.click_create_account()

@when ("Home page: I click on the Men button category")
def step_impl(context):
    context.home_page_obiect.category_men()

@when ("Home page: Click the cart button")
def step_impl(context):
    context.home_page_obiect.acces_cart()

@then ("Home page: Click the Proceed checkout button")
def step_impl(context):
    context.home_page_obiect.perform_checkout()

@when ('Home page: I search for a specific "{item_name}"')
def step_impl(context,item_name):
    context.home_page_obiect.search_item(item_name)

@then ("Home page: Adding the item to the wish list")
def step_impl(context):
    context.home_page_obiect.add_to_wishlist()

@when ("Home page: Click the reviews button")
def step_impl(context):
    context.home_page_obiect.check_reviews()

@when ("Home page: Set a rating for the item")
def step_impl(context):
    context.home_page_obiect.rate_item()

@when ('Home page: Write the "{review_title}" and the "{text_review}"')
def step_impl(context,review_title,text_review):
    context.home_page_obiect.write_review(review_title,text_review)

@then ("Home page: Click submit review and check the confirmation message")
def step_impl(context):
    context.home_page_obiect.submit_check_message()

@when ("Home page: Click on the small arrow near the name")
def step_impl(context):
    context.home_page_obiect.click_arrow()

@when ("Home page: Click on the Sign out button")
def step_impl(context):
    context.home_page_obiect.sign_out()

@then ("Home page: Check that the sign out message is displayed")
def step_impl(context):
    context.home_page_obiect.sign_out_msg()

@when ("Home page: Click on the sign in button")
def step_impl(context):
    context.home_page_obiect.sign_in()

@when ('When Home page: I search for a specific "{item_name}"')
def step_impl(context, item_name):
    context.home_page_obiect.search_item(item_name)

@then ("Home page: Click on the desired item")
def step_impl(context):
    context.home_page_obiect.click_item()

@when ("Home page: Click the Add to compare button")
def step_impl(context):
    context.home_page_obiect.add_compare()

@then ("Home page: Check that the confirmation message is displayed")
def step_impl(context):
    context.home_page_obiect.check_confirmation()

@when ("Home page: Click on the Compare Products link")
def step_impl(context):
    context.home_page_obiect.compare_products()

@when ("Home page: Click on the small arrow near  the name")
def step_impl(context):
    context.home_page_obiect.click_arrow()

@then ("Home page: Click on the  Your Wish list button")
def step_impl(context):
    context.home_page_obiect.to_wish_list()
