### 仮想環境

- 作成　：　conda create -n gym_trading python=3.6 anaconda
- 確認　：　conda info -e
- 削除　：　conda remove -n gym_trading --all
- コピー：　conda env export > gym_test.yaml
- 複製　：　conda env create -f gym_test.yaml