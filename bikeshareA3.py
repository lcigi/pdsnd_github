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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\nWould you like to explore new york city, chicago or washington?\n").lower()

    while city not in ["new york city", "chicago", "washington"]:
        if city == "new york city":
            return "new_york_city.csv"

        elif city == "chicago":
            return "chicago.csv"

        elif city == "washington":
            return "washington.csv"




    # get user input for month (all, january, february, ... , june)
    month_dict = {'january: 0', 'february: 1', 'march: 2', 'april: 3', 'may: 4' 'june: 5', 'all: 6'}
    month = int(input("\nFrom january to june, what month would you like to explore? \nPlease use integers with january = 0, june =5 and 'all' = 6\n"))

    while False:
        if month in month_dict:
            print('\nGreat!\n')
        else:
            print('\nplease try again, invalid input\n')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_dict = ('monday: 0', 'tuesday: 1', 'wednesday: 2' 'thursday: 3', 'friday: 4', 'saturday: 5', 'sunday: 6', 'all: 7')
    day = int(input("\nWhat day would you like to explore? \nPlease use integers with monday = 0, sunday = 6 and 'all' = 7.\n"))

    while False:
        if day in day_dict:
            print('\nGreat!\n')
        else:
            print('\nPlease try again. Invalid input\n')


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.datetime(df['Start Time'])

    df['month'] = df['Start time'].dt.month

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    df = df[df['month'] == month]

    df['week_day'] = df['Start time'].dt.dayofweek

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_list = ["January", "February", "March", "April", "May", "June"]

    index = int(df["start_time"].dt.month.mode())

    most_common_month = month_list[5]

    print("The most popular month was {}.".format(most_common_month))

    # display the most common day of week
    week_day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    index = int(df["start_time"].dt.weekday_name.mode())

    most_common_weekday = week_day_list(df["start_time"])

    print("The most popular month was {}.".format(most_common_weekday))

    # display the most common start hour
    filename = city

    filename = pd.read_csv(filename)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    CITY_DATA = pd.DataFrame(columns=['Start Station'])

    count_start_station = ['Start Station'].count(level='Start Station')

    most_popular_start_station = count_start_station.max()

    print('The most popular start station was {}.'.format(most_popular_start_station))


    # display most commonly used end station
    CITY_DATA = pd.DataFrame(columns=['End Station'])

    count_end_station = ['End Station'].count(level='End Station')

    most_popular_end_station = count_end_station.max()

    print('The most popular end station is {}.'.format(most_popular_end_station))


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    CITY_DATA = pd.DataFrame(columns=['Trip Duration'])

    total_travel_time = ['Trip Duration'].sum()

    print('The total travel time was {}.'.format(total_travel_time))

    # display mean travel time
    CITY_DATA = pd.DataFrame(columns=['Trip Duration'])

    mean_travel_time = ['Trip Duration'].mean()

    print('The mean travel time was {}.'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    filename = city

    # Display counts of user types
    user_types = df['User Types'].value_counts()

    print(user_types)

    # Display counts of gender

    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print('Not availabe')

    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:

        earliest_birth_year = df['Birth Year'].min()

        latest_birth_year = df['Birth Year'].max()

        mc_birth_year = df['Birth Year'].mode()

        print('Earliest birth year was: {}.'.format(earliest_birth_year))
        print('Most recent birth year was: {}.'.format(latest_birth_year))
        print('Most common birth year was: {}.'.format(mc_birth_year))

    else:
        print('Not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
