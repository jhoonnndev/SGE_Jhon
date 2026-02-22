from odoo.tests import TransactionCase,tagged

class TestPaciente(TransactionCase):

    def setUp(self):
        super(TestPaciente, self).setUp()
        self.hospital = self.env['examen.hospital'].create({
            'name': 'Hospital General',
            'urgencias': True,
        })
        self.paciente = self.env['examen.paciente'].create({
            'name': 'Juan Perez',
            'hospital_id': self.hospital.id,
        })

    def test_create_paciente(self):
        self.assertEqual(self.paciente.name, 'Juan Perez')
        self.assertEqual(self.paciente.hospital_id, self.hospital)

    def test_paciente_hospital_relation(self):
        self.assertEqual(self.paciente.hospital_id.name, 'Hospital General')

    def test_paciente_name_required(self):
        with self.assertRaises(Exception):
            self.env['examen.paciente'].create({
                'hospital_id': self.hospital.id,
            })

    def test_paciente_hospital_link(self):
        hospital2 = self.env['examen.hospital'].create({
            'name': 'Hospital de Especialidades',
            'urgencias': False,
        })
        self.paciente.hospital_id = hospital2
        self.assertEqual(self.paciente.hospital_id, hospital2)