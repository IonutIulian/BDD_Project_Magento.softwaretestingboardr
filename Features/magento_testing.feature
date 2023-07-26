Feature: Testing the functionality of magento.softwaretestingboard.com webpage


  Background:
    Given Home page: I am on magento.softwaretestingboard.com starting page

  @TEST1
  Scenario: Testing the magento.softwaretestingboard.com home page

    When  Home page: I check if I am on the right page
    Then  Home page: Check that the welcome message is displayed

  @TEST2
  Scenario: Testing the functionality of creating a user account on magento.softwaretestingboard.com

    When  Home page: Press the Create an Account link
    When  Create account page: Enter "Mihai" "Barbulescu" and "mihaita.vra@gmail.com"
    When  Create account page: Sign Up for Newsletter
    When  Create account page: Enter a  weak password "{parol}"
    Then  Create account page: Check message and change password to a stronger one"PARola123"
    When  Create account page: Enter the password in the confirmation-password textbox"PARola123"
    Then  Create account page: Click the Create Account button
    Then  Create account page: Check if the registering message is displayed

  @TEST3
  Scenario: Choose shopping options and add item to cart

    When  Home page: I click on the Men button category
    When  Men category page: I click on the jacket category
    When  Men category page: Choose shopping option style
    When  Men category page: Choose shopping option performance-fabric
    Then  Men category page: Sort the resulting items by "Price"
    When  Men category page: Select the cheapest jacket
    When  Men category page: Select size and color of the jacket
    Then  Men category page: Add to cart the desired jacket

  @TEST4
  Scenario: Enter shipping address

    When  Home page: Click the cart button
    Then  Home page: Click the Proceed checkout button
    When  Checkout page: Enter "str. Valcica nr.214" address
    When  Checkout page: Select "Romania" and "Suceava"
    When  Checkout page: Enter "123456" and "Falticeni"
    When  Checkout page: Enter "0745612370" number
    Then  Checkout page: Click next and place order buttons

  @TEST5
  Scenario Outline: Add items to wish list and review them

    When  Home page: I search for a specific "<item_name>"
    Then  Home page: Adding the item to the wish list
    When  Home page: Click the reviews button
    When  Home page: Set a rating for the item
    When  Home page: Write the "<review_title>" and the "<text_review>"
    Then  Home page: Click submit review and check the confirmation message
    Examples:
      |item_name      | review_title|                   text_review                               |
      |Driven Backpack|Un rucsac ok |Un raport pret-calitate bun, nu exceleaza dar isi face treaba|
      |Clamber Watch  |Pret bun     |L-am cumparat pentru sotia mea si a fost multumita           |


  @TEST6
  Scenario: Sign out from magento.softwaretestingboard.com

    When Home page: Click on the small arrow near the name
    When Home page: Click on the Sign out button
    Then Home page: Check that the sign out message is displayed

  @TEST7
  Scenario: Sign in to magento.softwaretestingboard.com

    When Home page: Click on the sign in button
    When Login page: I enter the email address, "mihaita.vra@gmail.com"
    When Login page: I enter the password, "PARola123"
    Then Login page: Click on the Sign in button

  @TEST8
  Scenario Outline: Add items to Compare Products section

    When Home page: I search for a specific "<item_name>"
    Then Home page: Click on the desired item
    When Home page: Click the Add to compare button
    Then Home page: Check that the confirmation message is displayed
    Examples:
    |item_name                   |
    |Aether Gym Pant             |
    |Livingston All-Purpose Tight|

  @TEST9
  Scenario: Add one item to wish list and delete the other one

    When Home page: Click on the Compare Products link
    Then Compare page: Cancel one item from the compare section
    Then Compare page: Add the other item to the wish list

  @TEST10
  Scenario: Share your wish list with your friends

    When Home page: Click on the small arrow near  the name
    Then Home page: Click on the  Your Wish list button
    When Wish page: Click on the Share Wish List button
    When Wish page: Enter friends email "costi@gmail.com , george@yahoo.com"
    When Wish page: Write them a message "Ce parere aveti despre aceste produse?"
    Then Wish page: Click on the Share Wish List button
    Then Wish page: Check confirmation message











