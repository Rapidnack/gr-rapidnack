# gr-rapidnack

gr-rapidnackプロジェクトは、Intel FPGAとCypress EZ-USB FX2LPを使ったCSRP(Cheap Software Radio Peripheral)を制御するGNU Radioモジュールのソースコードです。

![画像1](http://rapidack.sakura.ne.jp/ttl/wp-content/uploads/2019/05/GRC_CSRP1.png)
![画像2](http://rapidack.sakura.ne.jp/ttl/wp-content/uploads/2019/05/GRC_CSRP2.png)
![画像3](http://rapidack.sakura.ne.jp/ttl/wp-content/uploads/2019/05/GRC_CSRP3.png)

次の手順でインストールできます。
```
$ cd gr-rapidnack
$ mkdir build
$ cd build
$ cmake ../
$ make
$ sudo make install
$ sudo ldconfig
```
  
# Authors

[Rapidnack](http://rapidnack.com/)

# References

[https://github.com/Rapidnack/CsrpServer](https://github.com/Rapidnack/CsrpServer)

[https://github.com/Rapidnack/gr-rapidnack](https://github.com/Rapidnack/gr-rapidnack)

[https://github.com/Rapidnack/Spi1FifoIn](https://github.com/Rapidnack/Spi1FifoIn)

[https://github.com/Rapidnack/MAX1000_SDR_FX2LP](https://github.com/Rapidnack/MAX1000_SDR_FX2LP)

[https://github.com/Rapidnack/MAX10FB_SDR_FX2LP](https://github.com/Rapidnack/MAX10FB_SDR_FX2LP)

[https://github.com/Rapidnack/CYC4_SDR_FX2LP](https://github.com/Rapidnack/CYC4_SDR_FX2LP)

[https://github.com/Rapidnack/CYC2_SDR_FX2LP](https://github.com/Rapidnack/CYC2_SDR_FX2LP)
