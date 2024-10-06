import unittest
import yaml
import datetime as dt

class TestYAMLFiles(unittest.TestCase):

    def setUp(self):
        # This method is executed before each test, loading the YAML files.
        with open('gsoc.yml', 'r') as file:
            self.gsoc_data = yaml.load(file, Loader=yaml.BaseLoader)

        with open('gsoc_times.yml', 'r') as file:
            self.gsoc_times = yaml.load(file, Loader=yaml.BaseLoader)

    def test_gsoc_structure(self):
        # This function tests that gsoc.yml follows the expected structure.
        for season, students in self.gsoc_data.items():
            self.assertTrue(season.startswith('gsoc'), "Season does not start with 'gsoc'")
            for student, props in students.items():
                self.assertIn('rss_feed', props, f"Student {student} missing 'rss_feed'")
                self.assertIn('project', props, f"Student {student} missing 'project'")
                self.assertTrue(props['rss_feed'].startswith('http'), f"Invalid RSS feed for {student}")

    def test_gsoc_times_structure(self):
        # This function tests that gsoc_times.yml has the expected format.
        for student, date_str in self.gsoc_times.items():
            try:
                dt.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                self.fail(f"Date format is incorrect for {student}: {date_str}")
    
    def test_yaml_loads_without_error(self):
        # This function tests if the YAML files are loading correctly.
        try:
            with open('gsoc.yml', 'r') as file:
                yaml.load(file, Loader=yaml.BaseLoader)
        except yaml.YAMLError as exc:
            self.fail(f"gsoc.yml failed to load: {exc}")

        try:
            with open('gsoc_times.yml', 'r') as file:
                yaml.load(file, Loader=yaml.BaseLoader)
        except yaml.YAMLError as exc:
            self.fail(f"gsoc_times.yml failed to load: {exc}")

if __name__ == '__main__':
    unittest.main()
