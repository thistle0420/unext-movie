# U-NEXT作品一覧取得

## 概要

U-NEXTをスクレイピングして作品一覧を取得する

毎日9時に全作品(洋画、邦画、海外ドラマ、国内ドラマ、アニメ)をJSON形式で取得する

![image](https://github.com/thistle0420/unext-movie/assets/85113388/db26041a-e8d4-40e5-9685-f3d36a2ad0b7)

U-NEXTに存在している作品であれば上記以外のカテゴリの作品も取得可能。

| カテゴリ | コード |
| ---- | ---- |
| 洋画 | MNU0000141 |
| 邦画 | MNU0000709 |
| 海外ドラマ | MNU0000725 |
| 韓流・アジア | MNU0000739 |
| 国内ドラマ | MNU0000753 |
| アニメ | MNU0000768 |
| キッズ | MNU0000787 |
| ドキュメンタリー | MNU0000840 |
| 音楽・ライブ | MNU0000850 |
| エンタメ・スポーツ | MNU0000800 |
| 舞台・演劇 | MNU0011143 |

## 環境

```bash
python --version
Python 3.10.12
```

## 導入

```bash
pip install -r requirements.txt
python src/main.py
```
