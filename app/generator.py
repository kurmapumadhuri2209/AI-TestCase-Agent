def generate_test_cases(requirement):

    return f"""
Functional Test Cases

1. Verify the requirement is processed successfully.
2. Verify valid user input is accepted.
3. Verify expected output is generated.

Edge Cases

1. Empty input.
2. Very large input.
3. Special characters in input.

Negative Test Cases

1. Invalid input format.
2. Missing mandatory information.

Requirement Received:

{requirement}
"""