#!/usr/bin/env python3

"""
Tests of module: core.results.app

"""
import datetime
import unittest

from deepnox.helpers.testing_helpers import BaseTestCase
from deepnox.network.http import HttpRequest, HttpResponse, HttpHit, HttpMethod
from deepnox.third import arrow


class HttpRequestTestCase(BaseTestCase):
    """
    Unit tests for {HttpRequest}.
    """

    def test____init__(self):
        """
        Test: create a new {HttpRequest}
        :return:
        """
        self.assertIsInstance(HttpRequest(), HttpRequest)

    def test__size(self):
        request_summary = HttpRequest(body='body_test')
        self.assertEqual(request_summary.size, 9)

    def test__dict(self):
        request_summary = HttpRequest(body='body_test')
        self.assertEqual({"body": "body_test", "size": 9, "method": HttpMethod.GET},
                         request_summary.dict())


class HttpResponseTestCase(unittest.TestCase):
    """
    Unit tests for {HttpResponse}.
    """

    def test____init__(self):
        """
        Test: create a new {HttpResponse}
        :return:
        """
        self.assertIsInstance(HttpResponse(status_code=200,
                                           size=56,
                                           headers={"Content-Type": "application/json"},
                                           text="response_text_test",
                                           elapsed_time=120), HttpResponse)

    def test__dict(self):
        """
        Test: convert network response summary to dict.
        """
        response_summary = HttpResponse(status_code=200,
                                        size=56,
                                        headers={"Content-Type": "application/json"},
                                        text="response_text_test",
                                        elapsed_time=120)
        self.assertEqual(response_summary.dict(), {"status_code": 200,
                                                   "size": 56,
                                                   "headers": {"Content-Type": "application/json"},
                                                   "text": "response_text_test",
                                                   "elapsed_time": 120,
                                                   })


class HttpHitTestCase(BaseTestCase):
    """
    Unit tests for {HttpHit}.
    """

    def test____init__(self):
        """
        Test: create a new {HttpHit}
        :return:
        """
        request = HttpRequest(body='body_test')
        response = HttpResponse(status_code=200,
                                size=56,
                                headers={"Content-Type": "application/json"},
                                text="response_text_test",
                                elapsed_time=120)
        self.assertIsInstance(HttpHit(
            start_at=arrow.now().datetime,
            end_at=arrow.now().shift(seconds=+1).datetime,
            request=request,
            response=response,
        ), HttpHit)

    def test__dict(self):
        """
        Test: convert network hit to dict.
        """
        request_summary = HttpRequest(body='body_test')
        response_summary = HttpResponse(status_code=200,
                                        size=56,
                                        headers={"Content-Type": "application/json"},
                                        text="response_text_test",
                                        elapsed_time=120)

        now = datetime.datetime.now()
        http_hit = HttpHit(
            start_at=now,
            end_at=now,
            request=request_summary,
            response=response_summary, )
        self.assertEqual(http_hit.dict(),
                         {"start_at": now,
                          "end_at": now,
                          "request": {"body": "body_test", "size": 9},
                          "response": {"status_code": 200,
                                       "size": 56,
                                       "headers": {"Content-Type": "application/json"},
                                       "text": "response_text_test",
                                       "elapsed_time": 120,
                                       }
                          })


if __name__ == '__main__':
    unittest.main()
