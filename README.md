# robosys2022_mypkg

 ![test](https://github.com/ShumaKasai/mypkg/actions/workflows/test.yml/badge.svg?branch=lesson10)

ロボットシステム学で作成したROS2のテスト用パッケージ

## 動作確認済みの環境
- Ubuntu 22.04
- ROS2 Humble

## インストール
このリポジトリ―をクローンしてビルドする
```
$ cd ~/ros2_wa/src
$ git clone https://github.com/ShumaKasai/mypkg.git
$ git switch lesson10
$ colcon build
$ source ~/ros2_ws/install/setup.bash
$ source ~/ros2_wa/install/local_setup.bash
```

## 使用方法
### talker.py
0.5秒おきに、カウントアップした値を/countupへ送信する
```
$ ros2 run mypkg talker
```

### listener.py
/countupに来た値を表示する
```
$ ros2 run mypkg listener
```

### talk_listen.launch.py
talkerノードとlistenerノードを同時に実行する
```
$ ros2 launch mypkg talk_listen.launch.py
~~中略~~
[listener-2] [INFO] [1673428827.268510600] [listener]: Listen: 0
[listener-2] [INFO] [1673428827.756041800] [listener]: Listen: 1
[listener-2] [INFO] [1673428828.256801700] [listener]: Listen: 2
```

## ノードとトピック
![image](https://github.com/ShumaKasai/mypkg/blob/c075d805d7858221e7ebf3c5b26e8e90f25bd92c/ROS2_mypkg.png)
- talker・・・0.5秒おきに、カウントアップした値を/countupへ送信する
- listener・・・/countupに来た値を表示する

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.  
- このソフトウェアパッケージのコードは、許可を得て以下のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)を参考に、作成したものです.
  - [ryuichiueda/myslides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022) 

© 2022 Shuma Kasai
