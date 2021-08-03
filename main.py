from django.core.exceptions import ObjectDoesNotExist
from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)


# Исправить все плохие оценки
def fix_marks(kid_name):
    bad_marks = Mark.objects.filter(
        schoolkid__full_name__contains=kid_name, points__in=[2, 3])
    if bad_marks.count() == 0:
        print("Скорее всего, вы ввели имя ученика, у которого нет плохих оценок или такого имени.")
        return
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()
    print("Оценки исправлены!")


# Удалить все замечания
def remove_chastisements(kid_name):
    chastisements = Chastisement.objects.filter(
        schoolkid__full_name__contains=kid_name)
    if chastisements.count() == 0:
        print("Скорее всего, вы ввели имя ученика, у которого нет замечания или такого имени.")
        return
    chastisements.delete()
    print("Замечания удалены!")


# Получить похвалу от учителя
def append_commendation(subject, kid_name):
    try:
        lesson = Lesson.objects.filter(
            year_of_study=6, group_letter="А", subject__title=subject)[0]
    except IndexError:
        print("Возможно, вы ошиблись в названии предмета")
        return
    date = lesson.date
    teacher = lesson.teacher
    subject = lesson.subject
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
        Commendation.objects.create(text="Ты натренировался, брат.",
                                    created=date, schoolkid=schoolkid,
                                    teacher=teacher, subject=subject)
    except ObjectDoesNotExist:
        print("Вероятно, вы ввели имя несуществующего ученика, попробуйте еще раз.")
    finally:
        print("Похвала добавлена!")
