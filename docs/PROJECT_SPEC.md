# PROJECT: PROFESSIONAL PERSONAL FINANCE & SHARED BUDGET PLATFORM

> Note: We are building a reduced MVP first (see Roadmap in README.md). This document is the full long-term vision.

Искам да разработя професионално приложение за управление на лични и споделени финанси, което е предназначено да бъде реален търговски продукт, а не учебен проект.

Приложението трябва да бъде разработено така, че в бъдеще да може да бъде публикувано и продавано на реални потребители.

Основният език за backend/business logic трябва да бъде Python.

Не създавай просто демонстрационен desktop CRUD проект. Проектирайте системата като production-ready приложение с ясна архитектура, сигурност, database design, authentication, API, frontend, deployment и възможност за мащабиране.

---

## 1. ОСНОВНА ИДЕЯ

Приложението представлява Personal Finance Manager, чрез който потребителят може да:

* управлява приходи и разходи;
* следи банкови/парични сметки;
* създава месечни бюджети;
* поставя финансови цели;
* следи абонаменти и периодични разходи;
* вижда статистики и графики;
* получава автоматични финансови анализи;
* експортира информация;
* споделя бюджет с други хора;
* създава семейство/домакинство;
* определя роли и права;
* вижда кой потребител е направил даден разход;
* синхронизира данните между устройства.

Приложението трябва да бъде usable както от един човек, така и от семейство/двойка/съквартиранти.

---

## 2. ПРЕПОРЪЧИТЕЛЕН TECH STACK

**Backend:**

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Alembic

**Authentication:**

* JWT / secure session mechanism
* password hashing чрез bcrypt/Argon2
* email verification
* password reset
* optional 2FA

**Frontend:**

* модерен web frontend
* responsive дизайн
* desktop + mobile layout

За frontend може да бъде използван React + TypeScript.

**Charts:**

* Chart.js или Apache ECharts

**Background jobs:**

* Celery или подходящ Python task system

**Cache:**

* Redis

**Infrastructure:**

* Docker
* Docker Compose за development
* production-ready deployment configuration

**Testing:**

* pytest
* API tests
* integration tests

**Version control:**

* Git
* GitHub

**Документация:**

* OpenAPI
* README
* architecture documentation
* API documentation

---

## 3. АРХИТЕКТУРА

Използвай ясна многослойна архитектура:

```
Frontend
↓
REST API
↓
Authentication / Authorization
↓
Service Layer
↓
Repository / Data Access Layer
↓
PostgreSQL
```

Отделно:

```
Background Workers
↓
Redis
↓
Scheduled tasks / notifications / recurring transactions
```

Не смесвай UI, database queries и business logic в едни и същи файлове.

Проектът трябва да бъде структуриран така, че отделните компоненти да могат да се променят независимо.

---

## 4. USER ACCOUNT

Всеки потребител трябва да има:

* id
* first name
* last name
* email
* password hash
* profile picture
* currency
* timezone
* language
* created_at
* updated_at

Функции:

* Register
* Login
* Logout
* Email verification
* Forgot password
* Reset password
* Change password
* Edit profile
* Delete account
* Export personal data

Никога не съхранявай паролата като plain text.

---

## 5. DASHBOARD

След login потребителят вижда dashboard.

Показвай:

* текущ баланс;
* приходи за текущия месец;
* разходи за текущия месец;
* спестявания;
* бюджет;
* remaining budget;
* financial goals;
* upcoming bills;
* recurring payments;
* latest transactions.

Графики:

1. Income vs Expenses
2. Expenses by Category
3. Monthly Spending
4. Savings Progress
5. Budget Usage

Dashboard-ът трябва да бъде персонализиран според потребителя.

---

## 6. ACCOUNTS

Потребителят може да създава финансови сметки.

Например:

* Cash
* Bank Account
* Savings Account
* Credit Card
* Investment Account

Всеки account има:

* name
* type
* currency
* current balance
* description
* created_at

При добавяне на транзакция балансът трябва да се актуализира автоматично.

---

## 7. TRANSACTIONS

Основна функционалност.

Всяка транзакция:

* id
* user_id
* account_id
* type
* amount
* currency
* category
* description
* date
* notes
* attachment
* created_at
* updated_at

Типове:

* Income
* Expense
* Transfer

Функции:

* Add
* Edit
* Delete
* Search
* Filter
* Sort
* Pagination

Филтри:

* дата;
* категория;
* account;
* amount;
* transaction type;
* user.

---

## 8. CATEGORIES

Default категории:

* Food
* Transport
* Bills
* Shopping
* Entertainment
* Health
* Education
* Travel
* Subscriptions
* Housing
* Pets
* Other

Потребителят трябва да може:

* да създава категории;
* да редактира категории;
* да изтрива категории;
* да задава icon/color.

Категориите трябва да могат да бъдат различни за различни households.

---

## 9. BUDGETS

Потребителят може да създава бюджет. Например:

* Food: 500 EUR/month
* Entertainment: 150 EUR/month
* Transport: 100 EUR/month

Системата изчислява:

* Budget
* Spent
* Remaining
* Percentage Used

При достигане на определен процент:

* 80% → warning
* 100% → budget exceeded

Потребителят може да задава custom thresholds.

---

## 10. SHARED BUDGET / FAMILY

Това е една от основните функции на приложението.

Потребителят може да създаде HOUSEHOLD. Например: "The Vulkova Family".

След това може да покани:

* partner
* spouse
* parent
* child
* roommate

Поканата може да бъде чрез:

* email
* invitation link

---

## 11. HOUSEHOLD ROLES

Поддържай роли:

* OWNER
* ADMIN
* MEMBER
* VIEWER

Пример:

**Owner:**

* пълен контрол

**Admin:**

* управление на членове
* бюджети
* категории

**Member:**

* добавяне на транзакции
* виждане на общия бюджет

**Viewer:**

* само преглед

Permissions трябва да бъдат проверявани на backend, а не само във frontend.

---

## 12. SHARED TRANSACTIONS

При споделен бюджет всеки разход трябва да показва кой го е добавил.

Например:

* Maria — Groceries — €82.40
* Ivan — Electricity — €74.20

Трябва да има: "Added by Maria" или "Added by Ivan".

---

## 13. PRIVATE VS SHARED FINANCES

Много важна функционалност.

Потребителят трябва да може да има PRIVATE ACCOUNT и SHARED HOUSEHOLD ACCOUNT.

Например Maria има:

**Private:**

* Personal Savings
* Personal Cash

**Shared:**

* Family Account

Ivan не трябва да има достъп до private информацията на Maria.

Това трябва да бъде гарантирано от backend authorization.

---

## 14. SPLIT EXPENSES

При споделени бюджети трябва да има възможност за разделяне на разход.

Например Dinner: €100

* Maria: €50, Ivan: €50

Или:

* Maria: €70, Ivan: €30

Поддържай:

* equal split
* percentage split
* custom amount split

---

## 15. SETTLEMENTS

Системата може да изчислява кой на кого дължи пари.

Например:

* Maria paid: €300
* Ivan paid: €100

И системата показва: "Ivan owes Maria €100"

Трябва да има възможност да се маркира "Settled".

---

## 16. RECURRING TRANSACTIONS

Потребителят може да създава периодични транзакции. Например:

* Netflix — €15.99 — Every month
* Rent — €600 — Every month
* Salary — €2000 — Every month

Поддържай:

* daily
* weekly
* monthly
* yearly
* custom recurrence

Background worker трябва автоматично да създава транзакциите.

---

## 17. SUBSCRIPTIONS

Отделна секция: Subscriptions

Показвай:

* subscription name
* price
* billing period
* next payment
* category

Например:

* Netflix — €15.99
* Spotify — €10.99
* Gym — €30

Покажи:

* Monthly subscription cost
* Yearly subscription cost

Изпращай notification преди плащане.

---

## 18. FINANCIAL GOALS

Потребителят може да създава цели. Например "New Laptop":

* Target: €2,500
* Current: €1,340
* Progress: 53.6%

Поддържай:

* target amount
* current amount
* deadline
* monthly target
* description

---

## 19. ANALYTICS

Направи отделна Analytics секция.

Покажи:

* spending trends;
* income trends;
* savings rate;
* category distribution;
* monthly comparison;
* yearly comparison;
* biggest expenses;
* recurring expenses.

Потребителят трябва да може да избира:

* 7 days
* 30 days
* 3 months
* 6 months
* 1 year
* Custom

---

## 20. SMART INSIGHTS

Системата трябва да анализира данните и да генерира информативни insights. Например:

* "Your food expenses increased by 18% compared with last month."
* "Subscriptions represent €86.40 of your estimated monthly expenses."
* "Your average monthly spending over the last 6 months is €1,240."

Insights трябва да бъдат based on actual user data.

Не измисляй финансови факти.

---

## 21. NOTIFICATIONS

Notification system:

* budget exceeded
* budget near limit
* upcoming subscription
* upcoming recurring payment
* goal milestone
* household invitation
* expense added
* settlement reminder

Поддържай:

* in-app notifications
* email notifications

В бъдеще може да бъде добавено push notification.

---

## 22. ATTACHMENTS

При транзакция потребителят може да добави:

* receipt
* invoice
* photo
* PDF

Файловете трябва да бъдат съхранявани чрез cloud object storage, а не директно в PostgreSQL.

---

## 23. EXPORT

Потребителят трябва да може да експортира:

* CSV
* Excel
* PDF

Филтри:

* date range
* category
* account
* household
* transaction type

---

## 24. IMPORT

Позволи import на CSV.

Например банков CSV с колони: Date, Description, Amount, Category.

Добави mapping interface, така че потребителят да избере коя колона какво представлява.

---

## 25. SEARCH

Global search: потребителят пише "Netflix" и получава всички съответни:

* transactions
* subscriptions
* categories

---

## 26. MULTI-CURRENCY

Поддържай различни валути. Например:

* EUR
* USD
* GBP
* BGN

Всеки account може да има собствена валута.

При нужда приложението използва exchange rates.

Съхранявай оригиналната сума и валута.

Не променяй исторически транзакции само защото exchange rate се е променил.

---

## 27. SECURITY

Security трябва да бъде основен приоритет.

Изисквания:

* secure password hashing
* JWT/session security
* HTTPS
* input validation
* SQL injection protection
* XSS protection
* CSRF protection where applicable
* rate limiting
* secure cookies
* authorization checks
* file upload validation
* maximum file size
* audit logging

Никога не поставяй secret keys директно в GitHub.

Използвай .env и environment variables.

---

## 28. AUDIT LOG

За household действията създай audit log. Например:

* Maria added expense €80
* Ivan changed budget Food from €400 to €500
* Maria invited Ivan
* Ivan deleted transaction

Owner/Admin трябва да може да вижда audit history.

---

## 29. DATABASE

Използвай PostgreSQL.

Създай нормализирана relational database.

Основни таблици:

* users
* households
* household_members
* accounts
* categories
* transactions
* transaction_splits
* budgets
* budget_categories
* financial_goals
* subscriptions
* recurring_transactions
* notifications
* attachments
* audit_logs
* invitations

Използвай foreign keys, indexes и appropriate constraints.

Използвай Alembic migrations.

---

## 30. API

Backend API трябва да бъде RESTful. Например:

```
POST /auth/register
POST /auth/login
POST /auth/logout

GET /users/me

GET /accounts
POST /accounts

GET /transactions
POST /transactions
PUT /transactions/{id}
DELETE /transactions/{id}

GET /budgets
POST /budgets

GET /analytics

GET /households
POST /households

POST /households/{id}/invite

GET /households/{id}/members

POST /transactions/{id}/split

GET /notifications
```

API трябва да бъде documented чрез OpenAPI/Swagger.

---

## 31. FRONTEND UX

Интерфейсът трябва да изглежда като реален SaaS продукт.

Не използвай default HTML forms.

Използвай:

* responsive layout
* sidebar navigation
* cards
* tables
* charts
* modals
* confirmation dialogs
* loading states
* empty states
* error states
* success notifications
* skeleton loading where appropriate

Основна навигация:

* Dashboard
* Transactions
* Accounts
* Budgets
* Goals
* Subscriptions
* Analytics
* Household
* Notifications
* Settings

---

## 32. ONBOARDING

При първото стартиране:

```
Welcome
↓
Create account
↓
Choose currency
↓
Create first account
↓
Set monthly budget
↓
Optional: create household
↓
Dashboard
```

Направи onboarding-а кратък и лесен.

---

## 33. PRICING / MONETIZATION

Проектирайте продукта така, че да може да има: FREE, PREMIUM, FAMILY.

Примерно:

**FREE:**

* basic transactions
* basic budgets
* basic analytics

**PREMIUM:**

* unlimited budgets
* advanced analytics
* financial goals
* recurring transactions
* exports
* advanced insights

**FAMILY:**

* shared household
* multiple members
* split expenses
* settlements
* household analytics

Не hardcode-вай subscription logic във frontend.

Subscription status трябва да се управлява от backend.

Плащанията могат да бъдат интегрирани по-късно чрез Stripe.

---

## 34. ADMIN PANEL

Създай отделен admin interface.

Admin може да вижда:

* users
* households
* subscriptions
* system statistics
* reports
* errors
* audit events

Admin никога не трябва да има достъп до plaintext passwords.

---

## 35. TESTING

Напиши tests за:

* Authentication
* Authorization
* Transactions
* Budgets
* Households
* Permissions
* Splitting
* Recurring transactions
* Analytics

Минимум:

* unit tests
* integration tests
* API tests

Добави CI pipeline, който автоматично стартира tests при push към GitHub.

---

## 36. DOCKER

Създай Docker environment.

Services:

* frontend
* backend
* postgres
* redis

Development трябва да може да се стартира например с `docker compose up`.

---

## 37. DEPLOYMENT

Проектът трябва да бъде подготвен за production deployment.

Не искам приложението да работи само на моя компютър.

Подготви:

* production environment variables
* Docker images
* database migrations
* HTTPS
* logging
* backups
* health checks
* error handling

---

## 38. BACKUPS

PostgreSQL трябва да има автоматични backups.

Документирай:

* backup frequency
* retention
* restore procedure

---

## 39. GDPR / PRIVACY

Тъй като приложението ще обработва финансови данни, трябва да бъде проектирано с privacy/security mindset.

Добави:

* Privacy Policy placeholder
* Terms of Service placeholder
* account deletion
* personal data export
* data minimization
* consent management where required

Не събирай ненужни лични данни.

---

## 40. ERROR HANDLING

Никога не показвай stack trace на крайния потребител.

Потребителят трябва да получава: "Something went wrong. Please try again."

Developer logs трябва да съдържат подробната информация.

---

## 41. OBSERVABILITY

Добави production logging.

Следи:

* errors
* failed requests
* authentication failures
* background job failures
* database errors

Подготви проекта за бъдеща интеграция със система за error monitoring.

---

## 42. PERFORMANCE

Приложението трябва да използва:

* database indexes
* pagination
* caching where appropriate
* efficient queries
* lazy loading
* background processing

Не зареждай всички транзакции на потребителя наведнъж.

---

## 43. GITHUB

Repository-то трябва да изглежда професионално.

Структура:

```
README.md
LICENSE
.env.example
.gitignore
docker-compose.yml

/backend
/frontend
/tests
/docs
```

README трябва да съдържа:

* Project overview
* Features
* Architecture
* Tech stack
* Installation
* Environment variables
* Database setup
* Running locally
* Running tests
* Docker
* Deployment
* Screenshots
* Roadmap

---

## 44. DEVELOPMENT PROCESS

Не създавай всичко наведнъж.

Разработката трябва да бъде разделена на milestones.

1. Project architecture, Git, Docker, Database, FastAPI, Frontend
2. Authentication
3. Accounts + Transactions
4. Categories + Budgets
5. Dashboard + Analytics
6. Recurring transactions + Subscriptions
7. Financial goals
8. Households + invitations + roles
9. Split expenses + settlements
10. Notifications
11. Import / Export
12. Security hardening
13. Testing + CI/CD
14. Production deployment
15. Payments / Premium plans
16. Final polish + documentation

---

## 45. IMPORTANT DEVELOPMENT RULE

Не генерирай огромно количество код наведнъж.

За всяка стъпка:

1. Обясни какво ще изградим.
2. Покажи структурата на файловете.
3. Създай необходимите файлове.
4. Дай пълния код.
5. Обясни къде да бъде поставен.
6. Покажи как да се стартира.
7. Тествай функционалността.
8. Провери за грешки.
9. Едва след това премини към следващата стъпка.

Ако дадена архитектурна промяна изисква промяна в предишен код, посочи точно кои файлове трябва да бъдат променени.

Не оставяй pseudo-code или TODO вместо реална имплементация, освен когато функционалността умишлено е планирана за по-късен milestone.

---

## 46. QUALITY STANDARD

Целта не е: "Да изглежда като студентски проект."

Целта е: "Да изглежда като MVP на реален SaaS продукт."

Кодът трябва да бъде:

* clean
* maintainable
* modular
* secure
* testable
* documented
* scalable

Интерфейсът трябва да бъде:

* modern
* intuitive
* responsive
* consistent
* accessible

---

## 47. FINAL PRODUCT

Крайният продукт трябва да позволява на един човек да управлява личните си финанси и на семейство/група да управлява общ бюджет.

Примерен сценарий:

```
Maria създава акаунт.
↓
Добавя банковата си сметка.
↓
Добавя приходи.
↓
Добавя месечен бюджет.
↓
Създава household "Maria & Ivan".
↓
Кани Ivan.
↓
Ivan приема поканата.
↓
Двамата виждат общия бюджет.
↓
Maria плаща €100 за хранителни покупки.
↓
Добавя разхода.
↓
Ivan го вижда.
↓
Следващия път Ivan добавя €80.
↓
Системата изчислява split/settlement.
↓
Dashboard показва общите разходи.
↓
Analytics показва къде отиват парите.
↓
Системата предупреждава, че Food budget е достигнал 80%.
↓
В края на месеца Maria експортира финансовия отчет.
```

Това трябва да бъде цялостен, последователен продукт.

---

## 48. STARTING POINT

Започни от:

1. Final architecture
2. Technology decisions
3. Database ERD
4. Folder structure
5. Development roadmap
6. Git repository setup
7. Docker development environment
8. PostgreSQL setup
9. FastAPI backend skeleton
10. React frontend skeleton

Не започвай директно с Dashboard.

Първо създай стабилна основа.

Във всеки етап обяснявай защо е направен даден архитектурен избор и как той ще помогне приложението да бъде production-ready.
