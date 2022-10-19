from employees.employee import Employee


class Caelum(Employee):
    def show_tasks(self):
        print('You did a lot, Caelumer')

    def search_for_courses_of_the_month(self, month=None):
        print(f'Showing courses - {month}' if month else 'Showing courses of this month')
