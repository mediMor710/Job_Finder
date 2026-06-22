import streamlit as st
from api import search_jobs

# Page config
st.set_page_config(page_title='Job Finder', layout='wide')
# layout='wide' uses the full browser width

st.title('💼 Job Finder')
st.caption('Powered by Adzuna - searches millions of listing worlwide')

# Input section
col1, col2 = st.columns(2)

with col1:
    job_title = st.text_input('Job title', placeholder='e.g. Data Analyst')

with col2:
    city = st.text_input('City', placeholder='e.g. Frankfurt')

num_results = st.slider('Results per country', min_value=20, max_value=50, value=10)
# A slider so the user can control how many results can see

# search button
if st.button('Search jobs', type='primary'):
    # type="primary" makes the button blue and prominent

    if not job_title or not city:
        st.warning('Please enter both a job title and a city.')
    else:
        with st.spinner('Searching worldwide...'):
            # st.spinner() shows a loading animation
            df = search_jobs(job_title,city,results_per_page=num_results)

        if df.empty:
            st.error('No jobs found. Try different keyword or a larger city.')
        else:
            st.success(f"Found {len(df)} listing across {df['country']}.nunique()")
            # .nunique() counts how many unique values are in the targeted country

            # --- Results table
            st.dataframe(
                df[['title', 'company', 'location', 'country', 'salary_min', 'salary_max', 'url']],
                use_container_width=True,
                column_config={
                    'url': st.column_config.LinkColumn('Link')
                    # Makes the URL column clickable link
                }
            )

            # --- Download button
            csv = df.to_csv(index=False).encode('utf-8')

            st.download_button(
                label='Download results as CSV',
                data=csv,
                file_name=f"{job_title}_{city}_jobs.csv",
                mime='text/csv'
            )