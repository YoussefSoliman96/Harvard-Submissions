-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";
SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time
 each of their interview transcripts mentions the bakery. Littering took place at 16:36. No known witnesses.

SELECT name FROM people WHERE license_plate = (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10); --> Brandon

SELECT id FROM people WHERE name = "Brandon" --> Brandon id
SELECT passport_number FROM people WHERE name = "Brandon" --> Brandon passport number
SELECT account_number FROM bank_accounts WHERE person_id = (SELECT id FROM people WHERE name = "Brandon") --> Brandon account number
SELECT flight_id FROM passengers WHERE passport_number = (SELECT passport_number FROM people WHERE name = "Brandon") --> Brandon passport number)
SELECT day, month, year FROM flights WHERE id in (SELECT flight_id FROM passengers WHERE passport_number = (SELECT passport_number FROM people WHERE name = "Brandon")) --> Brandon took a flight the next day 29/7
SELECT id FROM flights WHERE day = 29; --> Flight id = 23
SELECT destination_airport_id FROM flights WHERE id = 23 -- > Destination id = 11
SELECT city FROM airports WHERE id = 11 --> San Francisco
SELECT phone_number FROM people WHERE name = "Brandon" --> Brandon (771) 555-6667
SELECT receiver,  FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND caller = "(771) 555-6667";

SELECT * FROM atm_transactions WHERE account_number = (SELECT account_number FROM bank_accounts WHERE person_id = (SELECT id FROM people WHERE name = "Brandon")) AND month = 7 AND day = 28
SELECT * FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = "Leggett Street";