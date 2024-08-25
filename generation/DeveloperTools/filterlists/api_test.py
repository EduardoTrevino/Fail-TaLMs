import pytest
import api  # assuming the APIs are in a file named api.py


# Test the languages endpoint
def test_get_languages():
    response = api.get_languages()
    assert isinstance(response, list)  # expecting a list of languages
    assert all('id' in language for language in response)
    assert all('name' in language for language in response)


# Test the licenses endpoint
def test_get_licenses():
    response = api.get_licenses()
    assert isinstance(response, list)  # expecting a list of licenses
    assert all('id' in license for license in response)
    assert all('name' in license for license in response)


# Test the filter lists endpoint
def test_get_lists():
    response = api.get_lists()
    assert isinstance(response, list)  # expecting a list of filter lists
    assert all('id' in filter_list for filter_list in response)
    assert all('name' in filter_list for filter_list in response)


# Test the list details endpoint
def test_get_list_details():
    response = api.get_list_details(301)  # example ID
    assert isinstance(response, dict)  # expecting a dictionary with list details
    assert 'id' in response
    assert 'name' in response


# Test the maintainers endpoint
def test_get_maintainers():
    response = api.get_maintainers()
    assert isinstance(response, list)  # expecting a list of maintainers
    assert all('id' in maintainer for maintainer in response)
    assert all('name' in maintainer for maintainer in response)


# Test the software endpoint
def test_get_software():
    response = api.get_software()
    assert isinstance(response, list)  # expecting a list of software
    assert all('id' in software for software in response)
    assert all('name' in software for software in response)


# Test the syntaxes endpoint
def test_get_syntaxes():
    response = api.get_syntaxes()
    assert isinstance(response, list)  # expecting a list of syntaxes
    assert all('id' in syntax for syntax in response)
    assert all('name' in syntax for syntax in response)


# Test the tags endpoint
def test_get_tags():
    response = api.get_tags()
    assert isinstance(response, list)  # expecting a list of tags
    assert all('id' in tag for tag in response)
    assert all('name' in tag for tag in response)