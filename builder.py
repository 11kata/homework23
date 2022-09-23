import function

CMD_TO_FUNCTION = {
    'filter': function.filter_query,
    'map': function.map_query,
    'unique': function.unique_query,
    'sort': function.sort_query,
    'limit': function.limit_query,
}
FILE_NAME = 'data/apache_logs.txt'


def build_query(cmd, param, data):
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)
