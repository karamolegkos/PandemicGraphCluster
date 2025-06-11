import csv

def normalise(value, min_value, max_value):
  return (value - min_value) / (max_value - min_value)

# Function to return zero if a string is ''
def zero_or_int_value(given_str):
  return int(given_str) if given_str != '' else 0

# Function to return zero if a string is ''
def zero_or_int_valueNA(given_str):
  return int(given_str) if given_str != 'NA' else 0

def gatherVaccines():
  # Filename
  filename = './data/vaccins.csv'

  # Make the Headers : Index values
  HEADERS_LINE = [
      'YearWeekISO', 
      'ReportingCountry', 
      'Denominator', 
      'NumberDosesReceived', 
      'NumberDosesExported', 
      'FirstDose', 
      'FirstDoseRefused', 
      'SecondDose', 
      'DoseAdditional1', 
      'DoseAdditional2', 
      'DoseAdditional3', 
      'DoseAdditional4', 
      'DoseAdditional5', 
      'UnknownDose', 
      'Region', 
      'TargetGroup', 
      'Vaccine', 
      'Population'
  ]

  HEADERS = {}
  for i in range(len(HEADERS_LINE)):
    HEADERS[HEADERS_LINE[i]] = i

  # Use this as a hashed table
  hashed_data = {}

  # Parse through the file
  lines_amount = 0
  with open(filename, newline='') as file:
    # Start the reader
    reader = csv.reader(file)

    headers_lines = True

    # For all the rows of the file
    for row in reader:
      # print(row)

      # Avoid the first line (this is the headers)
      if headers_lines:
        headers_lines = False
        continue

      # Count the lines
      lines_amount += 1

      # Find the current key for the hashed table
      year_week_ISO = row[HEADERS['YearWeekISO']]
      year = year_week_ISO[:4]
      week = year_week_ISO[6:8]

      country_code = row[HEADERS['ReportingCountry']]

      key_dictionary = {
          "year" : year,
          "week" : week,
          "country_code" : country_code
      }

      key = tuple(key_dictionary.items())

      # Make the starting value
      value = {
          "FirstDose"        : zero_or_int_value(row[HEADERS['FirstDose']]),
          "FirstDoseRefused" : zero_or_int_value(row[HEADERS['FirstDoseRefused']]),
          "SecondDose"       : zero_or_int_value(row[HEADERS['SecondDose']]),
          "DoseAdditional1"  : zero_or_int_value(row[HEADERS['DoseAdditional1']]),
          "DoseAdditional2"  : zero_or_int_value(row[HEADERS['DoseAdditional2']]),
          "DoseAdditional3"  : zero_or_int_value(row[HEADERS['DoseAdditional3']]),
          "DoseAdditional4"  : zero_or_int_value(row[HEADERS['DoseAdditional4']]),
          "DoseAdditional5"  : zero_or_int_value(row[HEADERS['DoseAdditional5']]),
          "UnknownDose"      : zero_or_int_value(row[HEADERS['UnknownDose']])
      }

      # If the key exists then only update the country
      if key in hashed_data:
        old_value = hashed_data[key]

        # If the key exists then only update the country
        value = {
          "FirstDose"        : zero_or_int_value(row[HEADERS['FirstDose']])        + old_value['FirstDose'],
          "FirstDoseRefused" : zero_or_int_value(row[HEADERS['FirstDoseRefused']]) + old_value['FirstDoseRefused'],
          "SecondDose"       : zero_or_int_value(row[HEADERS['SecondDose']])       + old_value['SecondDose'],
          "DoseAdditional1"  : zero_or_int_value(row[HEADERS['DoseAdditional1']])  + old_value['DoseAdditional1'],
          "DoseAdditional2"  : zero_or_int_value(row[HEADERS['DoseAdditional2']])  + old_value['DoseAdditional2'],
          "DoseAdditional3"  : zero_or_int_value(row[HEADERS['DoseAdditional3']])  + old_value['DoseAdditional3'],
          "DoseAdditional4"  : zero_or_int_value(row[HEADERS['DoseAdditional4']])  + old_value['DoseAdditional4'],
          "DoseAdditional5"  : zero_or_int_value(row[HEADERS['DoseAdditional5']])  + old_value['DoseAdditional5'],
          "UnknownDose"      : zero_or_int_value(row[HEADERS['UnknownDose']])      + old_value['UnknownDose']
        }
      
      # Update the hashed table
      hashed_data.update({key: value})

  # print("Lines parsed:", lines_amount)
  # print("Data Kept   :", len(hashed_data))

  # for key in hashed_data:
  #   print(key, ":", hashed_data[key])
  return hashed_data

def gatherCasesAndDeaths():
  codes3 = ['AUT', 'BEL', 'BGR', 'HRV', 'CYP', 'CZE', 'DNK', 'EST', 'NA', 'FIN', 'FRA', 'DEU', 'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'LVA', 'LIE', 'LTU', 'LUX', 'MLT', 'NLD', 'NOR', 'POL', 'PRT', 'ROU', 'SVK', 'SVN', 'ESP', 'SWE']
  codes2 = ['AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'NA', 'FI', 'FR', 'DE', 'GR', 'HU', 'IS', 'IE', 'IT', 'LV', 'LI', 'LT', 'LU', 'MT', 'NL', 'NO', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE']

  codes = {}
  for i in range(len(codes3)):
    codes[codes3[i]] = codes2[i]

  # Filename
  filename = './data/cases_deaths.csv'

  # Make the Headers : Index values
  HEADERS_LINE = [
      'country', 
      'country_code', 
      'continent', 
      'population', 
      'indicator', 
      'weekly_count', 
      'year_week', 
      'rate_14_day', 
      'cumulative_count', 
      'source', 
      'note'
  ]

  HEADERS = {}
  for i in range(len(HEADERS_LINE)):
    HEADERS[HEADERS_LINE[i]] = i

  # Use this as a hashed table
  hashed_data = {}

  # Parse through the file
  lines_amount = 0
  with open(filename, newline='') as file:
    # Start the reader
    reader = csv.reader(file)

    headers_lines = True

    # For all the rows of the file
    for row in reader:
      # print(row)

      # Avoid the first line (this is the headers)
      if headers_lines:
        headers_lines = False
        continue
      
      # Count the lines
      lines_amount += 1

      # Find the current key for the hashed table
      year_week = row[HEADERS['year_week']]
      year = year_week[:4]
      week = year_week[5:7]

      country_code = row[HEADERS['country_code']]

      key_dictionary = {
          "year" : year,
          "week" : week,
          "country_code" : codes[country_code]
      }

      key = tuple(key_dictionary.items())

      indicator = row[HEADERS['indicator']]

      # Make the starting value
      value = {
          "country"                                     : row[HEADERS['country']],
          "population"                                  : zero_or_int_valueNA(row[HEADERS['population']]),
          row[HEADERS['indicator']]+"_weekly_count"     : zero_or_int_valueNA(row[HEADERS['weekly_count']]),
          row[HEADERS['indicator']]+"_cumulative_count" : zero_or_int_valueNA(row[HEADERS['cumulative_count']])
      }

      if key in hashed_data:
        old_value = hashed_data[key]
        old_value[row[HEADERS['indicator']]+"_weekly_count"] = zero_or_int_valueNA(row[HEADERS['weekly_count']])
        old_value[row[HEADERS['indicator']]+"_cumulative_count"] = zero_or_int_valueNA(row[HEADERS['cumulative_count']])
        value = old_value

      hashed_data.update({key: value})

  # print("Lines parsed:", lines_amount)
  # print("Data Kept   :", len(hashed_data))

  # for key in hashed_data:
  #   print(key, ":", hashed_data[key])
  return hashed_data

# Get the datasets combined and normalised
def get_normal_data():
    # Gather values
    vaccines_data = gatherVaccines()
    cases_deaths_data = gatherCasesAndDeaths()

    # Finalize the data (combine the two datasets)
    final_data = {}
    for key in vaccines_data:
        if key in cases_deaths_data:
            cases_deaths_value = cases_deaths_data[key]
            vaccines_value = vaccines_data[key]

            values = {}
            for key_of_value in cases_deaths_value:
                values[key_of_value] = cases_deaths_value[key_of_value]
            
            for key_of_value in vaccines_value:
                values[key_of_value] = vaccines_value[key_of_value]
            
            final_data[key] = values
    first_value = list(final_data.values())[0]

    # Normalise the data
    population_min = first_value['population']
    population_max = first_value['population']
    cases_weekly_count_min = first_value['cases_weekly_count']
    cases_weekly_count_max = first_value['cases_weekly_count']
    cases_cumulative_count_min = first_value['cases_cumulative_count']
    cases_cumulative_count_max = first_value['cases_cumulative_count']
    deaths_weekly_count_min = first_value['deaths_weekly_count']
    deaths_weekly_count_max = first_value['deaths_weekly_count']
    deaths_cumulative_count_min = first_value['deaths_cumulative_count']
    deaths_cumulative_count_max = first_value['deaths_cumulative_count']
    FirstDose_min = first_value['FirstDose']
    FirstDose_max = first_value['FirstDose']
    FirstDoseRefused_min = first_value['FirstDoseRefused']
    FirstDoseRefused_max = first_value['FirstDoseRefused']
    SecondDose_min = first_value['SecondDose']
    SecondDose_max = first_value['SecondDose']
    DoseAdditional1_min = first_value['DoseAdditional1']
    DoseAdditional1_max = first_value['DoseAdditional1']
    DoseAdditional2_min = first_value['DoseAdditional2']
    DoseAdditional2_max = first_value['DoseAdditional2']
    DoseAdditional3_min = first_value['DoseAdditional3']
    DoseAdditional3_max = first_value['DoseAdditional3']
    DoseAdditional4_min = first_value['DoseAdditional4']
    DoseAdditional4_max = first_value['DoseAdditional4']
    DoseAdditional5_min = first_value['DoseAdditional5']
    DoseAdditional5_max = first_value['DoseAdditional5']
    UnknownDose_min = first_value['UnknownDose']
    UnknownDose_max = first_value['UnknownDose']

    for key in final_data:
        if final_data[key]['population'] < population_min:
            population_min = final_data[key]['population']

        if final_data[key]['population'] > population_max:
            population_max = final_data[key]['population']

        if final_data[key]['cases_weekly_count'] < cases_weekly_count_min:
            cases_weekly_count_min = final_data[key]['cases_weekly_count']

        if final_data[key]['cases_weekly_count'] > cases_weekly_count_max:
            cases_weekly_count_max = final_data[key]['cases_weekly_count']

        if final_data[key]['cases_cumulative_count'] < cases_cumulative_count_min:
            cases_cumulative_count_min = final_data[key]['cases_cumulative_count']

        if final_data[key]['cases_cumulative_count'] > cases_cumulative_count_max:
            cases_cumulative_count_max = final_data[key]['cases_cumulative_count']

        if final_data[key]['deaths_weekly_count'] < deaths_weekly_count_min:
            deaths_weekly_count_min = final_data[key]['deaths_weekly_count']

        if final_data[key]['deaths_weekly_count'] > deaths_weekly_count_max:
            deaths_weekly_count_max = final_data[key]['deaths_weekly_count']

        if final_data[key]['deaths_cumulative_count'] < deaths_cumulative_count_min:
            deaths_cumulative_count_min = final_data[key]['deaths_cumulative_count']

        if final_data[key]['deaths_cumulative_count'] > deaths_cumulative_count_max:
            deaths_cumulative_count_max = final_data[key]['deaths_cumulative_count']

        if final_data[key]['FirstDose'] < FirstDose_min:
            FirstDose_min = final_data[key]['FirstDose']

        if final_data[key]['FirstDose'] > FirstDose_max:
            FirstDose_max = final_data[key]['FirstDose']

        if final_data[key]['FirstDoseRefused'] < FirstDoseRefused_min:
            FirstDoseRefused_min = final_data[key]['FirstDoseRefused']

        if final_data[key]['FirstDoseRefused'] > FirstDoseRefused_max:
            FirstDoseRefused_max = final_data[key]['FirstDoseRefused']

        if final_data[key]['SecondDose'] < SecondDose_min:
            SecondDose_min = final_data[key]['SecondDose']

        if final_data[key]['SecondDose'] > SecondDose_max:
            SecondDose_max = final_data[key]['SecondDose']

        if final_data[key]['DoseAdditional1'] < DoseAdditional1_min:
            DoseAdditional1_min = final_data[key]['DoseAdditional1']

        if final_data[key]['DoseAdditional1'] > DoseAdditional1_max:
            DoseAdditional1_max = final_data[key]['DoseAdditional1']

        if final_data[key]['DoseAdditional2'] < DoseAdditional2_min:
            DoseAdditional2_min = final_data[key]['DoseAdditional2']

        if final_data[key]['DoseAdditional2'] > DoseAdditional2_max:
            DoseAdditional2_max = final_data[key]['DoseAdditional2']

        if final_data[key]['DoseAdditional3'] < DoseAdditional3_min:
            DoseAdditional3_min = final_data[key]['DoseAdditional3']

        if final_data[key]['DoseAdditional3'] > DoseAdditional3_max:
            DoseAdditional3_max = final_data[key]['DoseAdditional3']

        if final_data[key]['DoseAdditional4'] < DoseAdditional4_min:
            DoseAdditional4_min = final_data[key]['DoseAdditional4']

        if final_data[key]['DoseAdditional4'] > DoseAdditional4_max:
            DoseAdditional4_max = final_data[key]['DoseAdditional4']

        if final_data[key]['DoseAdditional5'] < DoseAdditional5_min:
            DoseAdditional5_min = final_data[key]['DoseAdditional5']

        if final_data[key]['DoseAdditional5'] > DoseAdditional5_max:
            DoseAdditional5_max = final_data[key]['DoseAdditional5']

        if final_data[key]['UnknownDose'] < UnknownDose_min:
            UnknownDose_min = final_data[key]['UnknownDose']

        if final_data[key]['UnknownDose'] > UnknownDose_max:
            UnknownDose_max = final_data[key]['UnknownDose']
    
    normalised_data = {}
    for key in final_data:
        values = {
            'country'                 : final_data[key]['country'],
            'population'              : normalise(final_data[key]['population'], population_min, population_max),
            'cases_weekly_count'      : normalise(final_data[key]['cases_weekly_count'], cases_weekly_count_min, cases_weekly_count_max),
            'cases_cumulative_count'  : normalise(final_data[key]['cases_cumulative_count'], cases_cumulative_count_min, cases_cumulative_count_max),
            'deaths_weekly_count'     : normalise(final_data[key]['deaths_weekly_count'], deaths_weekly_count_min, deaths_weekly_count_max),
            'deaths_cumulative_count' : normalise(final_data[key]['deaths_cumulative_count'], deaths_cumulative_count_min, deaths_cumulative_count_max),
            'FirstDose'               : normalise(final_data[key]['FirstDose'], FirstDose_min, FirstDose_max),
            'FirstDoseRefused'        : normalise(final_data[key]['FirstDoseRefused'], FirstDoseRefused_min, FirstDoseRefused_max),
            'SecondDose'              : normalise(final_data[key]['SecondDose'], SecondDose_min, SecondDose_max),
            'DoseAdditional1'         : normalise(final_data[key]['DoseAdditional1'], DoseAdditional1_min, DoseAdditional1_max),
            'DoseAdditional2'         : normalise(final_data[key]['DoseAdditional2'], DoseAdditional2_min, DoseAdditional2_max),
            'DoseAdditional3'         : normalise(final_data[key]['DoseAdditional3'], DoseAdditional3_min, DoseAdditional3_max),
            'DoseAdditional4'         : normalise(final_data[key]['DoseAdditional4'], DoseAdditional4_min, DoseAdditional4_max),
            'DoseAdditional5'         : normalise(final_data[key]['DoseAdditional5'], DoseAdditional5_min, DoseAdditional5_max),
            'UnknownDose'             : normalise(final_data[key]['UnknownDose'], UnknownDose_min, UnknownDose_max)
        }

        normalised_data[key] = values
    
    # for key in normalised_data:
    #     print(key, ":", normalised_data[key])
    
    return normalised_data