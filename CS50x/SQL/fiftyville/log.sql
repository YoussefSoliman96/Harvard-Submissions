-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";
SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time –
each of their interview transcripts mentions the bakery. |
Littering took place at 16:36. No known witnesses.

SELECT name FROM people WHERE license_plate = (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10); --> Brandon

SELECT id FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_account.account_number;
WHERE people.name = "Brandon"