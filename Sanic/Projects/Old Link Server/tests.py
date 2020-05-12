import uuid

from link_shortener.server import app
from link_shortener.models import actives


class TestActiveLinks:
    '''
    Unit tests for the active_links model.
    '''
    def setup_method(self, test_method):
        self.identifier = str(uuid.uuid1())
        self.owner = 'test.owner@applifting.cz'
        self.owner_id = '0' * 21
        self.endpoint = 'vlk'
        self.url = 'http://www.vlk.cz'

    def test_endpoint_length(self):
        '''
        Test the maximum length of an endpoint attribute.
        '''
        request, response = app.test_client.get('/links/about')
