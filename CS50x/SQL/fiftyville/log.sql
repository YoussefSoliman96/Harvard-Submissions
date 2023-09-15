-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";
SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time
 each of their interview transcripts mentions the bakery. Littering took place at 16:36. No known witnesses.

SELECT name FROM people WHERE license_plate in (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10); --> Thomas

SELECT id FROM people WHERE name = "Thomas" --> Thomas id 660982
SELECT passport_number FROM people WHERE name = "Thomas" --> Thomas passport number
SELECT account_number FROM bank_accounts WHERE person_id = (SELECT id FROM people WHERE name = "Thomas") --> Thomas account number
SELECT flight_id FROM passengers WHERE passport_number = (SELECT passport_number FROM people WHERE name = "Thomas") --> Thomas passport number)
SELECT day, month, year FROM flights WHERE id in (SELECT flight_id FROM passengers WHERE passport_number = (SELECT passport_number FROM people WHERE name = "Thomas")) --> Thomas took a flight the next day 29/7
SELECT id FROM flights WHERE day = 29; --> Flight id = 23
SELECT destination_airport_id FROM flights WHERE id = 23 -- > Destination id = 11
SELECT city FROM airports WHERE id = 11 --> San Francisco
SELECT phone_number FROM people WHERE name = "Thomas" --> Thomas (771) 555-6667
SELECT receiver, day FROM phone_calls WHERE caller = "(771) 555-6667";
SELECT name FROM people WHERE phone_number = "(918) 555-5327";
SELECT caller FROM phone_calls WHERE receiver = "(918) 555-5327" and day = 28;

SELECT * FROM atm_transactions WHERE account_number = (SELECT account_number FROM bank_accounts WHERE person_id = (SELECT id FROM people WHERE name = "Thomas")) AND month = 7 AND day = 28
SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street"; --> 76054385 ACCOUNT NUMBER OF RECEIVER

SELECT name FROM people WHERE id = (SELECT person_id FROM bank_accounts WHERE account_number = 76054385) --> Taylor
SELECT phone_number FROM people WHERE name = "Taylor"
SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = "Taylor")

SELECT * FROM atm_transactions WHERE account_number = 76054385;