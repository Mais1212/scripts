from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)


def fix_marks(kid_name):
    bad_marks = Mark.objects.filter(
        schoolkid__full_name__contains=kid_name, points__in=[2, 3])
    if not bad_marks:
        print("Скорее всего, вы ввели имя ученика, у которого нет плохих оценок или такого имени.")
        return
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()
    print("Оценки исправлены!")


def remove_chastisements(kid_name):
    chastisements = Chastisement.objects.filter(
        schoolkid__full_name__contains=kid_name)
    if not chastisements:
        print(
            "Скорее всего, вы ввели имя ученика, у которого нет замечания или такого имени.")
        return
    chastisements.delete()
    print("Замечания удалены!")


def append_commendation(subject, kid_name):
    try:
        lesson = Lesson.objects.filter(
            year_of_study=6, group_letter="А", subject__title=subject).first()
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
    except Schoolkid.DoesNotExist:
        print("Вероятно, вы ввели имя несуществующего ученика, попробуйте еще раз.")
    finally:
        print("Похвала добавлена!")
