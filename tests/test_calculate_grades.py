import unittest
from unittest.mock import patch, call
import pytest
from calculate_grades import *

class TestCalculateGrades(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup_capturing_output(self, capsys):
        self.capsys = capsys

    @patch('builtins.input', side_effect=['100', '90', '80', '70', '60'])
    def test_read_input_with_valid_input(self, mock_input):
        expected_grades = [100, 90, 80, 70, 60]
        result = read_input()
        self.assertEqual(result, expected_grades)

    def test_read_input_with_non_numerical_input(self):
        with patch('builtins.input', side_effect=['a', '1', '2', '3', '4']):
            grade_list = read_input()
            captured_output = self.capsys.readouterr()
            assert "You need to enter a number!\n" in captured_output.out
            assert grade_list == [1, 2, 3, 4]

    def test_calculate_stat_with_valid_grades(self):
        grades = [100, 90, 80, 70, 60]
        mean, sd = calculate_stat(grades)
        self.assertEqual(mean, 80)
        self.assertAlmostEqual(sd, 14.142, places=2)

    @patch('builtins.print')
    def test_print_stat_output_format(self, mock_print):
        mean, sd = 80, 14.142
        print_stat(mean, sd)
        mock_print.assert_has_calls([
            call('****** Grade Statistics ******'),
            call("The grades's mean is:", 80),  # Update the expected string here
            call('The population standard deviation of grades is: ', 14.142),
            call('****** END ******'),
        ])


    @patch('calculate_grades.read_input', return_value=[100, 90, 80, 70, 60])
    @patch('calculate_grades.calculate_stat', return_value=(80, 15.811))
    @patch('calculate_grades.print_stat')
    def test_display_grade_stat_integration(self, mock_print_stat, mock_calculate_stat, mock_read_input):
        display_grade_stat()
        mock_read_input.assert_called_once()
        mock_calculate_stat.assert_called_once_with([100, 90, 80, 70, 60])
        mock_print_stat.assert_called_once_with(80, 15.811)

if __name__ == "__main__":
    unittest.main()