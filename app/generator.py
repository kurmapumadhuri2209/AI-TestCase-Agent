def password_test_cases(requirement):
    return f"""
Requirement Category

Authentication - Password Reset

Priority

High

Risk Level

High

Reason

Password reset impacts account security. If this feature fails, users may lose access to their accounts or unauthorized users may gain access.

Functional Test Cases

1. Verify reset password email is sent successfully.
2. Verify user can click the reset password link.
3. Verify user can create a new password.
4. Verify user can log in with the new password.

Edge Cases

1. Expired reset password link.
2. Invalid reset token.
3. Multiple reset requests.
4. Password reuse attempt.

Negative Test Cases

1. Unregistered email address.
2. Invalid email format.
3. Empty email field.
4. Weak password submission.

Missing Requirements / Questions

1. How long should the reset link remain active?
2. Are password complexity rules required?
3. Should old passwords be blocked?
4. Should users receive a confirmation email?

Test Data Suggestions

1. Registered email.
2. Unregistered email.
3. Expired token.
4. Invalid token.

Requirement Received:

{requirement}
"""


def login_test_cases(requirement):
    return f"""
Requirement Category

Authentication - Login

Priority

High

Risk Level

High

Reason

Login impacts user access and authentication. If this feature fails, users may be unable to access their accounts or unauthorized users may gain access.

Functional Test Cases

1. Verify user can log in with valid credentials.
2. Verify successful navigation after login.
3. Verify session is created after login.
4. Verify logout functionality works correctly.

Edge Cases

1. Multiple failed login attempts.
2. Session timeout.
3. Login from multiple devices.
4. Browser refresh after login.

Negative Test Cases

1. Invalid username.
2. Invalid password.
3. Empty username field.
4. Empty password field.

Missing Requirements / Questions

1. Is Multi-Factor Authentication required?
2. What is the account lockout policy?
3. How long should the session remain active?

Test Data Suggestions

1. Valid user credentials.
2. Invalid user credentials.
3. Locked account.
4. Expired session.

Requirement Received:

{requirement}
"""


def registration_test_cases(requirement):
    return f"""
Requirement Category

User Management - Registration

Priority

Medium

Risk Level

Medium

Reason

Registration affects account creation and user onboarding. If this feature fails, new users may not be able to access the product.

Functional Test Cases

1. Verify a new user can successfully create an account with valid details.
2. Verify required fields are validated during registration.
3. Verify the user receives a successful account creation message.
4. Verify the user can log in after successful registration.

Edge Cases

1. Duplicate email address registration.
2. Very long name or email input.
3. Special characters in name fields.
4. Browser refresh during registration.

Negative Test Cases

1. Empty required fields.
2. Invalid email format.
3. Weak password.
4. Already registered email address.

Missing Requirements / Questions

1. What fields are mandatory for registration?
2. Are email verification steps required?
3. What password rules should be enforced?
4. Should duplicate accounts be blocked?
5. Is user consent required for terms and privacy policy?

Test Data Suggestions

1. Valid new user details.
2. Existing registered email.
3. Invalid email format.
4. Weak password.
5. Missing required fields.

Requirement Received:

{requirement}
"""


def shopping_cart_test_cases(requirement):
    return f"""
Requirement Category

E-commerce - Shopping Cart

Priority

Medium

Risk Level

Medium

Reason

Shopping cart functionality affects the purchase journey. If this feature fails, users may not be able to save products for checkout, which can impact sales.

Functional Test Cases

1. Verify user can add a product to the shopping cart successfully.
2. Verify cart item count updates after adding a product.
3. Verify product details in the cart match the selected product.
4. Verify user can remove a product from the cart.
5. Verify user can update product quantity in the cart.

Edge Cases

1. Adding the same product multiple times.
2. Adding a product with limited stock.
3. Updating quantity to the maximum allowed limit.
4. Refreshing the page after adding products to the cart.
5. Adding a product when the user is not logged in.

Negative Test Cases

1. Add an out-of-stock product to the cart.
2. Enter an invalid quantity.
3. Remove a product that is no longer available.
4. Add a product with missing price information.
5. Attempt cart update with expired session.

Missing Requirements / Questions

1. Should guest users be allowed to add products to the cart?
2. What is the maximum quantity allowed per product?
3. Should cart items be saved after logout?
4. How long should cart items remain saved?
5. Should users be notified when product price changes in the cart?

Test Data Suggestions

1. In-stock product.
2. Out-of-stock product.
3. Product with limited inventory.
4. Guest user.
5. Logged-in user.
6. Product with discount.
7. Product with changed price.

Requirement Received:

{requirement}
"""


def generic_test_cases(requirement):
    return f"""
Requirement Category

General Requirement

Priority

Medium

Risk Level

Medium

Reason

This requirement needs further analysis because the system could not identify a specific supported category.

Functional Test Cases

1. Verify that the user can successfully complete the requested action.
2. Verify valid input is accepted.
3. Verify expected output is generated.

Missing Requirements / Questions

1. What are the validation rules?
2. What error messages should be displayed?
3. Are there any security or access control rules?

Requirement Received:

{requirement}
"""


def generate_test_cases(requirement):

    requirement_lower = requirement.lower()

    if "password" in requirement_lower:
        return password_test_cases(requirement)

    if "login" in requirement_lower:
        return login_test_cases(requirement)

    if (
        "registration" in requirement_lower
        or "sign up" in requirement_lower
        or "signup" in requirement_lower
        or "create account" in requirement_lower
    ):
        return registration_test_cases(requirement)

    if (
        "cart" in requirement_lower
        or "shopping cart" in requirement_lower
        or "add products" in requirement_lower
        or "add product" in requirement_lower
    ):
        return shopping_cart_test_cases(requirement)

    return generic_test_cases(requirement)