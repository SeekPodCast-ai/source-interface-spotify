import json
import traceback
from typing import Any, Union, List, Dict
import urllib.parse
import requests
import os
import logging
from rauth import OAuth2Service

logger = logging.getLogger("source_interface_spotify")

JsonSerializable = Union[
    None, bool, int, float, str, List["JsonSerializable"], Dict[str, "JsonSerializable"]
]


class SpotifyAPIServiceInterface:
    def __init__(self):
        self.__client_id = os.environ["SPOTIFY_CLIENT_ID"]
        self.__client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
        self.__authorize_url = "https://accounts.spotify.com/authorize"
        self.__access_token_url = "https://accounts.spotify.com/api/token"
        self.__base_url = "https://api.spotify.com/v1/"
        self.data = {"grant_type": "client_credentials"}
        self.decoder = lambda content: json.loads(content)
        self.headers = {"Authorization": "Bearer {access_token}"}
        self.__service = None
        self.__token = None

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, value):
        if not value:
            try:
                self.__service = OAuth2Service(
                    client_id=self.__client_id,
                    client_secret=self.__client_secret,
                    name="spotify",
                    authorize_url=self.__authorize_url,
                    access_token_url=self.__access_token_url,
                    base_url=self.__base_url,
                )
            except Exception as service_err:
                logger.critical(f"Unable to create Spotify Service: {service_err}")
                traceback.print_exc()
                raise service_err

    @property
    def token(self):
        try:
            return self.__service.get_access_token(data=self.data, decoder=self.decoder)
        except Exception as token_error:
            logger.critical(f"Unable to get Spotify Token: {token_error}")
            traceback.print_exc()
            raise token_error


class SpotifyBaseAPIInterface(SpotifyAPIServiceInterface):
    def __init__(self):
        super().__init__()

    def get_response(
        self,
        url: str,
        method: str,
        headers: dict | None = None,
        data: Any = None,
        json_data: JsonSerializable = None,
    ):
        if headers is not None and isinstance(headers, dict):
            self.headers = self.headers | headers
            self.headers.update({"Authorization": f"Bearer {self.token}"})
        try:
            response = requests.request(
                method=method, url=url, headers=headers, data=data, json=json_data
            )
            response.raise_for_status()
        except Exception as api_error:
            logger.critical(
                f"An error occured while calling API with endpoint - {url}. Got {api_error}"
            )
            traceback.print_exc()
            raise api_error


class SpotifyAPIInterface(SpotifyBaseAPIInterface):
    def __init__(self):
        super().__init__()
        self.__get_episode_endpoint = self.__base_url + "episodes/{id}"
        self.__get_episodes_endpoint = self.__base_url + "episodes?ids={ids}"
        self.__get_show_endpoint = self.__base_url + "shows/{id}"
        self.__get_shows_endpoint = self.__base_url + "shows?ids={ids}"
        self.__get_show_episodes_endpoint = self.__base_url + "shows/{id}/episodes"

    def get_episode(self, episode_id: str):
        return self.get_response(
            url=self.__get_episode_endpoint.format(id=episode_id), method="GET"
        )

    def get_episodes(self, episode_ids: List[str]):
        return self.get_response(
            url=self.__get_episodes_endpoint.format(
                ids=urllib.parse.quote(",".join(episode_ids))
            ),
            method="GET",
        )

    def get_show(self, show_id: str):
        return self.get_response(
            url=self.__get_show_endpoint.format(id=show_id), method="GET"
        )

    def get_shows(self, show_ids: List[str]):
        return self.get_response(
            url=self.__get_shows_endpoint.format(
                ids=urllib.parse.quote(",".join(show_ids))
            ),
            method="GET",
        )

    def get_show_episodes(self, show_id: str):
        return self.get_response(
            url=self.__get_show_episodes_endpoint.format(id=show_id), method="GET"
        )
