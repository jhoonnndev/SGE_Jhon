
from odoo.tests.common import TransactionCase

# pruebas para validar que Odoo bloquea correctamente la creación de una sesión si metemos datos ilógicos (por ejemplo, si ponemos al instructor como alumno).
class TestOpenAcademySession(TransactionCase):

    def test_01_instructor_cannot_be_attendee(self):
        """Test that an instructor cannot be an attendee of his own session."""
        # Creamos un instructor
        instructor = self.env['res.partner'].create({
            'name': 'John Doe',
            'instructor': True,
        })
        # Creamos una sesión con ese instructor
        session = self.env['openacademy.session'].create({
            'name': 'Session 1',
            'instructor_id': instructor.id,
        })
        # Intentamos añadir al instructor como asistente
        with self.assertRaises(Exception):
            session.attendee_ids = [(4, instructor.id)]

    # Comprueba que salta error si el instructor está en la lista de asistentes
    def test_02_instructor_cannot_be_attendee_on_creation(self):
        """Test that an instructor cannot be an attendee of his own session on creation."""
        # Creamos un instructor
        instructor = self.env['res.partner'].create({
            'name': 'Jane Doe',
            'instructor': True,
        })
        # Intentamos crear una sesión con ese instructor y añadirlo como asistente
        with self.assertRaises(Exception):
            self.env['openacademy.session'].create({
                'name': 'Session 2',
                'instructor_id': instructor.id,
                'attendee_ids': [(4, instructor.id)],
            })

    #omprueba el onchange de los asientos (asientos negativos o más alumnos que asientos)
    def test_03_seats_onchange(self):
        """Test that the onchange method for seats works correctly."""
        # Creamos una sesión sin instructor
        session = self.env['openacademy.session'].create({
            'name': 'Session 3',
            'seats': 10,
        })
        # Probamos a poner un número de asientos negativo
        session.seats = -5
        self.assertEqual(session.seats, 0, "Seats should be set to 0 if a negative value is given.")
        # Probamos a poner un número de asientos menor que el número de asistentes
        attendee = self.env['res.partner'].create({
            'name': 'Attendee 1',
        })
        session.attendee_ids = [(4, attendee.id)]
        session.seats = 0
        self.assertEqual(session.seats, 1, "Seats should be set to the number of attendees if it's less than that.")