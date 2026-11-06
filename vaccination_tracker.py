"""
Vaccination Tracker - PROG211 Object-Oriented Programming 1 Assignment
Domain  : Health (Vaccination Tracker)
Concepts: Classes/objects (Task 1), dictionary data structure (Task 2),
          instance, class and static methods (Task 3), DPG alignment.

DPG note: no names or personal identifiers are stored. Each record uses an
anonymous ID, an age group and a district only.
"""
from datetime import date, timedelta


# ---------------------------------------------------------------- Class 1
class Vaccine:
    """A vaccine and its dosing schedule."""

    def __init__(self, name, doses_required, interval_days):
        self.name = name
        self.doses_required = doses_required
        # Tuple: the schedule is fixed and should not be changed (bonus use).
        # interval_days[i] = days to wait after dose i+1 before dose i+2.
        self.interval_days = tuple(interval_days)

    def describe(self):
        """Instance method: print a summary of the vaccine."""
        print(f"Vaccine: {self.name} | Doses: {self.doses_required} | "
              f"Gaps (days): {self.interval_days}")

    def gap_after_dose(self, dose_number):
        """Instance method: days to wait after the given dose number."""
        return self.interval_days[dose_number - 1]


# ---------------------------------------------------------------- Class 2
class VaccinationRecord:
    """An anonymous vaccination record linked to a Vaccine object."""

    AGE_GROUPS = ("0-5", "6-17", "18-49", "50+")   # tuple of allowed values
    _total_records = 0                              # class attribute

    def __init__(self, vaccine, age_group, district):
        if not self.is_valid_age_group(age_group):
            raise ValueError(f"Age group must be one of {self.AGE_GROUPS}")
        VaccinationRecord._total_records += 1
        self.record_id = f"VT-{VaccinationRecord._total_records:04d}"  # anonymous
        self.vaccine = vaccine          # interaction between objects
        self.age_group = age_group
        self.district = district
        self.doses_received = 0
        self.last_dose_date = None

    # ---- instance methods
    def administer_dose(self, dose_date=None):
        """Record one dose. Updates the record."""
        if self.is_complete():
            return f"{self.record_id}: already fully vaccinated."
        self.doses_received += 1
        self.last_dose_date = dose_date or date.today()
        return (f"{self.record_id}: dose {self.doses_received}/"
                f"{self.vaccine.doses_required} recorded on {self.last_dose_date}.")

    def is_complete(self):
        return self.doses_received >= self.vaccine.doses_required

    def next_due_date(self):
        """Return the date of the next dose, or None if not applicable."""
        if self.doses_received == 0 or self.is_complete():
            return None
        gap = self.vaccine.gap_after_dose(self.doses_received)
        return self.last_dose_date + timedelta(days=gap)

    def status(self):
        if self.is_complete():
            return "Fully vaccinated"
        if self.doses_received == 0:
            return "Not started"
        return f"In progress (next due {self.next_due_date()})"

    def display_info(self):
        print(f"ID: {self.record_id} | Vaccine: {self.vaccine.name} | "
              f"Age group: {self.age_group} | District: {self.district}\n"
              f"    Doses: {self.doses_received}/{self.vaccine.doses_required} "
              f"| Status: {self.status()}")

    # ---- class methods
    @classmethod
    def total_records(cls):
        """Class method: number of records created so far."""
        return cls._total_records

    @classmethod
    def with_first_dose(cls, vaccine, age_group, district, dose_date):
        """Class method used as an alternative constructor."""
        record = cls(vaccine, age_group, district)
        record.administer_dose(dose_date)
        return record

    # ---- static method
    @staticmethod
    def is_valid_age_group(age_group):
        """Static method: needs neither the object nor the class."""
        return age_group in VaccinationRecord.AGE_GROUPS


# ------------------------------------------- Task 2: dictionary functions
def add_record(records, record):
    """Add a record to the dictionary using its unique ID as the key."""
    records[record.record_id] = record
    print(f"Added {record.record_id}")


def display_records(records):
    """Loop through the dictionary and display every record."""
    print(f"\n--- All Records ({len(records)}) ---")
    for record in records.values():
        record.display_info()


def main():
    records = {}   # the ONE data structure: dictionary {record_id: object}

    # Object creation
    covid = Vaccine("COVID-19 (2-dose)", 2, (28,))
    polio = Vaccine("Polio (3-dose)", 3, (30, 30))
    covid.describe()
    polio.describe()
    print()

    r1 = VaccinationRecord(covid, "18-49", "Western Area Urban")
    r2 = VaccinationRecord.with_first_dose(polio, "0-5", "Bo", date(2026, 9, 1))
    r3 = VaccinationRecord(polio, "6-17", "Kenema")

    for r in (r1, r2, r3):
        add_record(records, r)

    # Interaction between objects: records use their Vaccine's schedule
    print(r1.administer_dose(date(2026, 9, 5)))
    print(r1.administer_dose(date(2026, 10, 3)))
    print(r2.administer_dose(date(2026, 10, 1)))

    display_records(records)

    print(f"\nTotal records created: {VaccinationRecord.total_records()}")
    print("Is '12-15' a valid age group?",
          VaccinationRecord.is_valid_age_group("12-15"))


if __name__ == "__main__":
    main()
