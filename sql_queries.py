# DROP TABLES

listings_table_drop = "drop table if exists listings;"
weather_table_drop = "drop table if exists weather;"
calendar_table_drop = "drop table if exists calendar;"
host_table_drop = "drop table if exists host;"
location_table_drop = "drop table if exists location;"
property_table_drop = "drop table if exists property;"
requirements_table_drop = "drop table if exists requirements;"
reviews_table_drop = "drop table if exists reviews;"
pric_table_drop = "drop table if exists price;"

# CREATE TABLES
listings_table_create = ("""
create table if not exists listings (
    id serial primary key,
    host_id bigint
);
""")


weather_table_create = ("""
create table if not exists weather(
    weather_id serial primary key,
    date timestamp, 
    high float,
    low float,
    max_precipitation_in_a_day float,
    daylight_hours_in_a_day float
);
""")

calendar_table_create = ("""
create table if not exists calendar(
    calendar_id serial primary key,
    listing_id int,
    date timestamp, 
    available boolean,
    price varchar,
    adjusted_price varchar,
    minimum_nights int,
    maximum_nights int,
    calendar_updated varchar,
    has_availability boolean,
    availability_30 int,
    availability_60 int,
    availability_90 int,
    availability_365 int,
    guests_included int,
    extra_people varchar
);
""")

host_table_create = ("""
create table if not exists host(
    listing_id int,
    host_id bigint,
    host_url varchar,
    host_name varchar,
    host_since timestamp, 
    host_location varchar,
    host_about varchar,
    host_response_time varchar,
    host_response_rate varchar,
    host_acceptance_rate varchar,
    host_is_superhost boolean, 
    host_thumbnail_url varchar,
    host_picture_url varchar,
    host_neighbourhood varchar,
    host_listings_count int,
    host_total_listings_count int,
    host_verifications varchar,
    host_has_profile_pic boolean,
    host_identity_verified boolean
);
""")

location_table_create = ("""
create table if not exists location(
    listing_id int,
    street varchar,
    city varchar,
    state varchar,
    zipcode varchar,
    market varchar,
    smart_location varchar,
    country_code  varchar(2),
    country varchar,
    latitude varchar,
    longitude varchar,
    is_location_exact boolean
);
""")

property_table_create = ("""
create table if not exists property(
    listing_id int,
    listing_url varchar,
    name varchar,
    summary varchar,
    space varchar,
    description varchar,
    experiences_offered varchar,
    neighborhood_overview varchar,
    notes varchar,
    transit varchar,
    access varchar,
    interaction varchar,
    house_rules varchar,
    thumbnail_url varchar,
    medium_url varchar,
    picture_url varchar,
    xl_picture_url varchar,
    neighbourhood varchar,
    neighbourhood_cleansed varchar,
    neighbourhood_group_cleansed varchar,
    property_type varchar,
    room_type varchar,
    accommodates int,
    bathrooms float,
    bedrooms int,
    beds int,
    bed_type varchar,
    amenities varchar,
    square_feet int
);
""")

requirements_table_create = ("""
create table if not exists requirements(
    listing_id int,
    requires_license bigint,
    license varchar,
    jurisdiction_names varchar,
    instant_bookable boolean,
    is_business_travel_ready boolean,
    cancellation_policy varchar,
    require_guest_profile_picture boolean,
    require_guest_phone_verification boolean,
    calculated_host_listings_count int,
    calculated_host_listings_count_entire_homes int,
    calculated_host_listings_count_private_rooms int,
    calculated_host_listings_count_shared_rooms int
);
""")

reviews_table_create = ("""
create table if not exists reviews(
    review_id serial primary key,
    listing_id int,
    date timestamp, 
    reviewer_id bigint,
    reviewer_name varchar,
    comments varchar,
    number_of_reviews int,
    number_of_reviews_ltm int,
    first_review  bigint,
    last_review  bigint,
    review_scores_rating int,
    review_scores_accuracy int,
    review_scores_cleanliness int,
    review_scores_checkin int,
    review_scores_communication int,
    review_scores_location int,
    review_scores_value int,
    reviews_per_month float
);
""")

price_table_create = ("""
create table if not exists price(
    price_id serial primary key,
    listing_id int,
    price varchar,
    weekly_price varchar,
    monthly_price varchar,
    security_deposit varchar,
    cleaning_fee varchar
);
""")


create_table_queries = [listings_table_create, weather_table_create, calendar_table_create, host_table_create, location_table_create, property_table_create, requirements_table_create, reviews_table_create, price_table_create]
drop_table_queries = [listings_table_drop, weather_table_drop, calendar_table_drop, host_table_drop, location_table_drop, property_table_drop, requirements_table_drop, reviews_table_drop, pric_table_drop]
