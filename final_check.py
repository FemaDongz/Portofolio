import sys
from bs4 import BeautifulSoup

def check():
    with open('index.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    issues = []
    # Check skip link
    skip = soup.find('a', class_='skip-to-content')
    if not skip or skip.get('href') != '#heroSection':
        issues.append("Skip link missing or wrong href")

    # Check heroSection exists
    if not soup.find(id='heroSection'):
        issues.append("heroSection id missing")

    # Check hamburger button
    btn = soup.find('button', id='hamburgerBtn')
    if not btn or 'aria-label' not in btn.attrs or btn.get('aria-expanded') != 'false':
        issues.append("Hamburger button incorrect")

    # Check maze labels
    maze_btns = soup.select('.ctrl-btn')
    for b in maze_btns:
        if 'aria-label' not in b.attrs:
            issues.append(f"Maze button missing label: {b.text}")

    # Check menu role
    menu = soup.find(id='menuOverlay')
    if not menu or menu.get('role') != 'navigation':
        issues.append("Menu overlay missing role navigation")

    if issues:
        print("\n".join(issues))
        sys.exit(1)
    print("All final checks passed!")

if __name__ == "__main__":
    check()
