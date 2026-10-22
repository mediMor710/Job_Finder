# 💼 Job Offers Finder

A simple job search application built with **Python and Streamlit** that allows users to find job opportunities by entering a job title and a target location. The application uses the **Adzuna API** to retrieve job offers from multiple countries and displays the results in an organized table.

## ✨ Features

- 🔎 Search for job offers using a job title and a target location.
- 🌍 Search across eight countries: Germany, France, the United States, the United Kingdom, the Netherlands, Australia, Canada, and Italy.
- 📊 Display up to 100 job offers in a structured table.
- 🏢 View job titles, company names, locations, and countries.
- 💰 Check minimum and maximum salary information when available.
- 📝 Read job descriptions and access the original offer through its URL.
- 🖥️ Use a simple, interactive interface powered by Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web interface |
| Pandas | Organizing and displaying job offer data |
| Requests | Sending HTTP requests to the API |
| Adzuna API | Retrieving job listings |

## 📁 Project Structure

```text
job-offers-finder/
│
├── app.py             # Streamlit application and user interface
├── api.py             # Adzuna API integration and job search logic
├── config.py          # API credentials configuration
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

### File Description

- **`app.py`** — Builds the Streamlit interface, collects the user's search inputs, calls the job search functionality, and displays the results in a table.
- **`api.py`** — Communicates with the Adzuna API to retrieve job offers from the supported countries.
- **`config.py`** — Stores the Adzuna API credentials (`app_id` and `app_key`).
- **`requirements.txt`** — Lists the Python packages required to run the application.
- **`README.md`** — Explains the project's purpose, setup, and usage.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/mediMor710/Job_Finder.git
cd Job_Finder
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it using the appropriate command for your operating system.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Adzuna API

Obtain your API credentials from the [Adzuna Developer Portal](https://developer.adzuna.com/).

Configure your `config.py` file with your credentials:

```python
app_id = "YOUR_APP_ID"
app_key = "YOUR_APP_KEY"
```

Replace the placeholder values with your actual credentials.

### 5. Run the application

From the project directory, execute:

```bash
streamlit run app.py
```

Streamlit will provide a local URL where you can open the application in your browser.

## 🚀 How to Use

1. Launch the application.
2. Enter a job title, such as `Data Analyst`, `Python Developer`, or `Data Engineer`.
3. Enter the target location, such as `Berlin`, `Paris`, or `London`.
4. Start the search.
5. Explore the returned job offers in the results table.
6. Review the available salary information and descriptions.
7. Open the original job advertisement using its URL.

The application displays a maximum of 100 offers per search. The actual number of results depends on API availability and the search criteria.

## 📋 Output

The results table contains the following columns:

| Column | Description |
|---|---|
| `title` | Job title |
| `company` | Recruiting company |
| `location` | City or location of the job |
| `country` | Country where the job is offered |
| `salary_min` | Minimum advertised salary, when available |
| `salary_max` | Maximum advertised salary, when available |
| `description` | Job description or summary returned by the API |
| `url` | Link to the original job advertisement |

Some offers may not contain salary information or a complete description.

## 🌐 Supported Countries

- Germany
- France
- United States
- United Kingdom
- Netherlands
- Australia
- Canada
- Italy

## 🔑 API and Data Source

This project uses the **Adzuna Job Search API** to retrieve job listings.

- API provider: [Adzuna](https://www.adzuna.com/)
- Developer documentation: [Adzuna API Documentation](https://developer.adzuna.com/)

The availability, number, and details of job offers depend on the API response, supported search parameters, and API usage limits.

## ⚠️ Limitations

- The application requires valid Adzuna API credentials and an internet connection.
- Search results depend on the availability of listings from the API.
- Salary information may be missing for some offers.
- The application displays up to 100 offers per search; this does not guarantee that 100 offers will always be available.
- API rate limits and access restrictions may affect search results.

## 🔮 Possible Improvements

- Add filters for salary, company, and employment type.
- Allow users to export results to CSV or Excel.
- Add pagination for browsing larger result sets.
- Improve error handling for API failures and invalid searches.
- Store favorite job offers for later reference.
- Introduce automated tests for the API and application logic.

## 👨‍💻 Author

**ELMEHDI MORTAJA**

- GitHub: (https://github.com/mediMor710)

## 📄 License
