# DA108 | Lab 03 Assignment

### Python Assignment: [Password Strength Checker with Feedback Loop](Password_Strength_Checker.py)

Implement a **password strength checker** that evaluates a given password while reinforcing the
understanding of fundamental **data types** like **int, float, bool, string, and list**. The program should
provide real-time feedback and allow users to **retry** until they create a strong password.

## To-Do List

1. Take User Input (String Handling)
    - Prompt the user to enter a **password**.
    - Store the password as a **string** and analyze its properties (length, character types, etc.).

2. Check Password Strength Using Different Data Types
    - Use Boolean Variables (`bool`) to check:
        - Presence of **uppercase** and **lowercase** letters.
        - Inclusion of **numbers** (`0-9`).
        - Inclusion of **special characters** (`@, #, $, etc.`).
    - Use Integers (`int`) to:
        - Store the password **length** and compare it against strength thresholds.
        - Count the occurrences of each character type.
    - Use Lists (`list`) to:
        - Store sets of **character categories** (letters, numbers, special characters).
        - Maintain a **history of previously entered passwords**.

3. Categorize Password Strength & Provide Feedback (Feedback Loop)
    - Categorize passwords into **"Weak"**, **"Medium"**, or **"Strong"** based on (use **if** statement):
        - **"Weak"** → Less than **6 characters**.
        - **"Medium"** → Contains letters and numbers but lacks special characters.
        - **"Strong"** → Has **uppercase, lowercase, numbers, and special characters**.
    - **Feedback Loop** (use **while** statement):
        - If the password is **"Weak"**, prompt the user to try again.
        - If **"Medium"**, suggest adding special characters.
        - If **"Strong"**, congratulate the user.
        - Continue prompting until the user enters a **"Strong"** password.

---

## Example Test Cases

Input: "hello"

Output: "Weak password. Try using numbers and special characters."

Input: "hello123"

Output: "Medium password. Try adding a special character for a stronger password."

Input: "Hello@123"

Output: "Strong password! Great job!"

---

## Key Learning Outcomes

- **String manipulation** (checking characters, slicing, etc.).
- **Boolean (`bool`)** for validation conditions.
- **Using Lists (`list`)** for storing history.
- **Using Integers (`int`) & Floats (`float`**) for calculations.
- **Loops & Conditional Statements** to guide user interaction.
---

## Submission Guidelines
- Create .py file
- Add **comments** explaining how each data type is used.
- Ensure your code is **efficient, well-structured, and readable**.