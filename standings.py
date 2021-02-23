import requests
import bs4
import re

URL = 'https://www.formula1.com/en/results.html/{}/{}.html'
URL_calendar = 'https://www.formula1.com/en/racing/{}.html'


def standings_check(request, year=2021):
    full_page = requests.get(URL.format(year, request))
    return_string = ""
    BsObj = bs4.BeautifulSoup(full_page.content, features="html.parser")
    if request == 'drivers':
        first_names = BsObj.findAll("span", {"class": "hide-for-tablet"})
        second_names = BsObj.findAll("span", {"class": "hide-for-mobile"})
        teams = BsObj.findAll("a", {"class": "grey semi-bold uppercase ArchiveLink"})
        points = BsObj.findAll("td", {"class": "dark bold"})
        return_string += f"Личный зачет для {year} года: \n"
        for r, i, j, k, l in zip(range(1, 22), first_names, second_names, teams, points):
            full_name_driver = i.getText() + ' ' + j.getText()
            full_name_team = ' '.join(k.getText().split(' ')[0:2])
            return_string += str(r) + '. ' + full_name_driver + ' (' + l.getText() + ') - ' + full_name_team + '\n'

    elif request == 'team':
        teams = BsObj.findAll("a", {"class": "dark bold uppercase ArchiveLink"})
        points = BsObj.findAll("td", {"class": "dark bold"})
        return_string += f"Кубок конструкторов для {year} года: \n"
        for r, i, j in zip(range(1, 22), teams, points):
            full_name_team = ' '.join(i.getText().split(' ')[0:2])
            return_string += str(r) + '. ' + full_name_team + ' (' + j.getText() + ')' + '\n'

    elif request == 'races':
        href_list = []
        gran_prix = BsObj.findAll("a", {"class": "dark bold ArchiveLink"})
        for i in gran_prix:
            href_list.append(i['href'])
        dates = BsObj.findAll('td', {'class': 'dark hide-for-mobile'})
        winners = BsObj.findAll('span', {'class': 'hide-for-mobile'})
        return_string += f"Список Гран-при для {year} года: \n"
        for r, i, j, k in zip(range(1, 22), dates, winners, gran_prix):
            return_string += str(r) + '. ' + k.getText().strip().ljust(17) + i.getText().ljust(13) + j.getText().ljust(
                13) + '\n'
        return return_string, href_list

    elif request == 'calendar':
        full_page = requests.get(URL_calendar.format(year))
        BsObj = bs4.BeautifulSoup(full_page.content, features="html.parser")
        events = BsObj.findAll('legend', {'class': 'card-title f1-uppercase f1-color--warmRed'})

        starts = BsObj.findAll('span', {'class': 'start-date'})
        finishes = BsObj.findAll('span', {'class': 'end-date'})
        months = BsObj.select('span.month-wrapper')

        names = BsObj.select('div.event-place')
        return_string += f"Календарь для {year} года: \n"
        for start, finish, name, month, event in zip(starts, finishes, names, months, events):
            if event.getText().startswith('RO'):
                return_string += name.getText() + '  ' + start.getText() + '-' + finish.getText() + " " + month.getText() + '\n'
            else:
                continue

    return return_string


# standings_check('calendar')


def get_GP_results(link):
    full_page = requests.get(link)
    BsObj = bs4.BeautifulSoup(full_page.content, features="html.parser")

    date = BsObj.findAll('span', {'class': 'full-date'})[0].getText()

    dirty_positions = [i.getText() for i in BsObj.findAll('td', 'dark') if
                       (i.getText()).isdigit() or i.getText() == 'NC']
    NC_count = dirty_positions.count('NC')
    real_positions_len = int((len(dirty_positions) - NC_count * 2) / 2)
    final_positions = []
    for i in range(real_positions_len):
        final_positions.append(i + 1)
    for i in range(real_positions_len + 1, len(dirty_positions)):
        final_positions.append("NC")

    drivers = BsObj.findAll('span', {'class': 'uppercase hide-for-desktop'})
    time = [i for i in BsObj.findAll('td', {'class': 'dark bold'}) if
            (('1' in i.getText()) or ('+' in i.getText()) or ('DNF' in i.getText()))]

    return_string = ""
    return_string += date + '\n'
    for pos, driver, tm in zip(final_positions, drivers, time):
        return_string += str(pos) + '. ' + driver.getText().strip() + ' ' + tm.getText().strip() + '\n'

    return return_string
