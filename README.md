### LCG Stats

This project automates the process of logging into my League of Comic Book Geeks account and then returns stats on my collection including:
- comics collected
- comics read
- cover price
- total price paid
- estimated value

as well as my favorite publishers, formats, and most collected characters.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

Clone the repository:
```git clone https://github.com/your-username/your-repo.git```

Navigate to the project directory:
```cd your-repo```

Install the required dependencies:
```pip install -r requirements.txt```

Create your own .env file with your login credentials for League of Comicbook Geeks:
EMAIL=<youremail>
PASSWORD=<yourpassword>

## Usage

Update the code with your desired website URL and element selectors in the Python file.

Run the Python file:
```python your_file.py```

The output will be displayed in the console, showing the extracted data from the website.

## Dependencies

The project relies on the following dependencies. They can be installed using the command mentioned in the Installation section.

- BeautifulSoup 4.9.3
- Selenium 4.0.0

# Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

# License
MIT License