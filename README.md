# pyInfinex
Python wrapper for the Infinex crypto exchange API

# How to use
- Some of the API endpoints are public, but some are private, meaning that you need an API key to access them - ex: posting a trading order, viewing your open orders ...

- To use the public API you do not need anything special, just run any public method from either spot, or wallet endpoints.

- To use the private API you first have to add a new entry in your user's path called "INFINEX_API_KEY" which must contain the API key created on infinex.cc

- All the available wrapper functions can be found in _EXAMPLE.py.

- Official API documentation: https://github.com/infinex-exchange/api-docs

# Setup
## Ubuntu (tested with 22.04.2)
### Prerequisites
```
sudo apt install git
sudo apt install python3-venv
```

### Installation
```
git clone https://github.com/ageorge95/pyInfinex pyInfinex
cd pyInfinex
sh install.sh
```

## Windows (tested with win10Pro, win11Pro)
### Prerequisites
- git for windows: https://gitforwindows.org/
- python 3.x (>=3.9, 3.11 is recommended): https://www.python.org/downloads/

### Installation
```
git clone https://github.com/ageorge95/pyInfinex pyInfinex
cd pyInfinex
install.bat
```

# Feedback/ Contribution

If you are stuck/ need more details on how to use any of the API functions you can join Infinex's official Discord server: https://discord.gg/4U8p99NBn7

Or you can directly create an issue on this repository and I will answer ASAP.

# Support
Found this project useful? Send your ❤ in any form you can 🙂. Please contact me if you donated and want to be added to the contributors list !
- apple APPLE---apple1tdscevmlwa03rt464mr03tf6qs6y2xm3ay4z9lzn9pshad6jkp2s4crqd9
- salvia XSLV---xslv19j3zexpgels2k8fkp30phxpxxz6syfzq52t2tuy8ac50nfmnennse9vjcw
- chia XCH---xch1glz7ufrfw9xfp5rnlxxh9mt9vk9yc8yjseet5c6u0mmykq8cpseqna6494
- cryptodoge XCD---xcd1ds6jljkla5gwfjgty8w4q442uznmw9erwmwnvfspulqke3ya9nxqy9fe8t
- flax XFX---xfx13uwa4zqp0ah5740mknk0z8g3ejdl06sqq8ldvvk90tw058yy447saqjg3u
- cannabis CANS---cans16ur4nqvvtdr8yduum5pljr3a73q33uuage6ktnsdr579xeerkc5q604j5v
- wheat WHEAT---wheat1z4cz3434w48qumwt2f2dqtmgq4lfyv5aswmda7yfmamhml2afrzsa80mr2
- taco XTX---xtx1crayqhdtx2rs5680q65c0c2ndaltje6vem0u0nnxtks4ucy058uqc0ak8m
- greendoge GDOG---gdog1ry524dunyuxkrjmzrdrgf5y6hzcdl0fghmncfcxxl83jknn82kmstzjjxk
- tad TAD---tad19s5nxa04znxsl7j6hud8p0uqtmnwd770d5a3nz40dtgwnuufjz0sgfcpnx
- spare SPARE---spare12e68ghay27pcdyuqcaz5qvtwst5mxzht33nxsxmygcd8nnxzhj6qjzytex
- cactus CAC---cac189er7g8gfsr6yl40t6gq8qygcrsjxkzhp50sk2xa6wh0f2nxzrhsm6rkfe
- flora XFL---xfl149k04h5p9crzsl0xz50efzka9clt56xtg5h33l35m8ld9h2knhqqvs7u76
- kale XKA---xka1m7hskvcd8xqx0a2e5nxc3ldn8gcz83pwvlkgd5x8vflaaq3uetmqj0ztk5
- maize XMZ---xmz1ycj7x6tsajgyannvr92udj23dsj6l4syqx38pmpzf6e7kkeeuvysscdvyw
- hddcoin HDD---hdd1qfs8hdtdrmsw9ya04cjex0d6dzkn7lfv7vp9g2dgup3p87ye9gqs6zvam2
- dogechia XDG---xdg17g6zx3u2a2zslwxrm0spv2297ygnuzhyme89x8kd5mrjz7mns39q6ge64c
- nchain ext9 NCH---nch1ae8hujcantv7naes30etvvcssm6uak9xzd5edwhtyq05adt60hkqlgyfmz
- chives XCC---xcc1amn5txlltvlcnlt6auw24ys6xku7t3npqt2szllassymswnehepszhnjar
- BTCGreen xBTC---xbtc1njnsnayxuj4nn0fnzf2nsjnladh79spljx5vvs8v6vqhk9kp6rksgvyszh
- Pipscoin PIPS---pips13qcawq6y5dkxqtwnup04m2zmee9lpzsec0zyczt0pd0ra6cuut3qgvhj0k
- mint XKM---xkm1k0nkq575wm3nmtkkxwrfmxg7qpt0hxe5m2fvw0dgvw3q0ynmzn3qqu5ntf
- stor STOR---stor1vahvcz80arp2jl6v4np8grjxncrypzfelmm4uk0gvds5rpuf523qn9w482
- tranzact  TRZ---trz1mct7p22g2m9gn9m0xtuac4mnrwjkev0pqsxgx7tr6cjk2thnxmkq8q45ep
- Staicoin STAI---stai1m0axlhek947j5mz2wpvy0m9sky49h3jfqwqesy8rmzxfv9j9k5kq9zl6ft
- Skynet XNT---xnt1cq8xdu8svwhruefr5khzpqxturemtqrf6gk7uqjyjrhdl2dyapmsh9desg
- Shibgreen XSHIB---xshib1pkelrz8uml46m6hdw06ttezhaqasexe0527jce4cc03uj4fc8rcsaaatwy
- Silicoin SIT---sit1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqj0s60a
- bpx BPX---bpx10d25g8jechcs2rfstkzpj2rzt68skw4etvqm2j7f8545uzd6kyrqgr2ea8
- Gold GL---gl1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqqwx0ye
- profit---profit1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqfhghvg
- littlelambocoin LLC---llc1wfhhxn4dtr7luedc4lzld2y2q32r66ruvqyppj7vr6g5u75xn92s3pz9gw
- ecostake ECO---eco1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrq5l9vpy
- chinilla HCX---hcx16ce9d6pj80nw6j2j9hgax30k6ww43na3ve86pm87tecsdhgc03sq7cvnmt
- petroleum XPT---xpt1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqq2qcs2
- seno XSE---xse1jx8mvumy9243t8qcu0e476r0azvckyaeyhnmu6jswxcr57q09zyqla5w2a
- lucky SIX---six1r09eundsl9ntdw5vgq9xk9qedcvxdg7tg3urndcewppc3cn55p2syhu2d4
- moon---moc1k49pfczryvea0h3hf6ls2fm6gykhaa9jymfhuy27790f470rt8js770rdv
- lotus LCH---lch1yxmdv2jykwsvmwemka3uc2g3zg7dqfaevd8n2z2jht9nstsammtsyla2ex
- Coffee XCF---xcf1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqcq54t6
- ethgreen XETH---xeth1e24uzser8h78gun2jppnqsgx7vsrktzkgdeuknat63ppcfw7htuq2pu73a
- goji XGJ---xgj1x0xyfmkz0xylyaaq6360un9hydjc543lrtuwu9pk5d008acq939qrlgdut
- greenbtc GBTC---gbtc1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqw0awqh
- kiwi KIK---kik1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrqhks6s3
- ballcoin BALL---ball1df3l4xpzc65xyzvdlleww6stwt70kd9a4ra0836hf6ahpcwd7yrq864g6s
- one XONE---xone1n52zrtr8k3sfdux47jy7luhrj77fcnqhwn6grmammt5zl3p9xgrs4cmuf7
