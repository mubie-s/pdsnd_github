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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter city name: ")
        if city in CITY_DATA:
            break
        else:
            print("City name is invalid")


    # TO DO: get user input for month (all, january, february, ... , june)
    months_ = ['all','january','february','march','april','may','june']
    while True:
        month = input("Enter desired month: ")
        if month not in months_:
            print("Specified month is unavailable")
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week_days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input("Enter desired day: ")
        if day not in week_days:
            print("Specified day is invalid")
        else:
            break


    print('*'*80)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common travel month is month {}".format(most_common_month))


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common travel day of the week is on {}".format(most_common_day))


    # TO DO: display the most common start hour
    most_common_starthour = df['hour'].mode()[0]
    print("Most common travel hour is hour {}".format(most_common_starthour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is {}".format(most_common_start_station))


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station is {}".format(most_common_start_station))


    # TO DO: display most frequent combination of start station and end station trip
    com_end_and_start_station = df.groupby(['Start Station','End Station']).size().nlargest(1)

    print("Most frequent combination of start station and end station is:\n")
    print('\n',com_end_and_start_station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total trip duration is {} mins".format(total_travel_time))



    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The average trip duration is {} mins".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print(count_user_type)


    # TO DO: Display counts of gender
    while True:
        try:
            count_gender = df['Gender'].value_counts()

            print(count_gender)
            break
        except KeyError:
            print("\nUnfortunately, Gender data is not available to this city\n")
            break



    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:

            earliest_birth_year = df['Birth Year'].min()
            print("The earliest year of birth is year {}".format(earliest_birth_year))

            recent_birth_year = df['Birth Year'].max()
            print("The most recent birth year is year {}".format(recent_birth_year))

            common_birth_year = df['Birth Year'].mode()[0]
            print("The most common birth year is year {}".format(common_birth_year))
            break
        except KeyError:
            print("\nUnfortunately, Birth Year data is not available to this city\n")
            break




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*80)


def display(df):
    while True:
        print("Below is the first five rows of raw data:\n",df.iloc[:5])
        response = input("\n Would you like to check again or exit? Enter YES for check again and NO for exit.\n")
        if response.lower() == 'no':
              break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
