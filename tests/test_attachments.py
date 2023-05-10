import json
import allure
from allure import attachment_type


def test_for_attachments():
    allure.attach("Some text", name='Text', attachment_type=attachment_type.TEXT)
    allure.attach(
        "<h1>HTML file</h1>", name='Html', attachment_type=attachment_type.HTML
    )
    allure.attach(
        json.dumps({"first": 1, "second": 2}),
        name='json',
        attachment_type=attachment_type.JSON,
    )
