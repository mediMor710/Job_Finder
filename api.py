import requests
import pandas as pd
from config import APP_ID,APP_KEY

def search_jobs(job_title, city, results_per_page=20):
    """
    Calls the Adzuna and returns a Dataframe of job listing.
    """
    # Adzuna doesn't accept the whole country name.
    # 'gb' = UK, 'us' = USA, 'fr'= France, 'de' = Germany, etc
    countries = ['gb', 'us', 'de', 'fr', 'au', 'ca', 'nl', 'it']

    all_jobs = [] # We'll collect results from every country here

    for coun in countries:
        # the 'coun' is the targeted country and the '1' is the page number
        url = f"https://api.adzuna.com/v1/api/jobs/{coun}/search/1"
        params = {
            'app_id':   APP_ID,
            'app_key':  APP_KEY,
            'results_per_page': results_per_page,
            'what': job_title,
            'where':    city,
            'content-type': 'application/json',
        }

        try:
            response = requests.get(url,params=params, timeout=10)
            # timeout=10 means if the server doesn't give results in 10 seconds we'll give up.
            response.raise_for_status()
            # This line raises an error automatically if the server crashed.
            data = response.json()
            jobs = data.get('results',[])
            # here we got a list job lists inside 'jobs'

            for job in jobs:
                all_jobs.append({
                    "title":    job.get('title', 'N/A'),
                    'company':  job.get('company', {}).get('display_name', 'N/A'),
                    # company is nested dict: {'display_name': 'Google',....}
                    'location': job.get('location',{}).get('display_name', 'N/A'),
                    'country':  coun.upper(),
                    'salary_min':   job.get('salary_min', 'N/A'),
                    'salary_max':   job.get('salary_max', 'N/A'),
                    'description':  job.get('description', "")[:200],
                    # We get just the first 200 characters
                    'url': job.get('redirect_url', ""),
                })
            
        except requests.exceptions.RequestException as e:
                # This will get any network error if found.
                print(f"Could not fetch jobs from {coun}: {e}")
                continue
    if not all_jobs:
         return pd.DataFrame()
        # Return an empty Dataframe if nothing was found

    df = pd.DataFrame(all_jobs)
    df = df.drop_duplicates(subset=['title', 'company', 'location'])

    return df