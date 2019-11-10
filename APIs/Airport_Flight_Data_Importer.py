#! python3

"""
Purpose: Get flight info using Kiwi.com API

Flights:
    https://docs.kiwi.com

Bookings:
    https://docs.kiwi.com/booking

Dominant airlines by hub:
    https://www.nasdaq.com/article/airline-hubs-which-carrier-dominates-your-airport-cm863860


General parameters:
    origin: string representing the ID or IATA (e.g. - DTW, DFW, COS)
    destination: string representing the ID or IATA (e.g. - DTW, DFW, COS)
    start_date: datetime representing first possible travel date (Format: month/day/year -> 2/22/2019)
    end_date: datetime representing last possible travel date (Format: month/day/year -> 2/22/2019)
    adults: number of adult passengers
    children: number of child passengers
    infants: number of infant passengers



NOTE: Reequired, non-standard packages:
    pandas
    requests
"""

import os
import math
import requests
import numpy as np
import pandas as pd
from time import sleep
from random import randint
from getpass import getuser
from datetime import datetime


##################################################
# User variables
depart_from = 'cos' # Depature hub
return_to = 'den' # Arrival hub
depart_date = '5/10/2019' # Format: mm/dd/yyyy
return_date = '5/17/2019' # Format: mm/dd/yyyy
num_adults = 2
num_children = 1
num_infants = 0
num_of_bags = 4


### Update to desired Excel output folder
excel_output_folder = r'C:\path\to\your\folder'

##################################################

kwargs = {
    'depart_from': depart_from.upper(),
    'return_to': return_to.upper(),
    'depart_dt': depart_date,
    'return_dt': return_date,
    'adults': num_adults,
    'children': num_children,
    'infants': num_infants,
    'currency': 'USD',
    'bag_count': num_of_bags,
    'version': 2,
    'passenger_count': (num_adults + num_children + num_infants)
    }



def search_flight(datetime_from=depart_date, datetime_to=return_date, **kwargs):
    """
    Get key flight info based on criteria
    """

    # depart_dt = datetime.strptime(datetime_from, '%m/%d/%Y').strftime('%d/%m/%Y')
    # return_dt = datetime.strptime(datetime_to, '%m/%d/%Y').strftime('%d/%m/%Y')
    depart_dt = datetime.strptime(kwargs['depart_dt'], '%m/%d/%Y').strftime('%d/%m/%Y')
    return_dt = datetime.strptime(kwargs['return_dt'], '%m/%d/%Y').strftime('%d/%m/%Y')

    url = 'https://api.skypicker.com/flights?'

    param_str = '?flyFrom={a}&to={b}'.format(a = kwargs['depart_from'], b = kwargs['return_to'])
    param_str += '&dateFrom={a}&dateTo={b}'.format(a = depart_dt, b = return_dt)
    param_str += '&adults={a}&children={a}'.format(a = kwargs['adults'],b = kwargs['children'],)
    param_str += '&infants={a}&curr={b}'.format(a = kwargs['infants'],b = kwargs['currency'],)


    resp = requests.get(os.path.join(url, param_str)).json()
    flights = []
    for flight in resp.get('data'):
        flight_info = {
            'booking_token': flight.get('booking_token'),
            'departure': datetime.utcfromtimestamp(flight.get('dTimeUTC')),
            'arrival': datetime.utcfromtimestamp(flight.get('aTimeUTC')),
            # 'arrival': datetime.utcfromtimestamp(flight.get('aTimeUTC')).strftime('%Y-%m-%d %H:%M'),
            'price': flight.get('price'),
            'currency': resp.get('currency'),
            'distance': flight['distance'],
            'legs': []
        }
        flight_info['duration_days'] = flight_info['arrival'] - flight_info['departure']
        flight_info['duration_hrs'] = (flight_info['duration_days'].total_seconds() / 60.0) / 60.0
        # flight_info
        for route in flight['route']:
            flight_info['legs'].append({
                'carrier': route['airline'],
                'departure': datetime.utcfromtimestamp(route.get('dTimeUTC')),
                'arrival': datetime.utcfromtimestamp(route.get('aTimeUTC')),
                'from': '{} ({})'.format(route['cityFrom'], route['flyFrom']),
                'to': '{} ({})'.format(route['cityTo'], route['flyTo']),
                })
        flight_info['carrier'] = ', '.join(set([c.get('carrier') for c in flight_info['legs']]))
        flights.append(flight_info)

    return flights



def parse_flight_data(results):
    """
    Process flight data
    """
    tmp_df = pd.DataFrame(results)
    tmp_df['num_stops'] = tmp_df['legs'].map(lambda x: len(x) - 1)
    tmp_df['price'] = tmp_df['price'].astype(float)
    tmp_df['duration_hrs'] = tmp_df['duration_hrs'].astype(float)
    return tmp_df



def get_tokens(flight_list):
    """
    Create list of booking tokens to retrieve booking info.
    """
    return [i['booking_token'] for i in flight_list]




def flight_booking_info(booking_token, **kwargs):
    """
    Look up booking info based on booking token.
    """
    booking_params = {
        'v': kwargs['version'],
        'pnum': kwargs['passenger_count'],
        'bnum':kwargs['bag_count'],
        'booking_token': booking_token
        }

    bookings_json = requests.get('https://booking-api.skypicker.com/api/v0.1/check_flights', params = booking_params).json()

    data_dict = {
        'booking_token':booking_token,
        'book_fee':bookings_json['book_fee'],
        'adults_price':bookings_json['adults_price'],
        'flights_price':bookings_json['flights_price'],
        'bags_fee':bookings_json['bags_fee'],
        'flight_real_price':bookings_json['flight_real_price'],
        'additional_bag_fee':bookings_json['additional_order_baggage_fee'],
        'extra_fee':bookings_json['extra_fee'],
        'total_cost':bookings_json['total'],
        # 'changes': len(bookings_json['flights']),
        }
    for i, flight in enumerate(bookings_json['flights']):
        tmp_name = f'carrier{i+1}'
        data_dict[tmp_name] = flight['operating_airline']['name']
        fb_name = f'fare_basis_{i+1}'
        data_dict[fb_name] = flight['fare_basis']


    cols = [i for i in data_dict.keys()]

    tmp_df = pd.DataFrame.from_dict(list(data_dict.items()))
    df1 = tmp_df.T
    new_cols = df1.loc[0]
    df2 = df1[1:]
    df2.columns = new_cols
    return df2




def max_col_width_dict(dataframe, output_dict=None):
    """
    Get column widths with padding.
    """

    if output_dict is None:
        output_dict = dict()

    max_col_width_dict = {i:int(round(dataframe[i].map(lambda x: len(str(x))).max() * 1.5, 0)) for i in dataframe}
    col_name_width_dict = {i:len(i) for i in dataframe.columns.values.tolist()}

    for i in max_col_width_dict.keys():
        for j in col_name_width_dict.keys():
            if i == j:
                if max_col_width_dict[i] > col_name_width_dict[j]:
                    output_dict[i] = max_col_width_dict[i]
                else:
                    output_dict[j] = col_name_width_dict[j]

    return output_dict



def send_to_excel(df, worksheet_name='FlightData', folder_path=None, file_name=None):
    """
    Output data to Excel workbook.

    Note: Will need to define output path or the file will land on a user's desktop.
    """
    if folder_path is None:
        folder_path = r'C:\Users\{}\Desktop'.format(getuser())
    if file_name is None:
        file_name = 'GRBA_812_Raw_Flight_Data_{}.xlsx'.format(datetime.today().strftime('%Y-%m-%d'))


    xl_path = os.path.join(folder_path, file_name)
    xl_writer = pd.ExcelWriter(xl_path, engine = 'xlsxwriter')

    df.to_excel(xl_writer, sheet_name = worksheet_name, index = False, startrow = 1, header = False)

    workbook  = xl_writer.book
    worksheet = xl_writer.sheets[worksheet_name]

    header_format = workbook.add_format({
        'bold': False,
        'align': 'center',
        'border': 0})

    col_dict = max_col_width_dict(df)
    for i, v in enumerate(df):
        worksheet.set_column(i, i, col_dict[v])


    for i, val in enumerate(df.columns.values.tolist()):
        worksheet.write(0, i, val, header_format)

    xl_writer.save()



if __name__ == '__main__':

    while True:
        print('Retrieving flights data...')
        flight_data_list = search_flight(**kwargs)
        flight_df = parse_flight_data(flight_data_list)
        print('Done!', flush = True)
        break
    data_tokens = get_tokens(flight_data_list)

    while True:
        print('Retrieving bookings data...')
        dfs = [flight_booking_info(i, **kwargs) for i in data_tokens]
        # bookings_df = pd.concat(dfs, ignore_index=True, sort=False).reset_index(drop=True)
        bookings_df = pd.concat(dfs, ignore_index=True, sort=False)
        print('Done!', flush = True)
        break

    while True:

        rename_cols = {
            'carrier1':'carrier 1 name',
            'carrier2': 'carrier 2 name',
            'carrier3': 'carrier 3 name',
            'carrier4': 'carrier 4 name',
            }

        print(f'Conducting final processing and sending to Excel...')
        full_df = pd.merge(flight_df, bookings_df, on='booking_token')
        output_df = full_df.drop(['booking_token','legs'], axis=1)
        output_df['ID'] = output_df.index.values + 1
        output_df.rename(columns=rename_cols, inplace=True)
        output_df['carrier 1'] = output_df['carrier'].str.split(',', expand=True)[0]
        if len(output_df['carrier'].str.split(',', expand=True).columns.values.tolist()) == 2:
            output_df['carrier 2'] = output_df['carrier'].str.split(',', expand=True)[1]
        else:
            output_df['carrier 2'] = None
        if len(output_df['carrier'].str.split(',', expand=True).columns.values.tolist()) == 3:
            output_df['carrier 3'] = output_df['carrier'].str.split(',', expand=True)[2]
        else:
            output_df['carrier 3'] = None
        output_df['depart_hub'] = depart_from.upper()
        output_df['arrive_hub'] = return_to.upper()
        output_df['Arrival_Date'] = pd.to_datetime(output_df['arrival']).dt.strftime('%Y-%m-%d')
        output_df['Departure_Date'] = pd.to_datetime(output_df['departure']).dt.strftime('%Y-%m-%d')
        
        output_df['Adults'] = num_adults
        output_df['Children'] = num_children
        output_df['Infants'] = num_infants
        output_df['Bag_Count'] = 4

        output_df = output_df.drop('carrier', axis=1)


        try:
            output_df = output_df.replace('', np.NaN)
        except ValueError:
            try:
                output_df = output_df.replace('', np.NaT)
            except ValueError:
                pass


        new_col_order = [
            'ID',
            'carrier 1',
            'carrier 2',
            'carrier 3',
            'arrival',
            'departure',
            'distance',
            'duration_days',
            'duration_hrs',
            'num_stops',
            'price',
            'book_fee',
            'adults_price',
            'flights_price',
            'bags_fee',
            'flight_real_price',
            'additional_bag_fee',
            'extra_fee',
            'total_cost',
            'depart_hub',
            'arrive_hub',
            'Arrival_Date',
            'Departure_Date',
            'Adults',
            'Children',
            'Infants',
            'Bag_Count',
            'carrier 1 name',
            'fare_basis_1',
            'carrier 2 name',
            'fare_basis_2',
            'carrier 3 name',
            'fare_basis_3',
            'carrier 4 name',
            'fare_basis_4',
            ]

        output_df = output_df.reindex(columns = new_col_order)

        send_to_excel(df=output_df, folder_path=excel_output_folder)
        print('Done!', flush=True)
        break
