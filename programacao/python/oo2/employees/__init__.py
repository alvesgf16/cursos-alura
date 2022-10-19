from employees.intermediate import Intermediate
from employees.junior import Junior

jose = Junior('José')
jose.search_for_unanswered_questions()

luan = Intermediate('Luan')
luan.search_for_unanswered_questions()
luan.search_for_courses_of_the_month()

luan.show_tasks()

print(luan)
