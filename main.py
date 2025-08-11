import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import file_handler as f
import webdriver as d


def main():
    shifts = {"MOR", "DAY", "TWI", "NIT"}
    codes = {
        key: {x for x in os.getenv(env).split(",")}
        for key, env in {
            "MOR": "MOR_CODES",
            "DAY": "DAY_CODES",
            "TWI": "TWI_CODES",
            "NIT": "NIT_CODES",
        }.items()
    }

    f.clear_files(shifts)

    driver, wait = d.setup_driver()

    driver.get(os.getenv("LINK"))
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))

    logins = f.load_aa_logins()
    for login in logins:
        d.process_login(codes, driver, login)

    driver.quit()


if __name__ == "__main__":
    main()
