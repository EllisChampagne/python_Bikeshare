import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# define variable
cities=['chicago','new york city','washington']
months=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December','All']
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']


def get_filters():
    # get_filters() is a Python function that collects user input for city, month, and day. 
    # It ensures that user inputs are valid based on the predefined lists of options.

    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """
    def check_input(prompt, valid_inputs):
        while True:
            user_input = input(prompt).strip().lower()
            if user_input in valid_inputs:
                return user_input
            else:
                print(f"Invalid input. Please enter one of the following: {', '.join(valid_inputs)}")

    print('\nHello! Let\'s explore some US bikeshare data!\n \nWe will be analyzing statistics from cities across select months and days.\n\nPlease choose your inputs:')
    
    """Def Check_input function runs to validate all inputs - albeit the validations seem to work without. Added based on feedback"""

    # TO DO: get user input for cities
    # COMPLETE: Second variable is for the user to declare 'City' and requests the value
    while True:
        city=str(input('\n\nPlease select a city from "Chicago", "New York City", or "Washington". \n')).lower()
        if city not in cities:
            print('Invalid city name. Please enter one of "Chicago", "New York City", or "Washington"\nReminder, check spelling.')
        else:
            break
    #TO DO: get user input for month (all, january, february, ... , june)
    # COMPLETE: Second variable is for user to declare 'month' amd reqests the value  

    while True:
        month=str(input('\nPlease select a month value, or choose All.\n')).title()
        if month not in months:
            print('Please select either All or a valid month - check spelling')
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # COMPLETE: Third variable is for user to declare 'day' amd reqests the value  

    while True:
        day=str(input('\nTo filter by day, please select a value from Monday - Sunday value, or else choose All.\n')).title()
        if day not in days:
            print('Your entry did not retun a valid day, please try again with Monday through Sunday Values or All.')
        else:
            break

    #print value here returns a break and the requested variables
    
    print('-'*40)
    return city, month, day
    # Once all three pieces of information are successfully collected, the function returns these values to be used in other parts of the program.


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # First create a dataframe for analysis utilizing the city var
    df = pd.read_csv(CITY_DATA[city]) 
    #easy first step, just create data fram to load city data from city variable
    #[city] is the input index for csv files

    # Modify the start time variable to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #modifys the start time to datetime with pandas

    # Utilize the new starttime variable for a month and day of week addition
    df['month'] = df['Start Time'].dt.month
    #creates a new column in dataframe for moth value
    df['day_of_week'] = df['Start Time'].dt.day_name()  # Convert day_of_week to string
    #same thing as above, but for day name using datetime functions - dt

    # Utilizing the month variable, identify index value to curate analysis
    if month != 'All':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # Same as above, but for day
    if day != 'All':
        day = day.title()
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    """ Author Notes: had to write numerous checks to confirm if the selected month is available in the data
     this reuquired validation across the month, the day, and the hour
     ultimately, took the same validation across all functions - just altering for their variables - time
     Gender, Stations etc. It's not necessary, but if one ever wanted to add an argument at the front could be 
     beneficial """


    print('\n~~~~~ Travel Time Stats ~~~~~\n')
    start_time = time.time()

    # display the most common month
    if 'month' in df: #checks to see if month is in the df
        month_mode = df['month'].mode() #if month is, run month_mode for most common
        if not month_mode.empty: #if month is NOT empty, print the iloc on index
            print('The most common month of travel is:', months[month_mode.iloc[0] - 1])
        else: #if empty, let user know no selection
            print('It appears there is no data for the month value selected.')
    else:
        print('No data available for the most common month.')

    # display the most common day of week
    # same as above for day_of_week df
    if 'day_of_week' in df:
        day_mode = df['day_of_week'].mode()
        if not day_mode.empty:
            print('The most common day for travel is: {}'.format(day_mode[0]))
        else:
            print('It appears there is no data for the day of the week selected.')
    else:
        print('No data available for the most common day of the week.')

        """ No need to comment on all the code - this is the same logic as day and month but for hour""" 

    # display the most common start hour
    if 'hour' in df:
        hour_mode = df['hour'].mode()
        if not hour_mode.empty:
            print('The most common start hour for a trip is: {}'.format(hour_mode[0]))
        else:
            print('It appears there is no data for the start hour selected.')
    else:
        print('No data available for the start hour.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n~~~~~ Station Stat Data ~~~~~\n')
    start_time = time.time()

    if not df.empty: #parent if not empty statement that runs to confirm valid inputs for checks
        # display most commonly used start station
        if 'Start Station' in df: #this format is similar to the above with time stats
                                # it's technically not needed since this isn't filtered
                                # however, for consistency it's included 
            popular_start_station = df['Start Station'].mode()
            if not popular_start_station.empty: 
            #if the start station is empty - or month (for example) would return nulls
            #then the user would get either a return value
                print('The most popular start station is:', popular_start_station.iloc[0])
            else:
                print('No data available for the most popular start station.')
            #else it would get no return data
                
        # display most commonly used end station
        if 'End Station' in df:
            popular_end_station = df['End Station'].mode()
            if not popular_end_station.empty:
                print('The most common ending station is:', popular_end_station.iloc[0])
            else:
                print('No data available for the most common ending station.')

        # display most frequent combination of start station and end station trip
        if 'Start Station' in df and 'End Station' in df:
            group_field = df.groupby(['Start Station', 'End Station'])
            popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
            if not popular_combination_station.empty:
                print('The most common trip is:\n', popular_combination_station)
            else:
                print('No data available for the most common trip.')

    else:
        print("No data available for the selected filters.")
   
    print("\nThe Station Stats took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\n~~~~~ Trip Duration Stats ~~~~~\n')
    start_time = time.time()

    if 'month' not in df:
        print(f"No data available for the selected month: {month}")
        return
    
    if not df.empty:#parent if not empty statement that runs to confirm valid inputs for checks
        # Calculate total travel time
        total_duration_seconds = df['Trip Duration'].sum()
        total_h, remaining_seconds = divmod(total_duration_seconds, 3600) 
        #This line converts the mean trip duration from seconds to hours and stores the result in two variables
        #total_h stores hours by taking the total duation and dividing by total seconds in hours - 3600 (otherwise would need to do minutes as well)
        #reamining secods is returned from divmod
        total_m, total_s = divmod(remaining_seconds, 60)
        #This line breaks down the remainder into minutes and seconds

        # Calculate mean travel time
        #the notes for this caluclation are the same as the above - expect with the mean calculation
        mean_duration_seconds = df['Trip Duration'].mean()
        mean_h, remaining_seconds = divmod(mean_duration_seconds, 3600) 
        mean_m, mean_s = divmod(remaining_seconds, 60)

        # Display total travel time and mean travel time
        print(f'The total travel time for your selected city is: {total_h} hours, {total_m} minutes, and {total_s:.1f} seconds.') #included .1 so that its nicer output 
        print(f'The mean travel time of a trip in your selected city is: {mean_h} hours, {mean_m} minutes, and {mean_s:.1f} seconds.') #included .1 so that its nicer ouput
    else:
        print("No Trip Duration data available for the selected filters - please try again.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n~~~~~ User Stats ~~~~~\n')
    start_time = time.time()

    #after a while, I just started to repeat the process for all columns - gender included
    #this code ensures that if gender is ever an argument it will validate that the city
    #month and other inputs can still run the analysis

    if not df.empty:#parent if not empty statement that runs to confirm valid inputs for checks
        # Display counts of user types
        if 'User Type' in df:
            user_type_counts = df['User Type'].value_counts()
            if not user_type_counts.empty:
                print('User Type Stats:')
                print(user_type_counts)
            else:
                print('No data available for User Type stats.')

        # Display counts of gender
        if 'Gender' in df:
            gender_counts = df['Gender'].value_counts()
            if not gender_counts.empty:
                print('Gender Stats for the selected city:')
                print(gender_counts)
            else:
                print('No data available for Gender stats.')

        # Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df:
            birth_years = df['Birth Year'].dropna()  # Drop missing values
            if not birth_years.empty:
                print('Birth Year Stats:')
                most_common_birth_year = birth_years.mode()
                if not most_common_birth_year.empty:
                    print(f'The Most Common Birth Year of riders: {most_common_birth_year.iloc[0]}')
                else:
                    print('No data available for the most common Birth Year.')

                most_recent_birth_year = int(birth_years.max())
                print(f'The Most Recent Birth Year, and youngest Rider was born in: {most_recent_birth_year}')

                earliest_birth_year = int(birth_years.min())
                print(f'The Earliest Birth Year of a rider is: {earliest_birth_year}')
            else:
                print('No data available for the Birth Year stats - please try different filters.')
    else:
        print("No Birth Year data available for the selected filters - please try again.")
#below statement runs across the defined functions until complete

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def review_data(df):
    print('\n~~~~~ Sample Data ~~~~~\n')
    start_time = time.time()
    start_loc = 0  # Start the index at 0 for the decleration of this variable

    while True: #outerloop
        review_data = input("Do you want to see five sample rows of the data? Please select 'Yes' or 'No': ").strip().lower() #user input for review_data

        if review_data == 'yes': #innerloop for user input and continues until break function
            if start_loc < len(df):  # Checks to see if the start_location is less than the df length
                print(df.iloc[start_loc:start_loc + 5]) #if so, prints the location + 5
                start_loc += 5 #adds to the start_location variable 
            else:
                print("No more data to display.")
                break #if fails no more data to display

            while True: #Second Inner Loop 
                review_data = input("Do you wish to see five more rows? Enter 'Yes' to see more or 'No' to stop: ").strip().lower()
                if review_data == 'yes': 
                    if start_loc < len(df):
                        print(df.iloc[start_loc:start_loc + 5])
                        start_loc += 5 
                    else:
                        print("No more data to display.")
                        break #break statement if data is maxed
                elif review_data == 'no':
                    print("No Additional Data Review Requested.")
                    break #break statement if user selects no after first run
                else:
                    print("Invalid input. Please enter 'Yes' to see more or 'No' to stop.") #statement to ensure validity of input

        elif review_data == 'no': #outerloop for if user inputs no - break runs
            print("No Data Review Requested.")
            break #outer loop break statement ending loop
        else: #outer loop for invalid argument keeping statement true
            print("Invalid input. Please enter 'Yes' or 'No'.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        if 'month' in df:
            user_stats(df)
        else:
            print("Data for the selected month is not available in the CSV.")
        
        review_data(df)
     # I became increasingly tired of adjusting each function to confirm if data is present, and therefore
     # requested a validation of month field to be validated before proceeding through the functions 
     # This still didn't operate as I expected though, but didn't hurt code from executing - would probably need
     # need to be pulled for speed at some point        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
