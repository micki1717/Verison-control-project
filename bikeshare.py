# Change DS and comments 
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Let's ask user to specify a city, month, and day to analyze.

    Returns:
        (str) CITY - name of the city to analyze 
        (str) MONTH - name of the month to filter by, or "all" to apply no month filter
        (str) DAY - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ('PLEASE ENTER THE CITY: ')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input ('\nSelect Chicago, New York City OR Washington for your analysis.\n').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ('PLEASE ENTER MONTH: ')
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('ENTER WHICH MONTH january, february,...,june : ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('PLEASE ENTER DAY: ').lower()

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:', most_common_month)

    # TO DO: display the most common day of week
    most_common_dayofweek = df['day_of_week'].mode()[0] 
    print('The most common day is:', most_common_dayofweek)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]  
    print('The most common hour is:', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode ()[0]
    print('The most common start station is:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station =df['End Station'].mode ()[0]
    print('The most common end station is:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    most_frequent_combination_station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip:',most_frequent_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =round(df['Trip Duration'].sum())
    print('The total travel time in hour is:', total_travel_time)
    # TO DO: display mean travel time
    
    mean_travel_time = round(df['Trip Duration'].mean())
    print('The mean travel time in hour is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    
    # TO DO: Display counts of gender
    try:      
        user_gender = df['Gender'].value_counts()
        print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    
        earliest_year = int(df['Birth Year'].min())
        print('The earliest year',earliest_year)   
             
        most_recent_year = int(df['Birth Year'].max())
        print('The most recent ', most_recent_year) 
                                
        most_common_year = int(df['Birth Year'].mode()[0])                             
        print('The most common year', most_common_year)
   
    except:
        print('Sorry there is no data for gender in Washington city!')
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data (df):
    """Displays raw data"""
    i = 0
    raw = input("Would you like to see some raw data ? ").lower()
    pd.set_option('display.max_columns',200)
              
    while True:
        if raw =='no':
              break
        elif raw =='yes':
            print(df[0:5])
            raw = input("press yes to see 5 more rows, press no to skip").lower()
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

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
