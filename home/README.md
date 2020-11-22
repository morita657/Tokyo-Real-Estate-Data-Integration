# Overview
This is the capstone project of the data engieering project on Udacity.

## The purpose and the goal of database
The purpose of the data engienering capstone project is to combine what I've learnt through the program and solidify my knowledge and enrich my hands-on experience before going wild.
The goal of the project that I've set myself is to apply technoclogies and experience with different types of datasets.

## Outline
* step 1. Scope the Project and Gather Data
step 1-1. Identify and gather the data I'll be using for my project (at least two sources and more than 1 million rows). See Project Resources for ideas of what data I can use.
step 1-2. Explain what end use cases I'd like to prepare the data for (e.g., analytics table, app back-end, source-of-truth database, etc.)

* step 2. Explore and Assess the Data
2-1. Explore the data to identify data quality issues, like missing values, duplicate data, etc.
2-2. Document steps necessary to clean the data

* step 3. Define the Data Model
3-1. Map out the conceptual data model and explain why I chose that model
3-2. List the steps necessary to pipeline the data into the chosen data model

* step 4. Run ETL to Model the Data
4-1 Create the data pipelines and the data model
4-2 Include a data dictionary
4-3 Run data quality checks to ensure the pipeline ran as expected
    Integrity constraints on the relational database (e.g., unique key, data type, etc.)
    Unit tests for the scripts to ensure they are doing the right thing
    Source/count checks to ensure completeness

* step 5. Complete Project Write Up
5-1. What's the goal? What queries will I want to run? How would Spark or Airflow be incorporated? Why did I choose the model I chose?
5-2. Clearly state the rationale for the choice of tools and technologies for the project.
5-3. Document the steps of the process.
5-4. Propose how often the data should be updated and why.
5-5. Post my write-up and final data model in a GitHub repo.
5-6. Include a description of how I would approach the problem differently under the following scenarios:
    If the data was increased by 100x.
    If the pipelines were run on a daily basis by 7am.
    If the database needed to be accessed by 100+ people.

## Instruction
1. Run `create_tables.py` on my terminal.
2. Run `jupyter notebook` on my terminal.
3. Follow the guideline in the notebook.

## Datasets
1. Tokyo Airbnb Detailed Open Data from Kaggle
2. Tokyo weather data from Kaggle

## Tools
* Jupyter notebook
* Apache Spark with Python
* Postgres Database

## ETL Process
Load datasets as CSV files -> Transform modeling on Jupyter

## Files
* sql_queries.py
* etl.py
* create_tables.py

## Data Modeling
![ERD]("ERD.png")
### Fact Table
listings - id, host_id, listing_id

### Dimension Tables
weather - weather_id, date, high, low, max_precipitation_in_a_day, daylight_hours_in_a_day

calendar - calendar_id, listing_id, date, available, price, adjusted_price, minimum_nights, maximum_nights, calendar_updated, has_availability, availability_30, availability_60, availability_90, availability_365, calendar_last_scraped, guests_included, extra_people, minimum_nights, maximum_nights, minimum_minimum_nights, maximum_minimum_nights, minimum_maximum_nights, maximum_maximum_nights, minimum_nights_avg_ntm, maximum_nights_avg_ntm 

host - listing_id, host_id, host_url, host_name, host_since, host_location, host_about, host_response_time, host_response_rate, host_acceptance_rate, host_is_superhost, host_thumbnail_url, host_picture_url, host_neighbourhood, host_listings_count, host_total_listings_count, host_verifications, host_has_profile_pic, host_identity_verified

location - listing_id, street, city, state, zipcode, market, smart_location, country_code, country, latitude, longitude, is_location_exact

property - listing_id, listing_url, name, summary, space, description, experiences_offered, neighborhood_overview, notes, transit, access, interaction, house_rules, thumbnail_url, medium_url, picture_url, xl_picture_url, neighbourhood, neighbourhood_cleansed, neighbourhood_group_cleansed, property_type, room_type, accommodates, bathrooms, bedrooms,  beds,  bed_type, amenities, square_feet

requirements - 
listing_id, requires_license, license, jurisdiction_names, instant_bookable, is_business_travel_ready, cancellation_policy, require_guest_profile_picture, require_guest_phone_verification, calculated_host_listings_count, calculated_host_listings_count_entire_homes, calculated_host_listings_count_private_rooms, calculated_host_listings_count_shared_rooms, 


reviews - review_id, listing_id, id, date, reviewer_id, reviewer_name, comments, number_of_reviews, number_of_reviews_ltm, first_review , last_review , review_scores_rating, review_scores_accuracy, review_scores_cleanliness, review_scores_checkin, review_scores_communication, review_scores_location, review_scores_value, reviews_per_month


price - price_id, listing_id, price, weekly_price, monthly_price, security_deposit, cleaning_fee



## Further Scenarios
Since the dataset in this project is the archive, the freshness of data is only the first usage. Therefore, real-time data extraction and process pipleline construction would be desired for real life usage. For example,  couple of the desired implementations are the following. The first one is that raw data scraping functionality in the Internet to keep the freshness of the data. The second one is S3 bucket configuration to store those data since the amount of the data would exceed the capacity of local computer. The third one is to Airflow implementaion to schedule data processing constantly.

## Usage of Processed Data
Since the processed data is strongly focused on the property information, one of the example usage is useful to consult business.  For example, suppose a new property owner started his/her property rent business on Airbnb, they might not know the proper price to gain the number of reservations. Utilizing this dataset, business analyst can support those new owners.
