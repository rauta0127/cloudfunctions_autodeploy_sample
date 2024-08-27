import base64
import pytest
from cloudevents.http import CloudEvent
from unittest.mock import patch
from io import StringIO
import sys

# 関数をインポート
from main import subscribe  # main.pyにコードがあると仮定


@pytest.fixture
def pubsub_event():
    # Pub/Subイベントをモックするためのデータを生成
    event_data = {
        "message": {"data": base64.b64encode(b"World").decode(), "attributes": {}}
    }

    # CloudEventのモックを作成
    headers = {
        "id": "1234567890",
        "source": "//pubsub.googleapis.com/projects/YOUR_PROJECT/topics/YOUR_TOPIC",
        "specversion": "1.0",
        "type": "google.cloud.pubsub.topic.v1.messagePublished",
    }

    return CloudEvent(headers, event_data)


def test_subscribe(pubsub_event):
    # 標準出力をキャプチャ
    captured_output = StringIO()
    sys.stdout = captured_output

    # subscribe関数を呼び出す
    subscribe(pubsub_event)

    # 標準出力に正しい内容が出力されたかを確認
    assert captured_output.getvalue().strip() == "Hello, World!"

    # 標準出力を元に戻す
    sys.stdout = sys.__stdout__
