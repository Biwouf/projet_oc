#Petites fonctions utiles de manière transverses
import datetime
import locale
import collections

locale.setlocale(locale.LC_TIME, "fr_FR")

def tuple_to_list_tuple(tup):
    lst = [tup]
    return lst

def lst_tuple_to_list(lst):
    output = [i[0] for i in lst]
    return output

def lst_tuple_to_tuple(lst):
    """Prend en paramètre une liste de 1 tuple"""
    return lst[0]

def unify_list(lst):
    "Supprime les doubons d'une liste"
    temp = set(lst)
    return list(temp)

#TIME
def string_to_date(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d').date()

def string_to_timestamp(date):
    return int(datetime.datetime.strptime(date, '%Y-%m-%d').timestamp())

def add_days_to_timestamp(time, days):
    return time + (3600*24)*days

def timestamp_to_date(ts):
    return datetime.datetime.fromtimestamp(ts).strftime('%A %d %B %Y')

#List/tuple operations
def keep_full(lst, idx):
    #Conserve les éléments d'une liste qui ont un nb d'occurences = idx
    output = []
    for key, value in collections.Counter(lst).items():
        if value == idx:
            output.append(key)
    return output
        