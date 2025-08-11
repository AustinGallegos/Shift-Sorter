import os


def clear_files(shifts):
    """Clear or create CSV files for each shift."""
    for shift in shifts.values():
        path = os.path.join("csvs/", f"{shift}.csv")
        with open(path, "w"):
            pass


def load_aa_logins(filepath="txt/associates.txt"):
    """Load AA logins from the specified file."""
    with open(filepath, "r") as file:
        content = file.readlines()
    return content


def assign_aa_to_shift(login, shift):
    """Append the AA login to the correct shift's CSV file and print the result."""
    path = os.path.join("csvs/", f"{shift}.csv")
    with open(path, "a") as file:
        file.write(login)
    print(login.strip(), f"-- {shift}")
