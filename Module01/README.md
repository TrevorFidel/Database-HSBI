# Module 1 - Introduction to Databases.
This page includes my notes for Module 1 and proof for the HSBI Database course.

# Learning Goals

By the end of the Module, you can:

Explain how this class works — the CBL/PBL philosophy, the portfolio-based project work assessment, and the "moving bar" of a first-time course.

Set up your personal GitHub portfolio from the course template, with a clean first commit and a .gitignore that keeps databases and secrets out of Git.

Set up the entire toolchain reproducibly with uv — one fixed Python plus SQLite, DuckDB, Datasette, and more — on Windows, macOS, or Linux, and verify it.

Explain — with a measurement, not a slide — the difference between an embedded database and a client/server database, and why most local apps should not run a server.

Load real rows into SQLite and query them from Python using bound parameters.

Take a first LLM-generated query, run it, and begin the habit that defines this course: verify before you trust.


> 

Module description

## Task Inspirations

- Inspiration 1
- Inspiration 2

## Task Personal Profile

Name: Nyongesa, Trevor Fidel.
Age:  22
Nationality: Kenyan.
Programming experience: I have   interracted with Kotlin, pyton, CPP and Javascript.For android apps and website development.I currently don't have any previous MCU knowledge but very eager to learn and get the knowledge. From the course i would want to navigate around databases and SQL. I find data a very crucial aspect in our life that with the correct data alot can be done.

## Task What is IoT
IoT(Internet of Things) -> physical devices connected to the internet and they collects,sends and recieve data.


Domains and included areas:
 Dormain is where IoT technology is used.

-Smart Home -> smartlocks,security cameras.
 
 -Healthcare -> smartwatch,wearable health monitors.
 
 -Environment -> Weather stations,Air quality sensors.


Commonly used (data) protocols:

-HTTP/HTTPS
-WI-FI

Typical devices (appliance or micro controller):

-Devices: sensors, smart appliances, GPS modules
-Microcontrollers: ESP32,Arduino boards,ESP8266.

Challenges:

-Security
-Privacy
## Task 7 cloud cost explanation
Running this telemetry dataset in the cloud could incur storage, computing, and data-transfer costs. The machine-shop business would normally pay these costs because it benefits from monitoring equipment, detecting bearing wear, and preventing expensive machine failures. SQLite avoids the cost of a dedicated database server for this small, local dataset, although computer hardware, storage, and backups still have costs.

## LLM explanation
I asked ChatGPT to generate a SQL query that calculates the average spindle load for each machine using readings taken after 18:00. The query executed successfully and returned one average per machine, ordered from highest to lowest. The execution plan helps me understand whether SQLite scans the readings table. I also tested the risk of using `LIKE '%18%'` instead of a proper time filter, because matching text anywhere in a timestamp can include readings that do not meet the intended time condition. This task showed me that LLM-generated SQL can be useful, but I must run it, inspect its execution plan, and test possible mistakes before trusting the results.

## Reflection 1
[Reflection 1](/Reflections/ref01.md)
