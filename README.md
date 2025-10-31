
---

# Test Strategy – Demoblaze Web Application

## Objective
To validate the **functional, API, performance, and usability** aspects of the [Demoblaze](https://www.demoblaze.com/) web application — ensuring all major workflows like **Signup, Login, Add to Cart, and Checkout** function correctly across environments.

---

## Scope

**In-Scope**
- Functional testing using Selenium (Python)
- API testing via Postman
- Manual test coverage for UI and validation
- Performance testing using Locust
- Mobile responsiveness and accessibility testing

**Out-of-Scope**
- Backend database verification
- Payment gateway integration
- Email/SMS notifications

---

## Test Approach

### 1. **Automation Testing (Selenium + Python)**
- Covers end-to-end user journey: **Signup → Login → Product Selection → Checkout**
- Uses Faker for random user data
- Captures screenshot after successful checkout
- Includes alert handling, explicit waits, and dynamic element handling

### 2. **API Testing (Postman)**
- API tests executed in **Postman**, verifying key endpoints:
  - `POST /view` → Fetch all products  
  - `POST /viewitem` → Get details of a single product  
  - `POST /addtocart` → Add selected product to cart  
  - `POST /deleteitem` → Remove a specific product from cart  
  - `POST /deletecart` → Clear cart after checkout  
- Tested for positive, negative, and boundary cases  
- Assertions included for response status, body, and message structure

### 3. **Manual Testing**
- Conducted using detailed Excel sheets
- Focused on UI validation, field behavior, and boundary testing
- Includes positive, negative, and exploratory test cases

### 4. **Performance Testing (Locust)**
- Simulated user load of 10–20 concurrent users
- Measured:
  - Average response time  
  - Requests per second (RPS)  
  - Failure rate  
- Target: Stable response and no API errors under moderate load

### 5. **Mobile Testing**
- Tested on Chrome DevTools for responsiveness
- Verified layout, navigation, and usability on various resolutions
- Checked accessibility features (font scaling, TalkBack, color contrast)

---

## ⚙️ Environment

- **Browser:** Google Chrome v129  
- **OS:** Windows 10  
- **Python:** 3.10  
- **Selenium:** 4.25  
- **Tools:** Faker, Locust, Postman, Excel  

---

## 🧾 Deliverables

- Automation script → `automation/demoblaze_checkout_test.py`  
- Performance script → `performance/locust_test.py`  
- Manual test cases → `manual_testcases/demoblaze_manual_testcases.xlsx`  
- API test cases → `api_testcases/demoblaze_api_testcases.xlsx`  
- Improvement suggestions → `docs/improvement_suggestions.md`  
- Screenshot → `reports/checkout_success.png`

---

## Success Criteria

- All critical test cases executed and passed  
- Checkout flow completed successfully end-to-end  
- No major functional or UI issues remain open  
- API and performance results within acceptable limits  

---


## Description of Files and Folders

### automation/
Contains Selenium-based UI automation scripts.

- **demoblaze_checkout_test.py**  
  Automates the full end-to-end user flow:
  - Signup (using Faker-generated credentials)  
  - Login  
  - Product selection by category  
  - Add to cart  
  - Checkout and purchase confirmation  
  - Captures a screenshot after successful checkout  
  If the user doesn’t enter any input, defaults are used:
  - Category → `Phones`  
  - Product → `Samsung galaxy s6`

---

### performance/
Contains load testing scripts written using **Locust**.

- **locust_test.py**  
  Simulates multiple concurrent users performing actions like browsing products and checking out, to evaluate:
  - Response time  
  - Throughput (Requests Per Second)  
  - Failure rate  

---

### manual_testcases/
Contains documented manual test cases.

- **demoblaze_manual_testcases.xlsx**  
  Covers UI, functional, and boundary test cases for core modules such as:
  - Login  
  - Signup  
  - Product listing  
  - Add to cart  
  - Checkout  
  - Logout  

---

### api_testcases/
Contains API-level test cases for the Demoblaze backend.

- **demoblaze_api_testcases.xlsx**  
  Includes detailed test cases for:
  - **GET /products** — fetch product list  
  - **POST /cart** — add product to cart  
  - **POST /checkout** — place order  
  - **DELETE /deletecart** — clear cart  

---

### docs/
Contains supporting documentation and recommendations.

- **mobile_testing.docx**  
  Describes mobile testing scope, device coverage, network conditions (Wi-Fi, 4G, offline), and accessibility testing (TalkBack, VoiceOver).

- **performance_testing.docx**  
  Documents load test objectives, execution plan, KPIs (Response Time, RPS, Failures), and results summary.

- **improvement_suggestions.docx**  
  The final curated suggestion document combining functional, UI, and validation improvements with short, actionable recommendations.

---

### reports/
Stores test evidence like screenshots and logs.

- **checkout_success.png**  
  Screenshot captured automatically after successful checkout via automation script.

---

### requirements.txt
Lists all required Python dependencies for automation and performance testing.

# Demoblaze Automation Script (Selenium + Python)

This project automates the **end-to-end checkout flow** on the [Demoblaze](https://www.demoblaze.com/) website using **Selenium WebDriver (Python)**.

It covers:
- **Signup** with dynamically generated credentials  
- **Login** with the same user  
- **Product selection** by category  
- **Add to Cart** and **Checkout flow**  
- **Purchase confirmation** and **screenshot capture**

---

## ⚙️ Prerequisites / Requirements

### System Requirements
- Python **3.8+**
- Google Chrome (latest version)
- ChromeDriver (matching your Chrome version)
- Stable internet connection

### Python Packages
Install all required libraries using:

```bash
pip install -r requirements.txt


