import pandas as pd
from io import StringIO


def build_report(data, asc=None):
    """Return list of drivers results:
        [
         {'driver': 'Sebastian Vettel',
            'car': 'FERRARI',
            'start': Timestamp('2018-05-24 12:02:58.917000'),
            'end': Timestamp('2018-05-24 12:04:03.332000'),
            'time': Timedelta('0 days 00:01:04.415000'),
            'result': '1:04.415'
            'position': 1},
         {'driver': 'Valtteri Bottas',
             'car': 'MERCEDES',
             'start': Timestamp('2018-05-24 12:00:00'),
             'end': Timestamp('2018-05-24 12:01:12.434000'),
             'time': Timedelta('0 days 00:01:12.434000'),
             'result': '1:12.434'
             'position': 2},]"""

    # Reading data

    abb_df = pd.read_csv(
        StringIO(data['abb']), sep='_', header=None,
        names=['abbreviation', 'driver', 'car'])

    abb_df.set_index('abbreviation', inplace=True)

    start_df = pd.read_csv(
        StringIO(data['start']), sep='_', header=None,
        names=['abbreviation', 'data_start', 'time_start'])

    start_df.set_index('abbreviation', inplace=True)

    end_df = pd.read_csv(
        StringIO(data['end']), sep='_', header=None,
        names=['abbreviation', 'data_end', 'time_end'])

    end_df.set_index('abbreviation', inplace=True)

    # Columns filling

    main_df = abb_df.join(start_df).join(end_df)

    main_df['start'] = main_df["data_start"] + ' ' + main_df["time_start"]
    main_df['start'] = pd.to_datetime(main_df['start'], errors='coerce', format='')

    main_df['end'] = main_df["data_end"] + ' ' + main_df["time_end"]
    main_df['end'] = pd.to_datetime(main_df['end'], errors='coerce', format='')

    main_df['time'] = main_df['end'] - main_df['start']
    main_df.loc[main_df['start'] >= main_df['end'], 'time'] = float('nan')

    main_df['result'] = main_df['time'].astype(str).str.replace('0 days 00:0', '').str.slice(stop=-3)
    main_df.loc[pd.isna(main_df['time']), 'result'] = 'Disqualified'

    # Column Position filling

    main_df.sort_values(by=['time'], inplace=True, na_position='last')
    main_df['position'] = 0

    position = 0
    last_time = 0

    for index, row in main_df.iterrows():
        if row['time'] != last_time:
            position += 1
            last_time = row['time']
        main_df.loc[index, 'position'] = position

    # Sorting by settings

    if asc is None:
        main_df.sort_values(by=['time'], inplace=True)
    else:
        main_df.sort_values(by=['driver'], ascending=asc, inplace=True)

    report = main_df.to_dict('records')

    return report


def print_report(report, driver, show_line=False):
    """
    Output for "build_report" function
    """
    if driver is None:

        if len(report):

            print(f'{"N": <3} | {"DRIVER": <20} | {"CAR": <30} | {"BEST LAP": <30}')
            print('-'*70)

            for record in report:
                if show_line and record['position'] > 15:
                    show_line = False
                    print('-'*70)
                print(f'{str(record["position"])+".": <3} | {record["driver"]: <20} | {record["car"]: <30} | {record["result"]}')
        else:
            print('Report is empty!')

    else:

        records = [x for x in report if x["driver"] == driver]
        if len(records):
            record = records[0]

            if record['time'] is None:
                race_result = 'Disqualified'
            else:
                race_result = str(record['time'])[:-3][11:]

            message = f"""
                Driver: {record["driver"]}
                Car: {record["car"]}
                Position: {record["position"]}
    
                Best lap:
                    start - {record["start"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}
                    end   - {record["end"].strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}
                    result: {record["result"]}"""

            print(message.replace('\t', ''))
        else:
            print('Driver not found!')
