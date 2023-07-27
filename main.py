from faker import Faker
from datetime import datetime, timedelta
from collections import defaultdict


# create a test_list
users = []
fake = Faker()
# Faker.seed(0)
for i in range(1,96):
    user_dict = {}
    user_dict['num'] = i
    user_dict['name'] = fake.name()
    user_dict['birthday'] = fake.date()
    users.append(user_dict)
    # print(user_dict)


def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    if current_date.weekday() < 5:
        start_period = current_date + timedelta(days=5-current_date.weekday())
        return (start_period.date()), (start_period + timedelta(6)).date()


def get_birthdays_per_week(employes: list) -> None:
    result = defaultdict(list)
    current_year = datetime.now().year
    for i in employes:
        bd = (i['birthday'])
        bd = datetime.strptime(bd, '%Y-%m-%d').date()
        bd = bd.replace(year=current_year)
        start, end = get_period()
        if start <= bd <= end:
            if bd.weekday() in (5, 6):
                # result[bd].append(i['name'])
                result['Monday'].append(i['name'])
                continue
            else:
                # result[bd].append(i['name'])
                result[bd.strftime('%A')].append(i['name'])
                continue
        else:
            continue
    return result


if __name__ =='__main__':
    print(get_birthdays_per_week(users))
