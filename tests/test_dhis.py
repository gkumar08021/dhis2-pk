import pytest

from src.core.dhis import Dhis


@pytest.fixture()
def dhis():
    return Dhis(server='play.dhis2.org/demo', username='admin', password='district', api_version=None)


@pytest.fixture()
def dhis_with_api_version():
    return Dhis(server='play.dhis2.org/demo', username='admin', password='district', api_version=26)


@pytest.fixture()
def dhis_with_https():
    return Dhis(server='https://play.dhis2.org/demo', username='admin', password='district', api_version=None)


@pytest.fixture()
def dhis_without_https():
    return Dhis(server='http://play.dhis2.org/demo', username='admin', password='district', api_version=None)


@pytest.fixture()
def dhis_localhost():
    return Dhis(server='localhost:8080', username='admin', password='district', api_version=None)


@pytest.fixture()
def dhis_localhost_ip():
    return Dhis(server='127.0.0.1:8080', username='admin', password='district', api_version=None)


def test_demo_server_200(dhis):
    response = dhis.get(endpoint='me')
    assert response['email'] == 'someone@dhis2.org'


def test_get_object_types(dhis):
    passed_objects = [
        'cat', 'catcombo', 'catcombos', 'categories', 'categorycombination', 'categorycombinations', 'categorycombo',
        'categorycombos', 'categoryoption', 'categoryoptiongroup', 'categoryoptiongroups', 'categoryoptiongroupset',
        'categoryoptiongroupsets', 'categoryoptions', 'catoption', 'catoptiongroup', 'catoptiongroups',
        'catoptiongroupset', 'catoptiongroupsets', 'catoptions', 'catscategory', 'chart', 'charts', 'constant',
        'constants', 'dashboard', 'dashboards', 'dataapprovallevels', 'dataelement', 'dataelementgroup',
        'dataelementgroups', 'dataelementgroupset', 'dataelementgroupsets', 'dataelements', 'dataset',
        'datasetapprovallevel', 'datasets', 'datavisualization', 'datavisualizations', 'datavizualisation',
        'datavizualizations', 'de', 'deg', 'degroup', 'degroups', 'degroupset', 'degroupsets', 'degs', 'des',
        'document', 'documents', 'ds', 'eventchart', 'eventcharts', 'eventreport', 'eventreports', 'eventtables', 'i',
        'ig', 'igs', 'ind', 'indgroups', 'indgroupsets', 'indicator', 'indicatorgroup', 'indicatorgroups',
        'indicatorgroupset', 'indicatorgroupsets', 'indicators', 'interpretation', 'interpretations', 'legendset',
        'legendsets', 'map', 'maps', 'optiongroup', 'optiongroups', 'optiongroupset', 'optiongroupsets', 'optionsets',
        'organisationunitgroups', 'organisationunitgroupsets', 'orgunitgroup', 'orgunitgroups', 'orgunitgroupset',
        'orgunitgroupsets', 'os', 'oug', 'ougroup', 'ougroups', 'ougroupset', 'ougroupsets', 'ougs', 'pi', 'pivottable',
        'pivottables', 'program', 'programindicator', 'programindicators', 'programs', 'report', 'reports',
        'reporttable', 'reporttables', 'sqlview', 'sqlviews', 'tea', 'teas', 'trackedentityattribute',
        'trackedentityattributes', 'ug', 'usergroup', 'usergroups', 'validationrule', 'validationrulegroup',
        'validationrulegroups', 'validationrules'
    ]

    for elem in passed_objects:
        dhis.get_object_type(elem)


def test_get_no_object_types(dhis):
    with pytest.raises(SystemExit):
        dhis.get_object_type('blupaodo')


def test_api_version(dhis_with_api_version):
    assert dhis_with_api_version.api_url == 'https://play.dhis2.org/demo/api/26'


def test_no_api_version(dhis):
    assert dhis.api_url == 'https://play.dhis2.org/demo/api'


def test_https_in_url(dhis):
    assert dhis.api_url.startswith('https://')


def test_localhost_url(dhis_localhost):
    assert dhis_localhost.api_url.startswith('http://localhost:8080')


def test_double_https_url(dhis_with_https):
    assert dhis_with_https.api_url == 'https://play.dhis2.org/demo/api'


def test_localhost_ip(dhis_localhost_ip):
    assert dhis_localhost_ip.api_url == 'http://127.0.0.1:8080/api'


def test_url_with_api():
    with pytest.raises(SystemExit):
        Dhis(server='play.dhis2.org/demo/api', username='admin', password='district', api_version=None)
