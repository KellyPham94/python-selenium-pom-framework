# Web Automated Testing Framework (Python + Selenium + Pytest)

An automated testing project demonstrating a transition from **Manual Testing Mindset** to **Automation Test Execution**. Built using Python, Selenium WebDriver, and Pytest following the **Page Object Model (POM)** design pattern.

---

## 📌 Test Planning & Test Cases (Manual Mindset)

Before automating, test scenarios were mapped to cover functional validity, edge cases, and basic security inputs (XSS validation).

| Test Case ID | Scenario | Input Data | Expected Result |
| :--- | :--- | :--- | :--- |
| **TC_01** | Valid Login | `student` / `Password123` | Redirected to success page (`/logged-in-successfully/`) |
| **TC_02** | Invalid Username | `incorrectUser` / `Password123` | Error message displayed on UI |
| **TC_03** | Invalid Password | `student` / `incorrectPassword` | Error message displayed on UI |
| **TC_04** | Security Input (XSS) | `<script>alert('XSS')</script>` | Input handled safely without alert execution |
| **TC_05** | Security Input (SQLi) | `' OR '1' = '1` | Login fails, no unauthorized access |


---

## 🛠️ Framework Highlights & Architecture

- **Page Object Model (POM):** Clean separation between page elements (`pages/`) and test scenarios (`tests/`).
- **Data-Driven Testing (DDT):** Efficient test coverage using Pytest's `@pytest.mark.parametrize`.
- **Automated Lifecycle Management:** Clean browser setup and teardown using `conftest.py` fixtures.
- **Automated HTML Reporting:** Generates clean test execution reports using pytest-html.

---

## 🚀 How to Run the Tests

1. **Clone the repository:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd <YOUR_PROJECT_FOLDER>
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Execute tests and generate HTML report:**
   ```bash
   pytest test_login_pom.py
   --html=report.html
   --self-contained-html
   

