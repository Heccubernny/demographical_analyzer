import pandas as pd 

def calculate_demographic_data(print_data = True):
	df = pd.read_csv('adult.data.csv')

	#Amount of people with each race
	count_race = df['race'].value_counts()

	# Average age of men
	average_age_of_men = round(df[df.sex == "Male"].age.mean(), 1)

	#percentage of people who have a Bachelor's degree
	percentage_of_bachelor_degree_holder = round(100*df[df.education == 'Bachelors'].size/df.size, 1)
	percentage_of_advance_education = df[df.education.isin(["Bachelors", "Masters", "Doctorate"])]
	more_than_fifty = percentage_of_advance_education[percentage_of_advance_education.salary == ">50K"]
	percentage_of_lower_education = df[~df.education.isin(["Bachelors", "Masters", "Doctorate"])]
	l_more_than_fifty = percentage_of_lower_education[percentage_of_lower_education.salary == ">50K"]

	# Percentage with higher education that earn >50K
	advance_education = round(((more_than_fifty.size/percentage_of_advance_education.size)*100),1)

	# Percentage without higher education that earn >50K
	lower_education = round(((l_more_than_fifty.size/percentage_of_lower_education.size)*100),1)
	min_hour_per_week = df["hours-per-week"].min()
	min_workers = df[df['hours-per-week'] == min_hour_per_week]
	min_workers_percentage = round(100*min_workers[min_workers.salary == ">50k"].size/min_workers.size,1)

	# country has the highest percentage of people that earn >50K
	per_country_with_higher = 100*df[df.salary == ">50k"]['native-country'].value_counts()/df['native-country'].value_counts(dropna = False)

	#print the country with highest percentage
	high_earning_country = per_country_with_higher.idxmax()
	
	per_high_earning_country = round(per_country_with_higher[high_earning_country], 1)
	occupation_in_India = df[df['native-country'] == 'India']
	popular_occupation_in_India = occupation_in_India[occupation_in_India.salary == '>50k'].occupation.value_counts().idxmax()


	print(df)
	print(count_race)
	print(average_age_of_men)
	print(f'{percentage_of_bachelor_degree_holder},"%"')
	print(advance_education,'%')
	print(lower_education, '%')
	print(min_hour_per_week,"hours/week")
	print(min_workers_percentage,"%")
	print('Country: ',high_earning_country)
	print(per_high_earning_country,'%')
	print('Popular Occupation: ',popular_occupation_in_India)


calculate_demographic_data()