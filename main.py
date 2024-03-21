from dotenv import load_dotenv
import time

# 環境変数から設定を読み込む
load_dotenv()


def sleep(seconds: int) -> None:
    """指定された秒数だけプログラムを停止します。"""
    time.sleep(seconds)


def main() -> None:
    print("処理全体を開始します。")
    for i in range(1):
        print(f"{i+1}回目の処理を開始します。")
        sleep(30)
        print(f"{i+1}回目の処理を終了します。")
    print("処理全体を終了します。")


if __name__ == "__main__":
    main()
