from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

def get_movie_listings(name: str, code: str, city: str, date: str) -> list:
    driver = webdriver.Chrome(options=options)
    url = f"https://in.bookmyshow.com/cinemas/{city}/{name}/buytickets/{code}/{date}"
    driver.get(url)

    # Wait for the movie listing to render (up to 15 seconds)
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(url))
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.sc-1412vr2-2"))
        )
    except Exception:
        print(f"Redirected!")
        driver.quit()
        return []

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "lxml")

    # Extract movie names from the cinema session listing
    movie_titles = soup.find_all("a", class_="sc-1412vr2-2 cPWByY")

    movies = []

    for title in movie_titles:
        movie_name = title.text.strip()
        movies.append(movie_name)

    return movies



if __name__ == "__main__":
    movies = get_movie_listings(name="inox-janak-place", code="SCJN", city="national-capital-region-ncr", date="20260312")
    print(movies)