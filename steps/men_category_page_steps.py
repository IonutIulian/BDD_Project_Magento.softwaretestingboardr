from behave import *

@when ("Men category page: I click on the jacket category")
def step_impl(context):
    context.men_page_object.category_jackets()

@when ("Men category page: Choose shopping option style")
def step_impl(context):
    context.men_page_object.select_style()

@when ("Men category page: Choose shopping option performance-fabric")
def step_impl(context):
    context.men_page_object.select_performance_fabric()

@then ('Men category page: Sort the resulting items by "{sort}"')
def step_impl(context,sort):
    context.men_page_object.sort_results(sort)

@when ("Men category page: Select the cheapest jacket")
def step_impl(context):
    context.men_page_object.cheapest()

@when ("Men category page: Select size and color of the jacket")
def step_impl(context):
    context.men_page_object.size_color()

@then ("Men category page: Add to cart the desired jacket")
def step_impl(context):
    context.men_page_object.add_cart()









