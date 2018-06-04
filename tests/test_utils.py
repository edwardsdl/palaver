import pytest

from palaver import utils
import pkg_resources


@pytest.mark.parametrize('filename, expected_access_code',
                         [('1.jpg', '0340-1222-1611-07003-01033992'),
                          ('2.jpg', '0340-1222-1611-07003-01033992'),
                          ('3.jpg', None)])
def test_get_access_code(filename, expected_access_code):
    image_path = pkg_resources.resource_filename('tests.surveys', filename)

    assert expected_access_code == utils.get_access_code(image_path)
