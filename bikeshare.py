import time
import pandas as pd
import numpy as np
import datetime

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
        city = input("\nWhich city's data would you like to view?\nChicago, New York City, or Washington?\n").lower()
        cities = ('chicago','new york city','washington')
        if city not in cities:
            print("\nSorry about that. We don't have that city's data. Please try another city.\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nAre you interested in a particular month?\nIf yes, type the month you're interested in. You may view data for January through June. Otherwise, type 'all'.\n").lower()
        months = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
        if month not in months:
            print ("\nSorry about that. We don't have data for that month. Please try another month.\n")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWould you be interested in a specific day of the week?\nIf yes, type day you're interested in. Otherwise, type 'all'.\n").lower()
        days = ('monday','tuesday','wednesday','thursday','friday', 'saturday', 'sunday', 'all')
        if day not in days:
            print ("\nSorry about that. We don't have data for that day. Please try another day.\n")
            continue
        else:
            break

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
    #Load City Data into DataFrame.
    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #Extract month, day of week, and hour data from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

        #Change day string to integer
        day = time.strptime(day,"%A").tm_wday

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most Common Month:", df['month'].mode()[0])
    print("January: 1, February: 2, March: 3, April: 4, May: 5, June: 6\n")

    # TO DO: display the most common day of week
    print("Most Common Day:", df['day_of_week'].mode()[0])
    print("Monday: 0, Tuesday: 1, Wednesday: 2, Thursday: 3, Friday: 4, Saturday: 5, Sunday: 6\n")

    # TO DO: display the most common start hour
    print("Most Common Hour:", df['hour'].mode()[0])
    print("Please note 24 hour clock.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most Common Start Station:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most Common End Station:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    print ("Most Frequent Combination of Start and End Station:", df['Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print ("Total Travel Time:", (df['Trip Duration'].sum()/86400), "days", "or", (df['Trip Duration'].sum()/31536000), "years")

    # TO DO: display mean travel time
    print ("Mean Travel Time:", (df['Trip Duration'].mean()/60), "minutes", "or", (df['Trip Duration'].mean()/3600), "hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print ("\nTypes of Users:\n", df['User Type'].value_counts())

    except KeyError:
        print ("No user type data available for this city or time period.")

    # TO DO: Display counts of gender
    try:
        print ('\nUsers\' Gender:\n', df['Gender'].value_counts())

    except KeyError:
        print ("No gender data available for this city or time period.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print ("\nEarliest Birth Year:", df['Birth Year'].min())
        print ("Most Recent Birth Year:", df['Birth Year'].max())
        print ("Most Common Birth Year:", df['Birth Year'].mode())

    except KeyError:
        print ("No birth year data available for this city or time period.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """ Displays DataFrame for raw bikeshare data """

    upper_row = 0
    lower_row = 5

    while True:
        raw = input("Would you like to view 5 lines of raw trip data?\nYes or No?\n").lower()
        if raw != "yes":
            break
        else:
            print(df.iloc[upper_row:lower_row])

            # Write a while loop

            while True:
                more_data = input("\nWould you like to see 5 more lines of data?\nYes or No?\n").lower()
                if more_data != "yes":
                    break
                else:
                    upper_row += 5
                    lower_row += 5
                    print(df.iloc[upper_row:lower_row])
                    continue
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
