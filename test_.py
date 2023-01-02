import parser

class TestSuite():
    def test_iperf_server_connection(self,server):
        error = server
        assert not error

    def test_iperf_client_connection(self,client):
        stdout, error = client
        assert not error
        dict = parser.parser(stdout)
        assert dict != []
        for value in dict:
            assert float(value["Transfer"]) > 500.5