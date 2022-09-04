from behave import given, when, then
from simple_calculator import add, subtract, multiply, divide

@given(u'Relevant Function is executed')
def step_impl(context):
    pass

@when(u'I input "{num1}" and "{num2}" to add function')
def step_impl(context, num1, num2):
    context.result = add(int(num1), int(num2))

@then(u'I get "{out}" as a result')
def step_impl(context, out):
    assert context.result == int(out), 'Expected {}, got {}'.format(out, context.result)

