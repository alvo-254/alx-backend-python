📁 0x03. Unittests and Integration Tests
This project covers writing unit and integration tests in Python using the unittest framework, mock, and parameterized. It is part of the ALX Backend Specialization.

🧠 Learning Objectives
By the end of this project, you should be able to:

Explain the difference between unit and integration tests

Apply mocking, parameterization, and fixtures in tests

Understand and use unittest, unittest.mock, and parameterized

Write tests for:

Function outputs

Exception raising

Class methods

Decorators

HTTP requests (mocked)

Test with fixtures and patch network/database calls

🛠️ Requirements
Ubuntu 18.04 LTS

Python 3.7+

Code must follow pycodestyle (PEP8) style

All Python files must be executable and include:

Shebang line: #!/usr/bin/env python3

Module, class, and function docstrings

Type annotations

📚 Project Structure
Copy
Edit
.
├── README.md
├── client.py
├── fixtures.py
├── test_client.py
├── test_utils.py
├── utils.py
📋 Tasks Summary
Task	Description
0	Unit test access_nested_map with @parameterized.expand
1	Test access_nested_map raises KeyError on invalid path
2	Test get_json using unittest.mock.patch
3	Test memoize decorator only calls underlying method once
4	Test GithubOrgClient.org with @patch and @parameterized.expand
5	Test _public_repos_url property using patch and memoization
6	Unit test public_repos() with mock data
7	Parametrize test for has_license()
8	Integration test with fixtures and @parameterized_class
9	Integration test for public_repos with license filter

▶️ How to Run Tests
To run any test file:

bash
Copy
Edit
python3 -m unittest test_utils.py
python3 -m unittest test_client.py
✅ Dependencies
Install parameterized if not already installed:

bash
Copy
Edit
pip install parameterized
