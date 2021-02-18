from api_pallada import API
from apps.user.services import utils
from typing import Optional


def get_marks(api: API) -> dict:
    tmp_result = dict()

    tmp = api.search_read(
        'portfolio_science.grade_view',
        [[['ID_student', '!=', '']]],
        {'fields': ['discipline', 'grade', 'term']},
    )
    for discipline in tmp:
        term = discipline['term'].strip()
        mark = discipline['grade'].split('/')[0].strip()
        if term in tmp_result:
            tmp_result[term].append({
                'name': discipline['discipline'].strip(),
                'mark': mark,
            })
        else:
            tmp_result[term] = [{
                'name': discipline['discipline'].strip(),
                'mark': mark,
            }]

    result = []
    for term in sorted(tmp_result.keys()):
        result.append({
            'term': term,
            'items': sorted(tmp_result[term], key=lambda x: x['mark']),
        })
    return result


def get_gradebook(api: API) -> Optional[str]:
    response = api.search_read(
        'portfolio_science.grade_attistation_view',
        [[['nzkn', '!=', '']]],
        {'limit': 10},
    )
    if not len(response):
        return None
    for i in response:
        if nzkn := i.get('nzkn'):
            return nzkn


def get_fio_group_and_average(api: API) -> tuple:
    tmp = api.search_read(
        'portfolio_science.grade_view',
        [[['ID_student', '!=', '']]],
        {'fields': ['ID_student', 'display_name', 'grade']},
    )

    average = 0
    count = 0

    for i in tmp:
        if not i['grade'][0].isdigit():
            continue
        average += int(i['grade'][0])
        count += 1

    average = round(average / count, 2)

    return tmp[0]['ID_student'], tmp[0]['display_name'], average


def get_data(api: API) -> dict:
    gradebook = get_gradebook(api)
    gradebook = gradebook if gradebook else api.login

    fio, group, average = get_fio_group_and_average(api)
    token = utils.make_token(fio, gradebook, group)

    utils.update_or_create_user(token, group, average)

    return {
        'token': token,
        'FIO': fio,
        'averga': average,
        'group': group,
        'zachotka': gradebook,
    }
