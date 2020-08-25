import json as jsonlib
import logging

from requests import Session

logger = logging.getLogger(__name__)


class BaseSession(Session):
    BLACKLIST_HEADERS = [
        "Authorization",
    ]

    def request(
        self,
        method,
        url,
        raise_for_status=True,
        params=None,
        data=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=None,
        cert=None,
        json=None,
    ):
        if timeout is None:
            timeout = 10

        request_logging = {
            "message": "Request",
            "method": method,
            "url": url,
            "headers": self.blacklist_headers(headers or {}),
            "params": params,
        }

        logger.info(jsonlib.dumps(request_logging))
        response = super().request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            cookies=cookies,
            files=files,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects,
            proxies=proxies,
            hooks=hooks,
            stream=stream,
            verify=verify,
            cert=cert,
            json=json,
        )
        try:
            content = response.json()
        except ValueError:
            content = ""

        response_logging = {
            "message": "Response",
            "method": method,
            "status_code": response.status_code,
            "url": url,
            "content": content,
        }

        logger.info(jsonlib.dumps(response_logging))
        return response

    def blacklist_headers(self, headers):
        return {key: value for key, value in headers if key not in self.BLACKLIST_HEADERS}
