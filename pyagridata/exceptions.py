class Error(Exception):
    """Base exception for AgriData errors."""


class HTTPError(Error):
    """Raised when the API returns a non-successful HTTP response."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code}: {message}")
