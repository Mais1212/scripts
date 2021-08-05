from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)


def check_for_exist(kid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=kid_name)
    except Schoolkid.DoesNotExist:
        print("Вероятно, вы ввели имя несуществующего ученика, попробуйте еще раз.")
        return None
    return schoolkid


def fix_marks(kid_name):
    schoolkid = check_for_exist(kid_name)
    if schoolkid is None:
        return
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    if not bad_marks:
        print("Скорее всего, вы ввели имя ученика, у которого нет плохих оценок")
        return
    for bad_mark in bad_marks:
        bad_mark.points = 5
        bad_mark.save()
    print("Оценки исправлены!")


def remove_chastisements(kid_name):
    schoolkid = check_for_exist(kid_name)
    if schoolkid is None:
        return
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    if not chastisements:
        print(
            "Скорее всего, вы ввели имя ученика, у которого нет замечаний.")
        return
    chastisements.delete()
    print("Замечания удалены!")


def append_commendation(subject, kid_name):
    lesson = Lesson.objects.filter(
        year_of_study=6, group_letter="А", subject__title=subject).first()
    if lesson is None:
        print("Возможно, вы ошиблись в названии предмета")
        return
    date = lesson.date
    teacher = lesson.teacher
    subject = lesson.subject
    schoolkid = check_for_exist(kid_name)
    if schoolkid is None:
        return
    Commendation.objects.create(text="Ты натренировался, брат.",
                                created=date, schoolkid=schoolkid,
                                teacher=teacher, subject=subject)
    print("Похвала добавлена!")
