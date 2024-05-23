from datetime import datetime
import re


def pad_dict_lists(input_dict:dict):
    max_length = max(len(lst) for lst in input_dict.values() if isinstance(lst,list))

    for k,v in input_dict.items() :
        if isinstance(v, list):
            current_length = len(input_dict[k])
            if current_length < max_length:
                input_dict[k].extend(['_'] * (max_length - current_length))

    return input_dict

def get_attrs_from_mode(html, attr):
    return html.get_attribute(attr)


def reformat_date(date_raw, input_format: str = '%d %b, %Y', output_format: str = '%Y-%m-%d'):
    dt_obj = datetime.strptime(date_raw, input_format)
    return datetime.strftime(dt_obj, output_format)


def cleanup_titles(titles: list):
    titles_list = []
    for title in titles:
        t = title.replace('Buy', '').replace('(?)', '')
        titles_list.append(t)
    return titles_list


def regex(input_list):
    price_list = []
    for p in input_list:
        p = re.sub('[^.$0-9]', '', p)
        if p == '':
            p = 'Free to Play'
        elif p.count("$") == 2:
            price = p.split('$')
            price_list.append(f' {price[1]} $')
        else:
            price_list.append(p)
    return price_list

def d_price_regex(input_list):
    price_list = []
    for p in input_list:
        p = re.sub('[^.$0-9]', '', p)
        if p.count("$") == 2:
            price = p.split('$')
            price_list.append(f' {price[2]} $')
        else:
            pass
    return price_list
def format_and_transform_steam(attrs: dict):
    transforms = {
        'game_img': lambda i: get_attrs_from_mode(i, 'src'),
        'popular_tags': lambda tags: str(tags),
        'release_date': lambda date: reformat_date(date, '%d %b, %Y', '%Y-%m-%d'),
        'game_title': lambda title: cleanup_titles(title),
        'game_price': lambda raw_price: regex(raw_price),
        'd_game_price': lambda raw_price: d_price_regex(raw_price)
    }
    for k, v in transforms.items():
        if k in attrs:
            attrs[k] = v(attrs[k])
    return attrs


def format_and_transform_epic(attrs: dict):
    transforms = {
        'game_img': lambda i: get_attrs_from_mode(i, 'src'),
        'popular_tags': lambda tags: str(tags),
        'release_date': lambda date: reformat_date(date, '%m/%d/%y', '%Y-%m-%d')
    }

    for k, v in transforms.items():
        try:

            if k in attrs:
                attrs[k] = v(attrs[k])
        except:
            pass
    return attrs

