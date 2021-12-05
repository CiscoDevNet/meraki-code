#!/usr/bin/env python
"""Demonstrate module vs. locally scoped variables.

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


# Create a module variable
module_variable = "I am a module variable."


# Define a function that expects to receive a value for an argument variable
def my_function(argument_variable):
    """Showing how module, argument, and local variables are used."""
    # Create a local variable
    local_variable = "I am a local variable."

    print(module_variable, "...and I can be accessed inside a function.")
    print(argument_variable, "...and I can be passed to a function.")
    print(local_variable, "...and I can ONLY be accessed inside a function.")


# Call the function; supplying the value for the argument variable
my_function(argument_variable="I am a argument variable.")


# Let's try accessing that local variable here at module scope
print("\nTrying to access local_variable outside of its function...")
try:
    print(local_variable)
except NameError as error:
    print(error)
