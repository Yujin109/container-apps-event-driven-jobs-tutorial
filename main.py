from azure.storage.queue import QueueClient
import os
from dotenv import load_dotenv
import time

# 環境変数から設定を読み込む
load_dotenv()
connection_string: str = os.getenv('AZURE_STORAGE_CONNECTION_STRING', default="")
queue_name: str = os.getenv('AZURE_STORAGE_QUEUE_NAME', default="")

if not connection_string:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRINGが設定されていません。")
if not queue_name:
    raise ValueError("AZURE_STORAGE_QUEUE_NAMEが設定されていません。")


def sleep(seconds: int) -> None:
    """指定された秒数だけプログラムを停止します。"""
    time.sleep(seconds)


def main() -> None:
    # QueueClientのインスタンスを作成
    queue_client = QueueClient.from_connection_string(
        conn_str=connection_string,
        queue_name=queue_name
        )

    # 1. キューからメッセージを1つ受信する
    messages = queue_client.receive_messages(
        messages_per_page=1,
        visibility_timeout=60
        )

    for message in messages:
        # 2. メッセージを処理する（ここでは単に表示するだけ）
        print(f"Processing message: {message.content}")
        # 3. 指定した時間だけsleepする（例: 5秒）
        sleep(300)
        # 4. キューからメッセージを削除
        queue_client.delete_message(message)
        print("Message processed and deleted")

        # 一つのメッセージを処理したらループを抜ける
        break
    else:
        print("No message received. Exiting...")


if __name__ == "__main__":
    main()
