import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ''
    month = ''
    day = ''
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # while (city not in ['chicago', 'new york city', 'washington']):
    while city not in CITY_DATA.keys():
        city = raw_input("Enter the city to analyze (i.e. chicago, new york city, washington): ")
        city = city.lower()
    
    # get user input for month (all, january, february, ... , june)
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'otober', 'november', 'december', 'all']
    while month not in valid_months:
        month = raw_input('Enter a month to filter by, or "all" to apply no month filter: ')
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in valid_days:
        day = raw_input('Enter day of the week or "all": ')
        day = day.lower()

    print('-'*40)
    return city, month, day


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



    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'otober', 'november', 'december']
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        #filter by day of the wekk to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    print("Most common month is:", df['month'].mode()[0])

    # display the most common day of week
    print("Most common day of week is:", df['day_of_week'].mode()[0])

    # display the most common start hour
    print("Most common start hour is:", df['start_hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most common start station:", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("Most commonly used end station:", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    #group_data = df.groupby(['Start Station', 'End Station'])
    df['COUNTER'] = 1
    group_data = df.groupby(['Start Station', 'End Station'])['COUNTER'].sum()
    print("Most frequent combination of start station and end station trip:", group_data.idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time (seconds) is: ", df['Trip Duration'].sum())

    # display mean travel time
    print("Mean travel time (seconds) is: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)



    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nEarliest year of birth: " + str(earliest_birth_year))
        print("\nMost recent year of birth: " + str(most_recent_birth_year))
        print("\nMost common year of birth: " + str(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):
    user_input = input('Do you want to see raw data? Enter yes or no. \n')
    line_number = 0

    while 1 == 1:
        if user_input.lower() != 'no':
            print(df.iloc[line_number : line_number + 5])
            line_number += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        restart = raw_input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
