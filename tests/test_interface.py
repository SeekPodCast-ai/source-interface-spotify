from unittest.mock import patch, MagicMock
from source_interface_spotify.interface import (
    SpotifyAPIInterface,
    SpotifyAPIServiceInterface,
)


# Mock environment variables
@patch.dict(
    "os.environ",
    {
        "SPOTIFY_CLIENT_ID": "fake_client_id",
        "SPOTIFY_CLIENT_SECRET": "fake_client_secret",
    },
)
class TestSpotifyAPIInterface:
    @patch("source_interface_spotify.interface.requests.request")
    @patch.object(SpotifyAPIServiceInterface, "token", new_callable=MagicMock)
    def test_get_episode(self, mock_token, mock_request):
        # Arrange
        mock_token.return_value = "fake_token"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"episode": "mock_episode_data"}
        mock_request.return_value = mock_response

        spotify_api = SpotifyAPIInterface()
        episode_id = "fake_episode_id"

        # Act
        response = spotify_api.get_episode(episode_id)

        # Assert
        mock_request.assert_called_once_with(
            method="GET",
            url=f"https://api.spotify.com/v1/episodes/{episode_id}",
            headers={"Authorization": f"Bearer {mock_token}"},
            data=None,
            json=None,
        )
        assert response.status_code == 200
        assert response.json() == {"episode": "mock_episode_data"}

    @patch("source_interface_spotify.interface.requests.request")
    @patch.object(SpotifyAPIServiceInterface, "token", new_callable=MagicMock)
    def test_get_episodes(self, mock_token, mock_request):
        # Arrange
        mock_token.return_value = "fake_token"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"episodes": "mock_episodes_data"}
        mock_request.return_value = mock_response

        spotify_api = SpotifyAPIInterface()
        episode_ids = ["fake_episode_id1", "fake_episode_id2"]

        # Act
        response = spotify_api.get_episodes(episode_ids)

        # Assert
        mock_request.assert_called_once_with(
            method="GET",
            url="https://api.spotify.com/v1/episodes?ids=fake_episode_id1%2Cfake_episode_id2",
            headers={"Authorization": f"Bearer {mock_token}"},
            data=None,
            json=None,
        )
        assert response.status_code == 200
        assert response.json() == {"episodes": "mock_episodes_data"}

    @patch("source_interface_spotify.interface.requests.request")
    @patch.object(SpotifyAPIServiceInterface, "token", new_callable=MagicMock)
    def test_get_show(self, mock_token, mock_request):
        # Arrange
        mock_token.return_value = "fake_token"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"show": "mock_show_data"}
        mock_request.return_value = mock_response

        spotify_api = SpotifyAPIInterface()
        show_id = "fake_show_id"

        # Act
        response = spotify_api.get_show(show_id)

        # Assert
        mock_request.assert_called_once_with(
            method="GET",
            url=f"https://api.spotify.com/v1/shows/{show_id}",
            headers={"Authorization": f"Bearer {mock_token}"},
            data=None,
            json=None,
        )
        assert response.status_code == 200
        assert response.json() == {"show": "mock_show_data"}

    @patch("source_interface_spotify.interface.requests.request")
    @patch.object(SpotifyAPIServiceInterface, "token", new_callable=MagicMock)
    def test_get_shows(self, mock_token, mock_request):
        # Arrange
        mock_token.return_value = "fake_token"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"shows": "mock_shows_data"}
        mock_request.return_value = mock_response

        spotify_api = SpotifyAPIInterface()
        show_ids = ["fake_show_id1", "fake_show_id2"]

        # Act
        response = spotify_api.get_shows(show_ids)

        # Assert
        mock_request.assert_called_once_with(
            method="GET",
            url="https://api.spotify.com/v1/shows?ids=fake_show_id1%2Cfake_show_id2",
            headers={"Authorization": f"Bearer {mock_token}"},
            data=None,
            json=None,
        )
        assert response.status_code == 200
        assert response.json() == {"shows": "mock_shows_data"}

    @patch("source_interface_spotify.interface.requests.request")
    @patch.object(SpotifyAPIServiceInterface, "token", new_callable=MagicMock)
    def test_get_show_episodes(self, mock_token, mock_request):
        # Arrange
        mock_token.return_value = "fake_token"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"episodes": "mock_show_episodes_data"}
        mock_request.return_value = mock_response

        spotify_api = SpotifyAPIInterface()
        show_id = "fake_show_id"

        # Act
        response = spotify_api.get_show_episodes(show_id)

        # Assert
        mock_request.assert_called_once_with(
            method="GET",
            url=f"https://api.spotify.com/v1/shows/{show_id}/episodes",
            headers={"Authorization": f"Bearer {mock_token}"},
            data=None,
            json=None,
        )
        assert response.status_code == 200
        assert response.json() == {"episodes": "mock_show_episodes_data"}
