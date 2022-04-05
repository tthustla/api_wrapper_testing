import vcr
from pytest import fixture
import pytest
from tmdbwrapper import TV
from requests.exceptions import HTTPError

tmdb_vcr = vcr.VCR(filter_query_parameters=['api_key'])


# @fixture
# def tv_keys():
#     # Responsible only for returning the test data
#     return ['id', 'origin_country', 'poster_path', 'name',
#             'overview', 'popularity', 'backdrop_path',
#             'first_air_date', 'vote_count', 'vote_average']


@tmdb_vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml')
def test_tv_popular():
    """Tests an API call to get a popular tv shows"""

    tv_instance = TV()
    data = tv_instance.popular(1)

    assert isinstance(data, list)
    assert isinstance(data[0], tuple)
    assert len(data[0]) == 4

@tmdb_vcr.use_cassette('tests/vcr_cassettes/tv-popular_fail.yml')
def test_tv_popualr_exception():
    tv_instance = TV()
    with pytest.raises(HTTPError):
        tv_instance.popular(501)