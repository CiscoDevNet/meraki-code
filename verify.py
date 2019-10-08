#!/usr/bin/env python
"""Verify the Meraki APIs are accessible and responding.



Copyright (c) 2018 Cisco and/or its affiliates.

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

import requests
import sys, os

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))

# Get the absolute path for the project / repository root
project_root = os.path.abspath(os.path.join(here, ".."))

# Extend the system path to include the project root and import the env files
sys.path.insert(0, project_root)
import env_user  # noqa

def verify() -> bool:
    """Meraki APIs"""
    print("==> Verifying access to the Meraki APIs")



    # Verify the Spark Room exists and is accessible via the access token
    try:
        r = requests.get(
            "https://api.meraki.com/api/v0/organizations",
            headers={
                "X-Cisco-Meraki-API-Key": env_user.MERAKI_API_KEY,
                "Content-Type": "application/json"
            }
        )
        print(r.status_code)
        if r.status_code == 200:
            print("Meraki connectivity verified")
        else:
            print("There is an issue connecting to the Meraki platform.  Please check the API Key")
        print()
    except:
        print("Unable to contact Meraki cloud")
        return False


    return True


if __name__ == '__main__':
    verify()
