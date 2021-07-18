from intermine.webservice import Service

service = Service('https://build.alliancegenome.org/alliancemine/service')
to_check = []


def assert_result(query_number, number_of_rows, expected_result):
    """

    :param query_number:
    :param number_of_rows:
    :param expected_result:
    :return:
    """

    try:
        assert len(number_of_rows) == expected_result
        return 'Query #' + query_number + ' PASSED. Returned ' + str(len(number_of_rows))
    except Exception as e:
        to_check.append(query_number)
        return 'Query #' + query_number + ' FAILED. Expected ' + str(expected_result) + ' returned ' + str(len(number_of_rows))


def assert_greater(query_number, number_of_rows, minimum):
    """

    :param query_number:
    :param number_of_rows:
    :param minimum:
    :return:
    """

    try:
        assert len(number_of_rows) >= minimum
        return 'Query #' + query_number + ' PASSED. Returned ' + str(len(number_of_rows))
    except Exception as e:
        to_check.append(query_number)
        return 'Query #' + query_number + ' FAILED. Expected ' + str(minimum) + ' returned ' + str(len(number_of_rows))


def query_01():
    """

    :return:
    """


    query = service.new_query('Gene')
    query.add_view('primaryIdentifier')
    query.add_constraint('organism.name', '=', 'Caenorhabditis elegans', code='A')
    query.add_constraint('primaryIdentifier', '!=', 'WB:WBGene*', code='B')

    return assert_result('01', query.rows(), 0)


def query_02():
    """

    :return:
    """

    query = service.new_query('Gene')
    query.add_view('primaryIdentifier')
    query.add_constraint('organism.name', '=', 'Danio rerio', code='A')
    query.add_constraint('primaryIdentifier', '!=', 'ZFIN:ZDB-GENE*', code='B')

    return assert_result('02', query.rows(), 0)


def query_03():
    """

    :return:
    """


    query = service.new_query('Gene')
    query.add_view('primaryIdentifier')
    query.add_constraint('organism.name', '=', 'Drosophila melanogaster', code='A')
    query.add_constraint('primaryIdentifier', '!=', 'FB:FBgn*', code='B')

    return assert_result('03', query.rows(), 0)

def query_04():
    """

    :return:
    """

    query = service.new_query('Gene')
    query.add_view('primaryIdentifier', 'synonyms.value')
    query.add_constraint('synonyms.value', '=', ' CG1034', code='A')

    return assert_result('04', query.rows(), 1)


def query_05():
    """

    :return:
    """

    query = service.new_query('Gene')
    query.add_view('primaryIdentifier', 'synonyms.value')
    query.add_constraint('synonyms.value', '=', ' CG1034', code='A')

    return assert_result('05', query.rows(), 1)


def query_06():
    """

    :return:
    """

    query = service.new_query('Gene')
    query.add_view('primaryIdentifier')
    query.add_constraint('organism.name', '=', 'Caenorhabditis elegans', code='A')
    query.add_constraint('primaryIdentifier', '=', 'WB:WBGene*', code='B')

    return assert_result('06', query.rows(), 48785)


def query_07():
    """

    :return:
    """

    query = service.new_query("Gene")
    query.add_view("primaryIdentifier", "synonyms.value")
    query.add_constraint("synonyms.value", "==", " predicted gene", code="A")

    return assert_result('07', query.rows(), 0)



if __name__ == '__main__':

    print(query_01())
    print(query_02())
    print(query_03())
    print(query_04())
    print(query_05())
    print(query_06())