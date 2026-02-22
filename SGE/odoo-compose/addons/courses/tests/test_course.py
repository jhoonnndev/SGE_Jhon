from odoo.tests import TransactionCase, tagged


@tagged('test_local')
class TestCourse(TransactionCase):
    def test_some_action(self):

        record = self.env['course.course']
            .create({'nombre': 'value',
                     'duration': 10,
                        'min_age': 18,
                            'price': 100,
                            'amount_discount': 20

                     })

        # with self.assertQueryCount(11):
        #     record.calculate_total_price()

        self.assertEqual(record.total_price, 80)


@tagged('test_local')
class TestStudent(TransactionCase):

    @classmethod
    def setUpClass(cls):
        # add env on cls and many other things
        super(TestStudent, cls).setUpClass()

        cls.students = cls.env['course.student'].create([
            {'name': 'gorka', 'dni': '12345678A', 'age': 14},
            {'name': 'ana sanz', 'dni': '87654321B', 'age': 20},
        ])

    def test_raises_error_under_age(self):
        record = self.env['course.student']
            .create({'name': 'value',
                     'dni': '12345678A',
                        'age': 14
                     })

        with self.assertRaises(ValidationError):
            record._check_minimum_age()

    def test_creation_area(self):
        pass
        # self.students = 20
        # self.assertRecordValues(self.properties, [
        #    {'name': ..., 'total_area': ...},
        #    {'name': ..., 'total_area': ...},
        # ])


    def test_compute_email(self):
        """Test that everything behaves like it should when selling a property."""
        self.students._compute_email()
        self.assertRecordValues(self.students  , [
           {'name': 'gorka', 'email': 'gorka@example.com'},
           {'name': 'ana sanz', 'email': 'ana.sanz@example.com'},
        ])

  
