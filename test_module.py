import unittest
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data = False)

    def test_count_race(self):
        actual = self.data['count_race'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertAlmostEqual(actual, expected, "Expected race count values to be [27816, 3124, 1039, 311, 271]")
    
    def test_average_age_of_men(self):
        actual = self.data['average_age_of_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, "Expected different value for average age of men.")

    def test_percentage_of_bachelor_degree_holder(self):
        actual = self.data['percentage_of_bachelor_degree_holder']
        expected = 16.4 
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage with Bachelors degrees.")

    def test_advance_education(self):
        actual = self.data['advance_education']
        expected = 46.5
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage with higher education that earn >50K.")
  
    def test_lower_education(self):
        actual = self.data['lower_education']
        expected = 17.4
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage without higher education that earn >50K.")

    def test_min_hour_per_week(self):
        actual = self.data['min_hour_per_week']
        expected = 1
        self.assertAlmostEqual(actual, expected, "Expected different value for minimum work hours.")     

    def test_min_workers_percentage(self):
        actual = self.data['min_workers_percentage']
        expected = 10
        self.assertAlmostEqual(actual, expected, "Expected different value for percentage of rich among those who work fewest hours.")   

    def test_high_earning_country(self):
        actual = self.data['high_earning_country']
        expected = 'Iran'
        self.assertAlmostEqual(actual, expected, "Expected different value for highest earning country.")   

    def test_per_high_earning_country(self):
        actual = self.data['per_high_earning_country']
        expected = 41.9
        self.assertAlmostEqual(actual, expected, "Expected different value for heighest earning country percentage.")   

    def test_popular_occupation_in_India(self):
        actual = self.data['popular_occupation_in_India']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected, "Expected different value for top occupations in India.")      

if __name__ == "__main__":
    unittest.main()
