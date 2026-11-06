# OOP1_Assignment1
# Vaccination Tracker (PROG211 – OOP 1)

A small, open-source Python program that tracks vaccination progress using
Object-Oriented Programming. Domain: **Health – Vaccination Tracker**.

## Features
- `Vaccine` class: name, number of doses, gap between doses (tuple).
- `VaccinationRecord` class: anonymous ID, age group, district, doses received.
- Links objects together: each record uses its `Vaccine` to work out the next due date.
- Stores all records in **one dictionary** (`record_id -> object`).
- `add_record()` and `display_records()` functions.

## OOP concepts used
| Requirement | Where |
|---|---|
| Two classes with attributes and methods | `Vaccine`, `VaccinationRecord` |
| Object creation and interaction | `main()`; a record holds a `Vaccine` object |
| Data structure (dictionary) | `records = {}` in `main()` |
| Instance methods | `administer_dose()`, `next_due_date()`, `status()`, `display_info()`, `describe()` |
| Class methods (`@classmethod`) | `total_records()`, `with_first_dose()` |
| Static method (`@staticmethod`) | `is_valid_age_group()` |
| Tuples (optional bonus) | `Vaccine.interval_days`, `VaccinationRecord.AGE_GROUPS` |

## How it meets Digital Public Goods (DPG) standards
- **Open-source:** the code is published in a public GitHub repository.
- **Inclusive and accessible:** plain-text console output, simple English, no special hardware or internet needed, and it runs on any computer with Python 3.
- **Privacy-respecting:** no names, phone numbers or addresses are stored. Each record has a system-generated anonymous ID (e.g. `VT-0001`), an age group and a district only.
- **Modular and reusable:** each class has one job, and the functions are separate from the classes, so other health programs can reuse `Vaccine` and `VaccinationRecord` for any vaccine.

## How to run
```
python vaccination_tracker.py
```
Requires Python 3.8+. No external libraries.

## Example output
See `sample_output.txt`:
```
Added VT-0001
VT-0001: dose 1/2 recorded on 2026-09-05.
...
ID: VT-0002 | Vaccine: Polio (3-dose) | Age group: 0-5 | District: Bo
    Doses: 2/3 | Status: In progress (next due 2026-10-31)
Total records created: 3
```

## Submission checklist
1. Create a public GitHub repository and upload these files.
2. Add your lecturer (amandus.bcoker@limkokwing.edu.sl) as a collaborator.
3. Print the hardcopy with screenshots (Tahoma, size 10, 1.15 spacing, justified).
