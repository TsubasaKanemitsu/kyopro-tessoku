## 2章
### 一次元の累積和
#### A07
- 前提
    - 複数の区間の重なり部分の総和を求めたい。
    - 求めたい区間の数と区間の範囲数が多いと全探索はできない
- 対応方法
    - 区間の開始位置にフラグを立てる。（今回は1とする）
    - 区間の終了位置の次の位置でフラグを下げる。（今回は-1とする）
    - 累積和を計算すると[開始, 終了]の位置の全てにフラグが立つことになり、終了後はフラグ下がる。
        - 例：区間の開始と終了を1 ~ 3とすると[0, 1, 0, 0, -1, 0, 0]という風にフラグを設定する。累積和を計算すると[0, 1, 1, 1, 0, 0, 0]となり、区間の[開始、終了]部分のみフラグを立てることができる。
    - 上記を応用し、複数の区間に対しても同様の処理を行うことで、O(N)で解答できる。

#### B07
t + 0.5というのが肝である。
+ 0.5の時を見るということは、人を減らすタイミングはr + 1ではなく、rにしておかないと、r + 0.5のタイミングで人が存在していることになってしまう。

### 二次元の累積和
