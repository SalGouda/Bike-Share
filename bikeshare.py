import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities = ['chicago', 'new york', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday']
    month, day = 'all', 'all'
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
    while city not in cities:
        city = input('\nEnter a valid city!\n').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    filter = input('\nWould you like to filter data by month, day, all, or none?\n').lower()
    
    if filter == 'month' or filter == 'all':
        month = input('\nWhich month - January, February, March, April, May, or June?\n').lower()
        while month not in months:
            month = input('\nEnter a valid month!\n').lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filter == 'day' or filter == 'all':
        day = input('\nWhich day - Saturday, Sunday, Monday, Tuesday, Wednesday, Thrusday, or Friday?\n').lower()
        while day not in days:
           day = input('\nEnter a valid day!\n').lower()
        
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

    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        
        df = df[df['month']==month]
        
    if day != 'all':
        df = df[df['day_of_week']==day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:', common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station:', common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most common end station:', common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + df['End Station']
    common_trip = df['trip'].mode()[0]
    print('Most common trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('Total trip duration is {} hours {} minutes {} seconds'.format(hour, minute, second))
    
    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    m, s = divmod(average_duration, 60)
    h, m = divmod(m, 60)
    print('Average trip duration is {} hours {} minutes {} seconds'.format(h, m, s))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Types of users:\n', user_types)
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Types of users by gender:\n', gender)
    except:
        print('No "Gender" information availabe')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        oldest = int(df['Birth Year'].min())
        youngest = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('Earliest year of birth: {} \nMost recent year of birth: {} \nMost common year of birth: {}'.format(oldest,youngest,common_year))     
    except:
         print('No "Birth Year" information available')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    runs = 0
    while True:
        raw_data = input('Would you like to view more raw data of the selected city? Enter yes or no. \n').lower()
    
        if raw_data == 'yes':
            runs += 1
            print(df.iloc[(runs-1)*5:runs*5])
        elif raw_data == 'no':
            break
        
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
       


if __name__ == "__main__":
	main()
